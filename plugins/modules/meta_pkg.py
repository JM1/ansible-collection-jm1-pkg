#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim:set fileformat=unix shiftwidth=4 softtabstop=4 expandtab:
# kate: end-of-line unix; space-indent on; indent-width 4; remove-trailing-space on;

# Copyright: (c) 2020, Jakob Meng <jakobmeng@web.de>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = r'''
---

module: meta_pkg

short_description: Use meta packages to simplify maintenance of the OS package manager.

description:
    - "This module allows to build, install and remove meta packages easily. Meta packages simplify the
       installation and removal of packages, using the OS package manager. A meta package does not ship nor
       manipulate any file or directory. It defines relationships between packages only [1][2], e.g. dependencies or
       conflicts. When a meta package is installed, the OS package manager will install or remove packages automatically
       to satisfy all relationships declared by the meta package. On systems that use dpkg (apt), such as Debian, Ubuntu
       and their derivatives, dependend packages will be marked as automatically installed. As soon as the meta package
       has been removed, all automatically installed packages will be removed as well. On systems that use dnf or an
       up-to-date yum, such as Fedora or CentOS, one might use 'dnf autoremove' or 'yum autoremove' to trigger the same
       autoremoving behaviour [2].

       For example, a meta package helps with deploying an updated list of packages. Previously installed packages which
       have been removed from the updated list, will be uninstalled automatically by the OS package manager, once the
       new meta package version is rolled out.

       Ref.:
       [1] U(https://www.debian.org/doc/debian-policy/ch-relationships.html)
       [2] U(https://docs.fedoraproject.org/en-US/packaging-guidelines/)
       [3] U(https://dnf.readthedocs.io/en/latest/command_ref.html#autoremove-command-label)
      "

requirements:
    - apt (e.g. in debian package python3-apt) [apt-based distributions only]
    - backports.tempfile (python 2 only)
    - dnf [dnf-based distributions only]
    - equivs-build (e.g. part of debian package equivs) [apt-based distributions only]
    - jinja2 (e.g. part of package python3-jinja2)
    - rpmbuild (e.g. in package rpm-build) [dnf-based or yum-based distributions only]
    - yum (python 2 only) [yum-based distributions only]

options:

    architecture:
        aliases: [ buildarch ]
        default: all or noarch
        description:
            - "Architecture specification string, e.g. C(all) for Debian or C(noarch) for Fedora."
        type: str

    conflicts:
        default: []
        description:
            - "When a package declares a conflict with another using I(conflicts), the package manager will refuse to
               allow them to be installed or/and unpacked on the system at the same time."
        type: list

    depends:
        aliases: [ requires ]
        default: []
        description:
            - "Declares an absolute dependency, it is required for the software to function correctly."
        type: list

    description:
        default: "Package management made easy."
        description:
            - "Contains an extended description of the meta package. The description should describe the meta package to
               a user (system administrator) who has never met it before so that they have enough information to decide
               whether they want to install it. Beware: Distributions based on both, apt (deb) and yum/dnf (rpm) do
               place several restrictions on the I(description) field. For example, the I(description) must not contain
               tabs and no lines longer than 80 characters. Details in
               U(https://www.debian.org/doc/debian-policy/ch-controlfields.html#s-f-description) and
               U(https://docs.fedoraproject.org/en-US/packaging-guidelines/#_summary_and_description)."
        type: str

    enhances:
        default: []
        description:
            - "This field is similar to I(suggests) but works in the opposite direction. It is used to declare that a
               package can enhance the functionality of another package."
        type: list

    maintainer:
        aliases: [ packager ]
        default: "{{Full Name}} <{{username}}@{{fqdn}}>"
        description:
            - "The package maintainer’s name and email address. The name must come first, then the email address inside
               angle brackets <> (in RFC822 format)."
        type: str

    manager:
        choices: [auto, apt, dnf, yum]
        default: auto
        description:
            - "The package manager to use, e.g. apt or yum. The default C(auto) will use existing facts or try to
               autodetect it. You should only use this field if the automatic selection is not working for some reason."
        type: str

    name:
        description:
            - "Meta package name."
        required: true
        type: str

    recommends:
        default: []
        description:
            - "Declares a strong, but not absolute, dependency. The I(recommends) field should list packages
               that would be found together with this one in all but unusual installations. If the functionality should
               be available by default for users, I(recommends) should be used, and I(suggests) otherwise."
        type: list

    state:
        choices: [present, absent]
        default: present
        description:
            - "Indicates the desired package state."
        type: str

    suggests:
        default: []
        description:
            - "Declare that one package may be more useful with one or more others. Using this field tells the packaging
               system and the user that the listed packages are related to this one and can perhaps enhance its
               usefulness, but that installing this one without them is perfectly reasonable. If the functionality
               should be available by default for users, I(recommends) should be used, and I(suggests) otherwise."
        type: list

    summary:
        aliases: [ synopsis ]
        default: "Meta package to simplify package management"
        description:
            - "A short and concise description of the package. The I(description) expands upon this."
        type: str

    version:
        default: "1"
        description:
            - "Meta package version."
        type: str

notes:
  - "If a package with the same name and version is installed already then this module exists without applying any
     changes to the system."
  - "Prior to installing a meta package on apt (deb) based distributions, one might use M(apt) to update the package
     cache and hence avoid unsatisfied dependency errors."
  - "If I(state) is C(absent), any package with the given name is removed, regardless of the version and whether or not
     its a meta package."
  - "If I(state) is C(absent) and I(manager) evaluates to C(apt), then this module will act as module M(apt), i.e. it
     will remove I(name) but will not purge its configuration files."
  - "If I(state) is C(absent) and I(manager) evaluates to C(dnf), then the package removal is done using the autoremove
     feature. This removes all 'leaf' packages from the system that were originally installed as dependencies of user-
     installed packages but which are no longer required by any such package. If this behavior is not wanted, one may
     use module M(dnf) instead of M(jm1.pkg.meta_pkg)."
  - "Wildcards can be used for I(depends), I(recommends), I(suggests), I(enhances) and I(conflicts) options. But beware:
     Wildcards will be resolved on the ansible host where this module is executed, hence only packages known to the
     package manager on that host will be matched."
  - "Guides about package relationships I(depends), I(recommends), I(suggests), I(enhances) and I(conflicts):
     * Debian:
         U(https://www.debian.org/doc/debian-policy/ch-relationships.html)
     * Fedora:
         U(https://docs.fedoraproject.org/en-US/packaging-guidelines/)
         U(https://docs.fedoraproject.org/en-US/packaging-guidelines/WeakDependencies/)"
  - "Debian, Ubuntu and their derivatives do not provide any field in *.deb packages that is equivalent to Fedora's
     'Supplements:' field in in *.rpm packages."

author: "Jakob Meng (@jm1)"
'''

EXAMPLES = r'''
- jm1.pkg.meta_pkg:
    name: "developer-tools"
    depends:
    - make
    - gcc
    - git
    - vim
    conflicts:
    - clang
'''

RETURN = r'''
conflicts:
    description: List of conflicting packages after wildcard expansion
    returned: changed or success
    type: list
    sample: [ 'clang' ]

depends:
    description: List of required packages after wildcard expansion
    returned: changed or success
    type: list
    sample: [ 'make', 'gcc', 'git', 'vim' ]

enhances:
    description: List of enhanced packages after wildcard expansion
    returned: changed or success
    type: list
    sample: []

maintainer:
    description: The package maintainer’s name and email address
    returned: changed or success
    type: str
    sample: 'Jakob Meng <jakobmeng@web.de'

manager:
    description: The package manager that is used effectively
    returned: changed or success
    type: str
    sample: 'apt'

recommends:
    description: List of recommended packages after wildcard expansion
    returned: changed or success
    type: list
    sample: []

suggests:
    description: List of suggested packages after wildcard expansion
    returned: changed or success
    type: list
    sample: []
'''

# NOTE: Synchronize imports with DOCUMENTATION string above
from ansible.module_utils._text import to_native
from ansible.module_utils.basic import AnsibleModule, missing_required_lib
from ansible.module_utils.common.dict_transformations import dict_merge
from ansible.module_utils.facts import ansible_collector
from ansible.module_utils.facts import default_collectors
from ansible.module_utils.facts.namespace import PrefixFactNamespace
import ansible.module_utils.six as six
import datetime
import jinja2
import os
import pwd
import re
import socket
import traceback

try:
    import apt
except ImportError:
    APT_IMPORT_ERROR = traceback.format_exc()
    HAS_APT = False
else:
    APT_IMPORT_ERROR = None
    HAS_APT = True

try:
    import dnf
except ImportError:
    DNF_IMPORT_ERROR = traceback.format_exc()
    HAS_DNF = False
else:
    DNF_IMPORT_ERROR = None
    HAS_DNF = True

try:
    import yum  # is Python 2 only
except ImportError:
    YUM_IMPORT_ERROR = traceback.format_exc()
    HAS_YUM = False
else:
    YUM_IMPORT_ERROR = None
    HAS_YUM = True


if six.PY2:
    try:
        from backports import tempfile
    except ImportError:
        BACKPORTS_TEMPFILE_IMPORT_ERROR = traceback.format_exc()
        HAS_BACKPORTS_TEMPFILE = False
    else:
        BACKPORTS_TEMPFILE_IMPORT_ERROR = None
        HAS_BACKPORTS_TEMPFILE = True
elif six.PY3:
    import tempfile


DEBIAN_CONTROLFILE_TEMPLATE = r'''
Section: metapackages
Priority: optional
Standards-Version:  4.5.0
Package: {{ name }}
Version: {{ version }}
Architecture: {{ architecture }}
Maintainer: {{ maintainer }}

Conflicts: {{ conflicts|join(', ') }}
Depends: {{ depends|join(', ') }}
Enhances: {{ enhances|join(', ') }}
Recommends: {{ recommends|join(', ') }}
Suggests: {{ suggests|join(', ') }}

Description: {{ summary }}
 {{ description|wordwrap(width=80)|indent(1) }}

'''

RPM_SPEC_TEMPLATE = r'''
{% if summary %}
Summary: {{ summary }}
{% endif %}

Name: {{ name }}
Version: {{ version }}
Release: 1%{dist}
License: GPL
BuildArch: {{ architecture }}

{% if conflicts %}
Conflicts: {{ conflicts|join(', ') }}
{% endif %}

{% if enhances %}
Enhances: {{ enhances|join(', ') }}
{% endif %}

{% if recommends %}
Recommends: {{ recommends|join(', ') }}
{% endif %}

{% if depends %}
Requires: {{ depends|join(', ') }}
{% endif %}

{% if suggests %}
Suggests:  {{ suggests|join(', ') }}
{% endif %}

{% if description %}
%description
{{ description|wordwrap(width=80) }}
{% endif %}

%prep
%setup -c -T

%build

%install

%files

%changelog
* {{ now().strftime('%a %b %-d %Y') }} {{ maintainer }} {{ version }}
- Initial RPM release

'''

ENV_VARS = dict(
    # We screenscrape apt-get, yum and dnf output for information so
    # we need to make sure we use the C locale when running commands
    LANG='C',
    LC_ALL='C',
    LC_MESSAGES='C',
    LC_CTYPE='C',
)

APT_ENV_VARS = dict(
    DEBIAN_FRONTEND='noninteractive',
    DEBIAN_PRIORITY='critical',
)


def apt_package_status(name, cache):
    is_installed = False
    is_virtual = False
    installed_pkg = None

    try:
        pkg = cache[name]
    except KeyError:
        is_installed = False
        is_virtual = cache.is_virtual_package(name)
        installed_pkg = None
        return is_installed, is_virtual, installed_pkg

    is_installed = True
    is_virtual = False
    installed_pkg = pkg.installed
    return is_installed, is_virtual, installed_pkg


def as_re_fullmatch(regex):
    """
    Emulate python-3.4 re.fullmatch().
    Ref.: https://stackoverflow.com/a/30212799/6490710
    """
    return "(?:" + regex + r")\Z"


def match(patterns, strings):
    matched = []

    for pattern in patterns:
        # decide between just-a-package-name vs. regex pattern by searching for disallowed characters
        # Ref.: https://lists.debian.org/debian-dpkg/2006/05/msg00087.html
        is_not_regex = re.compile(as_re_fullmatch(r'^[0-9a-zA-Z\.\+\_\-]*$')).match(pattern)

        if is_not_regex:
            # just a package name
            matched.append(pattern)
        else:
            # regex pattern
            regex = re.compile(as_re_fullmatch(pattern))
            for string in strings:
                if regex.match(string):
                    matched.append(string)

    return set(matched)


def make_rpm(architecture,
             conflicts,
             cwd,
             depends,
             description,
             enhances,
             maintainer,
             manager,
             name,
             recommends,
             suggests,
             summary,
             version,
             module):
    spec_path = os.path.join(cwd, '%s.spec' % name)
    spec_template = jinja2.Template(RPM_SPEC_TEMPLATE)
    spec_template.globals['now'] = datetime.datetime.utcnow
    spec_content = spec_template.render(
        architecture=architecture,
        conflicts=conflicts,
        depends=depends,
        description=description,
        enhances=enhances,
        maintainer=maintainer,
        name=name,
        recommends=recommends,
        suggests=suggests,
        summary=summary,
        version=version)

    with open(spec_path, 'w') as f:
        f.write(spec_content)

    cmd = "rpmbuild --define '_topdir {topdir}' -ba '{spec_path}'".format(
        topdir=cwd, spec_path=spec_path)
    module.run_command(cmd, check_rc=True, cwd=cwd, environ_update=ENV_VARS)

    cmd = "sh -c '/usr/lib/rpm/redhat/dist.sh --dist'"
    rc, stdout, stderr = module.run_command(cmd, check_rc=True, cwd=cwd, environ_update=ENV_VARS)
    dist = stdout

    pkg_filename = 'RPMS/{architecture}/{name}-{version}-1{dist}.{architecture}.rpm'.format(
        dist=dist, name=name, version=version, architecture=architecture)

    pkg_path = os.path.join(cwd, pkg_filename)

    return pkg_path


def install(architecture,
            conflicts,
            depends,
            description,
            enhances,
            maintainer,
            manager,
            name,
            recommends,
            suggests,
            summary,
            version,
            module):

    if manager == 'apt':
        pkg_names = []
        with apt.Cache() as cache:
            is_installed, is_virtual, installed_pkg = apt_package_status(name, cache)

            if is_installed and version == installed_pkg.version:
                # package is present already
                return False, conflicts, depends, enhances, recommends, suggests

            # TODO: Replace with 'apt-cache pkgnames' if not HAS_APT?
            pkg_names = cache.keys()

        conflicts = sorted(match(conflicts, pkg_names))
        depends = sorted(match(depends, pkg_names))
        enhances = sorted(match(enhances, pkg_names))
        recommends = sorted(match(recommends, pkg_names))
        suggests = sorted(match(suggests, pkg_names))

        with tempfile.TemporaryDirectory() as dir:
            control_path = os.path.join(dir, 'package.ctl')
            control_template = jinja2.Template(DEBIAN_CONTROLFILE_TEMPLATE)
            control_content = control_template.render(
                architecture=architecture,
                conflicts=conflicts,
                depends=depends,
                description=description,
                enhances=enhances,
                maintainer=maintainer,
                name=name,
                recommends=recommends,
                suggests=suggests,
                summary=summary,
                version=version)

            with open(control_path, 'w') as f:
                f.write(control_content)

            cmd = "equivs-build '{control_path}'".format(control_path=control_path)
            module.run_command(cmd, check_rc=True, cwd=dir, environ_update=dict_merge(ENV_VARS, APT_ENV_VARS))

            # Even though equivs-build pretends that 'the package has been created in the current directory,
            # not in ".." as indicated by the message above!", it might create the package exactly there, e.g.
            # when equivs-build is run as root in Ansible. As a workaround we move the package if required.

            pkg_filename = '{name}_{version}_{architecture}.deb'.format(
                name=name, version=version, architecture=architecture)

            module.debug('package filename: %s' % pkg_filename)

            pkg_path = os.path.join(dir, pkg_filename)

            if not os.path.isfile(pkg_path):
                wrong_pkg_path = os.path.join(os.path.join(dir, os.pardir), pkg_filename)
                module.atomic_move(wrong_pkg_path, pkg_path)

            cmd = "apt-get install -y '{pkg_path}'".format(pkg_path=pkg_path)
            module.run_command(cmd, check_rc=True, cwd=dir, environ_update=dict_merge(ENV_VARS, APT_ENV_VARS))

            return True, conflicts, depends, enhances, recommends, suggests

    elif manager == 'dnf':
        pkg_names = []
        with dnf.Base() as base:
            base.read_all_repos()
            base.fill_sack(load_system_repo=True, load_available_repos=False)
            q = base.sack.query()
            installed_pkgs = q.installed().filter(name=name, version=version).run()
            if installed_pkgs:
                # package is present already
                return False, conflicts, depends, enhances, recommends, suggests

            base.reset(repos=True, sack=True)
            base.read_all_repos()
            base.fill_sack(load_system_repo=True, load_available_repos=True)
            q = base.sack.query()

            pkg_names = map(lambda pkg: pkg.name, q.available())
            pkg_names = sorted(set(pkg_names))

            conflicts = sorted(match(conflicts, pkg_names))
            depends = sorted(match(depends, pkg_names))
            enhances = sorted(match(enhances, pkg_names))
            recommends = sorted(match(recommends, pkg_names))
            suggests = sorted(match(suggests, pkg_names))

            with tempfile.TemporaryDirectory() as dir:
                pkg_path = make_rpm(
                    architecture,
                    conflicts,
                    dir,
                    depends,
                    description,
                    enhances,
                    maintainer,
                    manager,
                    name,
                    recommends,
                    suggests,
                    summary,
                    version,
                    module)

                # Install using dnf CLI
                #  cmd = "dnf install -y '{pkg_path}'".format(pkg_path=pkg_path)
                #  module.run_command(cmd, check_rc=True, cwd=dir, environ_update=ENV_VARS)

                # Install using dnf API
                pkgs = base.add_remote_rpms([pkg_path])
                for pkg in pkgs:
                    base.package_install(pkg)
                base.resolve()
                base.download_packages(base.transaction.install_set)
                base.do_transaction()

        return True, conflicts, depends, enhances, recommends, suggests

    elif manager == 'yum':
        yb = yum.YumBase()
        if yb.rpmdb.searchNevra(name=name, ver=version):
            # package is present already
            return False, conflicts, depends, enhances, recommends, suggests

        pkgs = yb.pkgSack.simplePkgList()
        pkg_names = map(lambda x: x[0], pkgs)  # x = (n, a, e, v, r)
        pkg_names = sorted(set(pkg_names))

        conflicts = sorted(match(conflicts, pkg_names))
        depends = sorted(match(depends, pkg_names))
        enhances = sorted(match(enhances, pkg_names))
        recommends = sorted(match(recommends, pkg_names))
        suggests = sorted(match(suggests, pkg_names))

        with tempfile.TemporaryDirectory() as dir:
            pkg_path = make_rpm(
                architecture,
                conflicts,
                dir,
                depends,
                description,
                enhances,
                maintainer,
                manager,
                name,
                recommends,
                suggests,
                summary,
                version,
                module)

            cmd = "yum install -y '{pkg_path}'".format(pkg_path=pkg_path)
            module.run_command(cmd, check_rc=True, cwd=dir, environ_update=ENV_VARS)

        return True, conflicts, depends, enhances, recommends, suggests

    # else manager not in [ 'apt', 'dnf', 'yum' ]
    return False, conflicts, depends, enhances, recommends, suggests


def remove(manager,
           name,
           module):

    if manager == 'apt':
        with apt.Cache() as cache:
            if name not in cache:
                # package is absent already
                return False

        cmd = "apt-get remove -y '{name}'".format(name=name)
        module.run_command(cmd, check_rc=True, environ_update=dict_merge(ENV_VARS, APT_ENV_VARS))
        return True

    elif manager == 'dnf':
        with dnf.Base() as base:
            base.read_all_repos()
            base.fill_sack(load_system_repo=True, load_available_repos=False)
            q = base.sack.query()
            if not q.installed().filter(name=name).run():
                # package is absend already
                return False

            # Removal using dnf CLI
            #  cmd = "dnf autoremove -y '{name}'".format(name=name)
            #  module.run_command(cmd, check_rc=True, environ_update=ENV_VARS)
            #  return True

            # Removal using dnf API
            base.conf.clean_requirements_on_remove = True
            base.remove(name)
            base.resolve(allow_erasing=True)
            base.do_transaction()

            return True

    elif manager == 'yum':
        yb = yum.YumBase()
        if not yb.rpmdb.searchNevra(name=name):
            # package is absent already
            return False

        cmd = "yum autoremove -y '{name}'".format(name=name)
        module.run_command(cmd, check_rc=True, environ_update=ENV_VARS)
        return True

    # else manager not in [ 'apt', 'dnf', 'yum' ]
    return False


def core(module):
    architecture = module.params['architecture']
    conflicts = module.params['conflicts']
    depends = module.params['depends']
    description = module.params['description']
    enhances = module.params['enhances']
    maintainer = module.params['maintainer']
    manager = module.params['manager']
    name = module.params['name']
    recommends = module.params['recommends']
    state = module.params['state']
    suggests = module.params['suggests']
    summary = module.params['summary']
    version = module.params['version']

    if not maintainer:
        pwuid = pwd.getpwuid(os.getuid())

        username = pwuid.pw_name

        if pwuid.pw_gecos:
            fullname = pwuid.pw_gecos.split(',')[0]
        else:
            # fallback to username
            fullname = username

        fqdn = socket.getfqdn()

        maintainer = '{fullname} <{username}@{fqdn}>'.format(fullname=fullname, username=username, fqdn=fqdn)

    if manager == 'auto':
        # Inspired by https://github.com/ansible/ansible/blob/devel/lib/ansible/modules/setup.py
        namespace = PrefixFactNamespace(namespace_name='ansible', prefix='ansible_')

        fact_collector = \
            ansible_collector.get_ansible_collector(all_collector_classes=default_collectors.collectors,
                                                    namespace=namespace,
                                                    filter_spec='*',
                                                    gather_subset=['pkg_mgr'],
                                                    minimal_gather_subset=frozenset(['pkg_mgr']))

        facts_dict = fact_collector.collect(module=module)
        manager = facts_dict['ansible_pkg_mgr']

    if manager not in ['apt', 'dnf', 'yum']:
        raise ValueError('manager %s is not supported' % manager)

    if manager == 'apt' and not HAS_APT:
        module.fail_json(msg=missing_required_lib("apt"), exception=APT_IMPORT_ERROR)

    if manager == 'dnf' and not HAS_DNF:
        module.fail_json(msg=missing_required_lib("dnf"), exception=DNF_IMPORT_ERROR)

    if manager == 'yum' and not HAS_YUM:
        module.fail_json(msg=missing_required_lib("yum"), exception=YUM_IMPORT_ERROR)

    if not architecture:
        if manager == 'apt':
            architecture = 'all'
        elif manager in ['yum', 'dnf']:
            architecture = 'noarch'

    if module.check_mode:
        return dict(
            changed=False,
            architecture=architecture,
            conflicts=conflicts,
            depends=depends,
            description=description,
            enhances=enhances,
            maintainer=maintainer,
            manager=manager,
            name=name,
            recommends=recommends,
            state=state,
            suggests=suggests,
            summary=summary,
            version=version)

    if state == 'present':
        changed, conflicts, depends, enhances, recommends, suggests = install(
            architecture,
            conflicts,
            depends,
            description,
            enhances,
            maintainer,
            manager,
            name,
            recommends,
            suggests,
            summary,
            version,
            module)
    elif state == 'absent':
        changed = remove(
            manager,
            name,
            module)

    return dict(
        changed=changed,
        architecture=architecture,
        conflicts=conflicts,
        depends=depends,
        description=description,
        enhances=enhances,
        maintainer=maintainer,
        manager=manager,
        name=name,
        recommends=recommends,
        state=state,
        suggests=suggests,
        summary=summary,
        version=version)


def main():
    module = AnsibleModule(
        argument_spec=dict(
            architecture=dict(type='str', aliases=['buildarch']),
            conflicts=dict(type='list', default=[]),
            depends=dict(type='list', default=[]),
            description=dict(type='str', default='Package management made easy.'),
            enhances=dict(type='list', default=[]),
            maintainer=dict(type='str', aliases=['packager']),
            manager=dict(type='str', choices=['auto', 'apt', 'dnf', 'yum'], default='auto'),
            name=dict(required=True, type='str'),
            recommends=dict(type='list', default=[]),
            state=dict(type='str', choices=['present', 'absent'], default='present'),
            suggests=dict(type='list', default=[]),
            summary=dict(type='str', aliases=['synopsis'], default='Meta package to simplify package management'),
            version=dict(type='str', default='1')
        ),
        supports_check_mode=True,
    )

    if not HAS_APT or not HAS_DNF or not HAS_YUM:
        pass  # errors handled in def core()

    if six.PY2 and not HAS_BACKPORTS_TEMPFILE:
        module.fail_json(msg=missing_required_lib("backports.tempfile"), exception=BACKPORTS_TEMPFILE_IMPORT_ERROR)
    try:
        result = core(module)
    except Exception as e:
        module.fail_json(msg=to_native(e), exception=traceback.format_exc())
    else:
        module.exit_json(**result)


if __name__ == '__main__':
    main()

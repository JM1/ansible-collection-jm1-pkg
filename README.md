# Ansible Collection for Software Packaging and Deployment

This repo hosts the [`jm1.pkg`](https://galaxy.ansible.com/jm1/pkg) Ansible Collection.

The collection includes a variety of Ansible content to help with packaging and deployment of software.

For example, Ansible module [`jm1.pkg.meta_pkg`](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/plugins/modules/meta_pkg.py)
simplifies the build, installation and removal of meta packages using the OS package manager, such as `apt`, `yum` or
`dnf`. A meta package does not include any files, it rather defines [relationships](https://www.debian.org/doc/debian-policy/ch-relationships.html)
between packages only, e.g. dependencies or conflicts. When a meta package is installed, the OS package manager will
install or remove packages automatically to satisfy all relationships declared by the meta package. This helps to keep
your system clean e.g. when packages should be removed during upgrades or updates to Ansible playbooks: Previously
installed packages which are removed from the meta package dependencies, will be uninstalled automatically by the OS
package manager once the new meta package version is rolled out.

For example:

1. We start our coding career with Subversion:
    ```yaml
    - hosts: all
      tasks:
        - name: Install software required by jm1.pkg's roles and modules
          import_role:
            name: jm1.pkg.setup

        - name: Install C development tools
          jm1.pkg.meta_pkg:
            name: developer-tools
            version: '1'
            depends:
            - make
            - gcc
            - subversion
            - vim
    ```

2. Later we want to switch from Subversion to Git:
    ```yaml
    - hosts: all
      tasks:
        - name: Install software required by jm1.pkg's roles and modules
          import_role:
            name: jm1.pkg.setup

        - name: Install C development tools
          jm1.pkg.meta_pkg:
            name: developer-tools
            version: '2'
            depends:
            - make
            - gcc
            - git
            - vim
    ```

When the second release of `developer-tools` is installed, the OS package manager might [`autoremove`](https://dnf.readthedocs.io/en/latest/command_ref.html#autoremove-command-label)
`subversion` if no other package depends on it anymore.

## Included content

Click on the name of a module or role to view that content's documentation:

- **Modules**:
    * [meta_pkg](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/plugins/modules/meta_pkg.py)
- **Roles**:
    * [apt_repository](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/roles/apt_repository/README.md)
    * [apt_sources_list_removal](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/roles/apt_sources_list_removal/README.md)
    * [setup](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/roles/setup/README.md)
    * [yum_repository](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/roles/yum_repository/README.md)

## Requirements and Installation

### Installing necessary software

Content in this collection requires additional roles and collections, e.g. to collect operating system facts. You can
fetch them from Ansible Galaxy using the provided [`requirements.yml`](requirements.yml):

```sh
ansible-galaxy collection install --requirements-file requirements.yml
ansible-galaxy role install --role-file requirements.yml
# or
make install-requirements
```

Content in this collection requires additional tools and libraries, e.g. to interact with apt's, yum's and dnf's APIs.
You can use role [`jm1.pkg.setup`](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/roles/setup/README.md) to
install necessary software packages:

```yaml
- hosts: all
  roles:
    - jm1.pkg.setup
```

Or to install these packages locally:

```sh
sudo -s

ansible-console localhost << EOF
gather_facts
include_role name=jm1.pkg.setup
EOF
```

The exact requirements for every module and role are listed in the corresponding documentation.
See the module documentations for the minimal version supported for each module.

### Installing the Collection from Ansible Galaxy

Before using the `jm1.pkg` collection, you need to install it with the Ansible Galaxy CLI:

```sh
ansible-galaxy collection install jm1.pkg
```

You can also include it in a `requirements.yml` file and install it via
`ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: jm1.pkg
    version: 2022.9.25
```

## Usage and Playbooks

You can either call modules by their Fully Qualified Collection Namespace (FQCN), like `jm1.pkg.meta_pkg`, or you
can call modules by their short name if you list the `jm1.pkg` collection in the playbook's `collections`,
like so:

```yaml
---
- name: Using jm1.pkg collection
  hosts: localhost

  collections:
    - jm1.pkg

  tasks:
    - name: Satisfy software requirements
      import_role:
        name: setup

    - name: Create and install a new meta package
      meta_pkg:
        name: "developer-tools"
        depends:
        - make
        - gcc
        - git
        - vim
```

For documentation on how to use individual modules and other content included in this collection, please see the links
in the 'Included content' section earlier in this README.

See [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more
details.

## Contributing

There are many ways in which you can participate in the project, for example:

- Submit bugs and feature requests, and help us verify them
- Submit pull requests for new modules, roles and other content

We're following the general Ansible contributor guidelines;
see [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html).

If you want to develop new content for this collection or improve what is already here, the easiest way to work on the
collection is to clone this repository (or a fork of it) into one of the configured [`ANSIBLE_COLLECTIONS_PATHS`](
https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths) and work on it there:
1. Create a directory `ansible_collections/jm1`;
2. In there, checkout this repository (or a fork) as `pkg`;
3. Add the directory containing `ansible_collections` to your
   [`ANSIBLE_COLLECTIONS_PATHS`](https://docs.ansible.com/ansible/latest/reference_appendices/config.html#collections-paths).

Helpful tools for developing collections are `ansible`, `ansible-doc`, `ansible-galaxy`, `ansible-lint`, `flake8`,
`make` and `yamllint`.

| OS                                           | Install Instructions                                                |
| -------------------------------------------- | ------------------------------------------------------------------- |
| Debian 10 (Buster)                           | Enable [Backports](https://backports.debian.org/Instructions/). `apt install ansible ansible-doc ansible-lint flake8 make yamllint` |
| Debian 11 (Bullseye)                         | `apt install ansible ansible-lint flake8 make yamllint` |
| Debian 12 (Bookworm)                         | `apt install ansible ansible-lint flake8 make yamllint` |
| Red Hat Enterprise Linux (RHEL) 7 / CentOS 7 | Enable [EPEL](https://fedoraproject.org/wiki/EPEL). `yum install ansible ansible-lint ansible-doc  python-flake8 make yamllint` |
| Red Hat Enterprise Linux (RHEL) 8 / CentOS 8 | Enable [EPEL](https://fedoraproject.org/wiki/EPEL). `yum install ansible                           python3-flake8 make yamllint` |
| Red Hat Enterprise Linux (RHEL) 9 / CentOS 9 | Enable [EPEL](https://fedoraproject.org/wiki/EPEL). `yum install ansible                           python3-flake8 make yamllint` |
| Ubuntu 18.04 LTS (Bionic Beaver)             | Enable [Launchpad PPA Ansible by Ansible, Inc.](https://launchpad.net/~ansible/+archive/ubuntu/ansible). `apt install ansible ansible-doc ansible-lint flake8 make yamllint` |
| Ubuntu 20.04 LTS (Focal Fossa)               | `apt install ansible ansible-doc ansible-lint flake8 make yamllint` |
| Ubuntu 22.04 LTS (Jammy Jellyfish)           | `apt install ansible             ansible-lint flake8 make yamllint` |

Have a look at the included [`Makefile`](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/Makefile) for
several frequently used commands, to e.g. build and lint a collection.

## More Information

- [Ansible Collection Overview](https://github.com/ansible-collections/overview)
- [Ansible User Guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## License

GNU General Public License v3.0 or later

See [LICENSE.md](LICENSE.md) to see the full text.

## Author

Jakob Meng
@jm1 ([github](https://github.com/jm1), [galaxy](https://galaxy.ansible.com/jm1), [web](http://www.jakobmeng.de))

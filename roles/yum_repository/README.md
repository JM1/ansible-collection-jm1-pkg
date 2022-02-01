# Ansible Role `jm1.pkg.yum_repository`

This role helps with managing [yum repositories][yum-repository-howto] from Ansible variables. Role variable
`yum_repository_config` defines a list of tasks which will be run by this role. Each task calls an Ansible module
similar to tasks in roles or playbooks except that [task keywords such as `name`, `notify` and `when`][
playbooks-keywords] are ignored. For example, to add the `Extra Packages for Enterprise Linux (EPEL)` repository on
CentOS 9 (Stream) define variable `yum_repository_config` in [`group_vars` or `host_vars`][ansible-inventory] as such:

```yml
yum_repository_config:
# Extra Packages for Enterprise Linux (EPEL)
# Ref.: https://docs.fedoraproject.org/en-US/epel/
- dnf:
    disable_gpg_check: yes
    name: 'https://dl.fedoraproject.org/pub/epel/epel-release-latest-{{ distribution_id|last }}.noarch.rpm'
- dnf:
    disable_gpg_check: yes
    name: 'https://dl.fedoraproject.org/pub/epel/epel-next-release-latest-{{ distribution_id|last }}.noarch.rpm'
```

[ansible-inventory]: https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html
[playbooks-keywords]: https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html
[yum-repository-howto]: https://www.redhat.com/sysadmin/add-yum-repository

**Tested OS images**
- Generic cloud image of [`CentOS 7 (Core)` \[`amd64`\]](https://cloud.centos.org/centos/7/images/)
- Generic cloud image of [`CentOS 8 (Core)` \[`amd64`\]](https://cloud.centos.org/centos/8/x86_64/images/)
- Generic cloud image of [`CentOS 9 (Stream)` \[`amd64`\]](https://cloud.centos.org/centos/9-stream/x86_64/images/)

Available on Ansible Galaxy in Collection [jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

## Requirements

This role uses module(s) from collection [`community.general`][galaxy-community-general]. To install this collection
you may follow the steps described in [`README.md`][jm1-pkg-readme] using the provided [`requirements.yml`][
jm1-pkg-requirements].

[galaxy-community-general]: https://galaxy.ansible.com/community/general
[jm1-pkg-readme]: https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/README.md
[jm1-pkg-requirements]: https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/requirements.yml

Python library `python-dnf` is required by Ansible's [`dnf`][ansible-module-dnf] module.

| OS                                           | Install Instructions      |
| -------------------------------------------- | ------------------------- |
| Red Hat Enterprise Linux (RHEL) 7 / CentOS 7 | Not applicable            |
| Red Hat Enterprise Linux (RHEL) 8 / CentOS 8 | `dnf install python3-dnf` |
| Red Hat Enterprise Linux (RHEL) 9 / CentOS 9 | `dnf install python3-dnf` |

## Variables

| Name                                               | Default value                      | Required | Description |
| -------------------------------------------------- | ---------------------------------- | -------- | ----------- |
| `distribution_id`                                  | *depends on operating system*      | no       | List which uniquely identifies a distribution release, e.g. `[ 'Debian', '10' ]` for `Debian 10 (Buster)` |
| `yum_repository_config`                            | `{{ yum_repository_config_epel }}` | no       | List of tasks to run [^supported-modules], e.g. to add yum repository definitions |
| `yum_repository_config_centos_7`                   | *refer to [`roles/yum_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `CentOS 7` |
| `yum_repository_config_centos_8`                   | *refer to [`roles/yum_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `CentOS 8` |
| `yum_repository_config_centos_9`                   | *refer to [`roles/yum_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `CentOS 9` |
| `yum_repository_config_epel`                       | *refer to [`roles/yum_repository/defaults/main.yml`](defaults/main.yml)* | no | List of tasks to add yum repository definitions of Extra Packages for Enterprise Linux (EPEL) for the distribution matching `distribution_id` and `distribution_release` |
| `yum_repository_config_red_hat_enterprise_linux_7` | *refer to [`roles/yum_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Red Hat Enterprise Linux (RHEL) 7` |
| `yum_repository_config_red_hat_enterprise_linux_8` | *refer to [`roles/yum_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Red Hat Enterprise Linux (RHEL) 8` |
| `yum_repository_config_red_hat_enterprise_linux_9` | *refer to [`roles/yum_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Red Hat Enterprise Linux (RHEL) 9` |

[^supported-modules]: Supported Ansible modules are [`blockinfile`][ansible-module-blockinfile], [`dnf`][
ansible-module-dnf], [`copy`][ansible-module-copy], [`file`][ansible-module-file], [`ini_file`][
ansible-module-ini-file], [`lineinfile`][ansible-module-lineinfile], [`template`][ansible-module-template], [`yum`][
ansible-module-yum] and [`yum_repository`][ansible-module-yum-repository],

[ansible-module-blockinfile]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/blockinfile_module.html
[ansible-module-dnf]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/dnf_module.html
[ansible-module-copy]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html
[ansible-module-file]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html
[ansible-module-lineinfile]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/lineinfile_module.html
[ansible-module-template]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html
[ansible-module-yum]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_module.html
[ansible-module-yum-repository]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_repository_module.html

## Dependencies

None.

## Example Playbook

```yml
- hosts: all
  become: yes
  vars:
    # Variables are listed here for convenience and illustration.
    # In a production setup, variables would be defined e.g. in
    # group_vars and/or host_vars of an Ansible inventory.
    # Ref.:
    # https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html
    # https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html
    yum_repository_config: '{{ yum_repository_config_centos_9.epel + yum_repository_config_centos_9.epel_next }}'

  roles:
  - name: Manage YUM repositories
    role: jm1.pkg.yum_repository
    tags: ["jm1.pkg.yum_repository"]
```

For instructions on how to run Ansible playbooks have look at Ansible's
[Getting Started Guide](https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html).

## License

GNU General Public License v3.0 or later

See [LICENSE.md](../../LICENSE.md) to see the full text.

## Author

Jakob Meng
@jm1 ([github](https://github.com/jm1), [galaxy](https://galaxy.ansible.com/jm1), [web](http://www.jakobmeng.de))

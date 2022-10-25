# Ansible Role `jm1.pkg.apt_repository`

This role helps with managing [apt repositories][apt-sources-list] and [apt keys][apt-keys-migration] from Ansible
variables. Role variable `apt_repository_config` defines a list of tasks which will be run by this role. Each task calls
an Ansible module similar to tasks in roles or playbooks except that only few [keywords][playbooks-keywords] such as
`register` and `when` are supported. For example, to add apt keys and apt repositories for Debian 11 (Bullseye) define
variable `apt_repository_config` in [`group_vars` or `host_vars`][ansible-inventory] as such:

```yml
apt_repository_config:
#
# archive keyring
# Ref.: https://packages.debian.org/bullseye/debian-archive-keyring
- ansible.builtin.apt_key:
    # bullseye_stable
    id: 605C66F00D6C9793
    url: https://ftp-master.debian.org/keys/release-11.asc
    keyring: /etc/apt/trusted.gpg.d/debian-archive-bullseye-stable.gpg
- ansible.builtin.apt_key:
    # bullseye_security_automatic
    id: A48449044AAD5C5D
    url: https://ftp-master.debian.org/keys/archive-key-11-security.asc
    keyring: /etc/apt/trusted.gpg.d/debian-archive-bullseye-security-automatic.gpg
- ansible.builtin.apt_key:
    # bullseye_automatic
    id: 73A4F27B8DD47936
    url: https://ftp-master.debian.org/keys/archive-key-11.asc
    keyring: /etc/apt/trusted.gpg.d/debian-archive-bullseye-automatic.gpg
#
# data sources
- ansible.builtin.apt_repository:
    # bullseye
    repo: deb http://deb.debian.org/debian bullseye main contrib non-free
    filename: debian-bullseye
- ansible.builtin.apt_repository:
    # bullseye updates
    repo: deb http://deb.debian.org/debian bullseye-updates main contrib non-free
    filename: debian-bullseye-updates
- ansible.builtin.apt_repository:
    # bullseye security
    repo: deb http://deb.debian.org/debian-security/ bullseye-security main contrib non-free
    filename: debian-bullseye-security
```

[ansible-inventory]: https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html
[apt-keys-migration]: https://blog.jak-linux.org/2021/06/20/migrating-away-apt-key/
[apt-sources-list]: https://manpages.debian.org/stable/apt/sources.list.5.en.html
[playbooks-keywords]: https://docs.ansible.com/ansible/latest/reference_appendices/playbooks_keywords.html

**Tested OS images**
- [Cloud images](https://cdimage.debian.org/images/cloud/buster/daily/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 10 (Buster)` \[`amd64`\]
- [Cloud image](https://cdimage.debian.org/images/cloud/bullseye/daily/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 11 (Bullseye)` \[`amd64`\]
- [Cloud image](https://cdimage.debian.org/images/cloud/bookworm/daily/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 12 (Bookworm)` \[`amd64`\]
- Ubuntu cloud image of [`Ubuntu 18.04 LTS (Bionic Beaver)` \[`amd64`\]](https://cloud-images.ubuntu.com/bionic/current/)
- Ubuntu cloud image of [`Ubuntu 20.04 LTS (Focal Fossa)` \[`amd64`\]](https://cloud-images.ubuntu.com/focal/)
- Ubuntu cloud image of [`Ubuntu 22.04 LTS (Jammy Jellyfish)` \[`amd64`\]](https://cloud-images.ubuntu.com/jammy/)

Available on Ansible Galaxy in Collection [jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

## Requirements

Ansible module `jm1.ansible.execute_module` from Collection [`jm1.ansible`][galaxy-jm1-ansible] is used to run tasks
defined in variable `apt_repository_config`. To install `jm1.ansible.execute_module` you may follow the steps described
in [`README.md`][jm1-pkg-readme] using the provided [`requirements.yml`][jm1-pkg-requirements].

[galaxy-jm1-ansible]: https://galaxy.ansible.com/jm1/ansible
[jm1-cloudy-readme]: ../../README.md
[jm1-cloudy-requirements]: ../../requirements.yml

Tool `gpg` is required by Ansible's [`apt_key`][ansible-builtin-apt-key] module.

| OS                                           | Install Instructions |
| -------------------------------------------- | -------------------- |
| Debian 10 (Buster)                           | `apt install gnupg`  |
| Debian 11 (Bullseye)                         | `apt install gnupg`  |
| Debian 12 (Bookworm)                         | `apt install gnupg`  |
| Ubuntu 18.04 LTS (Bionic Beaver)             | `apt install gnupg`  |
| Ubuntu 20.04 LTS (Focal Fossa)               | `apt install gnupg`  |
| Ubuntu 22.04 LTS (Jammy Jellyfish)           | `apt install gnupg`  |

Python library `python-apt` is required by Ansible's [`apt_repository`][ansible-builtin-apt-repository] module.

| OS                                           | Install Instructions                 |
| -------------------------------------------- | ------------------------------------ |
| Debian 10 (Buster)                           | `apt install python-apt python3-apt` |
| Debian 11 (Bullseye)                         | `apt install python3-apt`            |
| Debian 12 (Bookworm)                         | `apt install python3-apt`            |
| Ubuntu 18.04 LTS (Bionic Beaver)             | `apt install python-apt python3-apt` |
| Ubuntu 20.04 LTS (Focal Fossa)               | `apt install python3-apt`            |
| Ubuntu 22.04 LTS (Jammy Jellyfish)           | `apt install python3-apt`            |

## Variables

| Name                                 | Default value                  | Required | Description |
| ------------------------------------ | ------------------------------ | -------- | ----------- |
| `apt_repository_config`              | *refer to [`roles/apt_repository/defaults/main.yml`](defaults/main.yml)* | no | List of tasks to run [^example-modules] [^supported-keywords] [^supported-modules], e.g. to add apt data sources or apt keys |
| `apt_repository_config_debian_9`     | *refer to [`roles/apt_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Debian 9 (Stretch)` |
| `apt_repository_config_debian_10`    | *refer to [`roles/apt_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Debian 10 (Buster)` |
| `apt_repository_config_debian_11`    | *refer to [`roles/apt_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Debian 11 (Bullseye)` |
| `apt_repository_config_debian_12`    | *refer to [`roles/apt_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Debian 12 (Bookworm)` |
| `apt_repository_config_ubuntu_18_04` | *refer to [`roles/apt_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Ubuntu 18.04 LTS (Bionic Beaver)` |
| `apt_repository_config_ubuntu_20_04` | *refer to [`roles/apt_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Ubuntu 20.04 LTS (Focal Fossa)` |
| `apt_repository_config_ubuntu_22_04` | *refer to [`roles/apt_repository/defaults/main.yml`](defaults/main.yml)* | no | apt data sources and keys for `Ubuntu 22.04 LTS (Jammy Jellyfish)` |
| `distribution_id`                    | *depends on operating system*  | no       | List which uniquely identifies a distribution release, e.g. `[ 'Debian', '10' ]` for `Debian 10 (Buster)` |

[^supported-modules]: Tasks will be executed with [`jm1.ansible.execute_module`][jm1-ansible-execute-module] which
supports modules and action plugins only. Some Ansible modules such as [`ansible.builtin.meta`][ansible-builtin-meta]
and `ansible.builtin.{include,import}_{playbook,role,tasks}` are core features of Ansible, in fact not implemented as
modules and thus cannot be called from `jm1.ansible.execute_module`. Doing so causes Ansible to raise errors such as
`MODULE FAILURE\nSee stdout/stderr for the exact error`. In addition, Ansible does not support free-form parameters
for arbitrary modules, so for example, change from `- debug: msg=""` to `- debug: { msg: "" }`.

[^supported-keywords]: Tasks will be executed with [`jm1.ansible.execute_module`][jm1-ansible-execute-module] which
supports keywords `register` and `when` only.

[^example-modules]: Useful Ansible modules in this context could be [`apt_key`][ansible-builtin-apt-key],
[`apt_repository`][ansible-builtin-apt-repository], [`blockinfile`][ansible-builtin-blockinfile], [`copy`][
ansible-builtin-copy], [`file`][ansible-builtin-file], [`lineinfile`][ansible-builtin-lineinfile] and
[`template`][ansible-builtin-template].

[ansible-builtin-apt-key]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_key_module.html
[ansible-builtin-apt-repository]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/apt_repository_module.html
[ansible-builtin-blockinfile]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/blockinfile_module.html
[ansible-builtin-copy]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html
[ansible-builtin-file]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/file_module.html
[ansible-builtin-lineinfile]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/lineinfile_module.html
[ansible-builtin-meta]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/meta_module.html
[ansible-builtin-template]: https://docs.ansible.com/ansible/latest/collections/ansible/builtin/template_module.html
[jm1-ansible-execute-module]: https://github.com/JM1/ansible-collection-jm1-ansible/blob/master/plugins/modules/execute_module.py

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
    apt_repository_config: |
      {{
        apt_repository_config_debian_11.keyring +
        apt_repository_config_debian_11.bullseye.deb +
        apt_repository_config_debian_11.bullseye_security.deb +
        apt_repository_config_debian_11.bullseye_updates.deb
      }}

  roles:
  # Remove /etc/apt/sources.list before apt repositories will be added to /etc/apt/sources.list.d/ by role
  # jm1.pkg.apt_repository else Ansible's apt_repository module might skip repositories if they are present in
  # /etc/apt/sources.list.
  - name: Remove /etc/apt/sources.list
    role: jm1.pkg.apt_sources_list_removal
    tags: ["jm1.pkg.apt_sources_list_removal"]

  - name: Manage apt keys and apt repositories
    role: jm1.pkg.apt_repository
    tags: ["jm1.pkg.apt_repository"]
```

For instructions on how to run Ansible playbooks have look at Ansible's
[Getting Started Guide](https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html).

## License

GNU General Public License v3.0 or later

See [LICENSE.md](../../LICENSE.md) to see the full text.

## Author

Jakob Meng
@jm1 ([github](https://github.com/jm1), [galaxy](https://galaxy.ansible.com/jm1), [web](http://www.jakobmeng.de))

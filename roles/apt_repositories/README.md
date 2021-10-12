# Ansible Role `jm1.pkg.apt_repositories`

This role helps to manage [apt repositories](https://manpages.debian.org/stable/apt/sources.list.5.en.html). It allows
to add or remove apt repositories in variable `apt_repositories` as a list where each list item is a dictionary of
parameters that will be passed to Ansible's
[`apt_repository`](https://docs.ansible.com/ansible/latest/modules/apt_repository_module.html) module.

**Tested OS images**
- [Cloud images](https://cdimage.debian.org/cdimage/openstack/current/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 10 (Buster)` \[`amd64`\]
- [Cloud image](https://cdimage.debian.org/images/cloud/bullseye/latest/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 11 (Bullseye)` \[`amd64`\]
- Ubuntu cloud image of [`Ubuntu 18.04 LTS (Bionic Beaver)` \[`amd64`\]](https://cloud-images.ubuntu.com/bionic/current/)
- Ubuntu cloud image of [`Ubuntu 20.04 LTS (Focal Fossa)` \[`amd64`\]](https://cloud-images.ubuntu.com/focal/)

Available on Ansible Galaxy in Collection [jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

## Requirements

Python library `python-apt` is required by Ansible's
[`apt_repository`](https://docs.ansible.com/ansible/latest/modules/apt_repository_module.html) module.

| OS                                           | Install Instructions                 |
| -------------------------------------------- | ------------------------------------ |
| Debian 10 (Buster)                           | `apt install python-apt python3-apt` |
| Debian 11 (Bullseye)                         | `apt install python3-apt`            |
| Ubuntu 18.04 LTS (Bionic Beaver)             | `apt install python-apt python3-apt` |
| Ubuntu 20.04 LTS (Focal Fossa)               | `apt install python3-apt`            |

## Variables

| Name               | Default value                           | Required | Description                                                                                               |
| ------------------ | --------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `apt_repositories` | *depends on `distribution_id` variable* | no       | List of parameter dictionaries for Ansible's `apt_repository` module                                      |
| `distribution_id`  | *depends on operating system*           | no       | List which uniquely identifies a distribution release, e.g. `[ 'Debian', '10' ]` for `Debian 10 (Buster)` |

## Dependencies

None.

## Example Playbook

```yml
- hosts: all
  vars:
    # Variables are listed here for convenience and illustration.
    # In a production setup, variables would be defined e.g. in
    # group_vars and/or host_vars of an Ansible inventory.
    # Ref.:
    # https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html
    # https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html
    apt_repositories:
    - # buster
      repo: deb http://deb.debian.org/debian buster main contrib non-free
      filename: debian-buster
    - # buster updates
      repo: deb http://deb.debian.org/debian buster-updates main contrib non-free
      filename: debian-buster-updates
    - # buster proposed updates:
      repo: deb http://deb.debian.org/debian buster-proposed-updates main contrib non-free
      filename: debian-buster-proposed-updates
    - # buster security
      repo: deb http://deb.debian.org/debian-security/ buster/updates main contrib non-free
      filename: debian-buster-security

  roles:
  # Remove /etc/apt/sources.list before apt repositories will be added to /etc/apt/sources.list.d/ by role
  # jm1.pkg.apt_repositories else Ansible's apt_repository module might skip repositories if they are present in
  # /etc/apt/sources.list.
  - name: Remove /etc/apt/sources.list
    role: jm1.pkg.apt_sources_list_removal
    tags: ["jm1.pkg.apt_sources_list_removal"]

  - name: Manage apt repositories
    role: jm1.pkg.apt_repositories
    tags: ["jm1.pkg.apt_repositories"]
```

For instructions on how to run Ansible playbooks have look at Ansible's
[Getting Started Guide](https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html).

## License

GNU General Public License v3.0 or later

See [LICENSE.md](../../LICENSE.md) to see the full text.

## Author

Jakob Meng
@jm1 ([github](https://github.com/jm1), [galaxy](https://galaxy.ansible.com/jm1), [web](http://www.jakobmeng.de))

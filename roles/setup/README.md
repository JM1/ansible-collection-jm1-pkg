# Ansible Role `jm1.pkg.setup`

This role helps to install necessary tools and libraries for all roles and modules in collection
[jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

**NOTE:** This role will *not* fetch and install any Ansible role or collection, because Ansible preloads all modules,
roles and tasks etc. before it executes any of them. Please make sure that all necessary roles and collections are
installed before running Ansible. To do so, you may follow the steps described in [`README.md`](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/README.md)
using the provided [`requirements.yml`](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/requirements.yml).

**Tested OS images**
- Cloud image of [`Debian 10 (Buster)` \[`amd64`\]](https://cdimage.debian.org/images/cloud/buster/daily/)
- Cloud image of [`Debian 11 (Bullseye)` \[`amd64`\]](https://cdimage.debian.org/images/cloud/bullseye/daily/)
- Cloud image of [`Debian 12 (Bookworm)` \[`amd64`\]](https://cdimage.debian.org/images/cloud/bookworm/daily/)
- Generic cloud image of [`CentOS 7 (Core)` \[`amd64`\]](https://cloud.centos.org/centos/7/images/)
- Generic cloud image of [`CentOS 8 (Core)` \[`amd64`\]](https://cloud.centos.org/centos/8/x86_64/images/)
- Generic cloud image of [`CentOS 9 (Stream)` \[`amd64`\]](https://cloud.centos.org/centos/9-stream/x86_64/images/)
- Ubuntu cloud image of [`Ubuntu 18.04 LTS (Bionic Beaver)` \[`amd64`\]](https://cloud-images.ubuntu.com/bionic/current/)
- Ubuntu cloud image of [`Ubuntu 20.04 LTS (Focal Fossa)` \[`amd64`\]](https://cloud-images.ubuntu.com/focal/)
- Ubuntu cloud image of [`Ubuntu 22.04 LTS (Jammy Jellyfish)` \[`amd64`\]](https://cloud-images.ubuntu.com/focal/)

Available on Ansible Galaxy in Collection [jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

## Requirements

Python library `python-apt` is required by Ansible's [`apt`](https://docs.ansible.com/ansible/latest/modules/apt_module.html) module.

| OS                                           | Install Instructions                 |
| -------------------------------------------- | ------------------------------------ |
| Debian 10 (Buster)                           | `apt install python-apt python3-apt` |
| Debian 11 (Bullseye)                         | `apt install python3-apt`            |
| Debian 12 (Bookworm)                         | `apt install python3-apt`            |
| Red Hat Enterprise Linux (RHEL) 7 / CentOS 7 | Not applicable                       |
| Red Hat Enterprise Linux (RHEL) 8 / CentOS 8 | Not applicable                       |
| Red Hat Enterprise Linux (RHEL) 9 / CentOS 9 | Not applicable                       |
| Ubuntu 18.04 LTS (Bionic Beaver)             | `apt install python-apt python3-apt` |
| Ubuntu 20.04 LTS (Focal Fossa)               | `apt install python3-apt`            |
| Ubuntu 22.04 LTS (Jammy Jellyfish)           | `apt install python3-apt`            |

Python library `python-dnf` is required by Ansible's [`dnf`](https://docs.ansible.com/ansible/latest/modules/dnf_module.html) module.

| OS                                           | Install Instructions      |
| -------------------------------------------- | ------------------------- |
| Debian 10 (Buster)                           | Not applicable            |
| Debian 11 (Bullseye)                         | Not applicable            |
| Debian 12 (Bookworm)                         | Not applicable            |
| Red Hat Enterprise Linux (RHEL) 7 / CentOS 7 | Not applicable            |
| Red Hat Enterprise Linux (RHEL) 8 / CentOS 8 | `yum install python3-dnf` |
| Red Hat Enterprise Linux (RHEL) 9 / CentOS 9 | `yum install python3-dnf` |
| Ubuntu 18.04 LTS (Bionic Beaver)             | Not applicable            |
| Ubuntu 20.04 LTS (Focal Fossa)               | Not applicable            |
| Ubuntu 22.04 LTS (Jammy Jellyfish)           | Not applicable            |

## Variables

| Name               | Default value                           | Required | Description                                                                                               |
| ------------------ | --------------------------------------- | -------- | --------------------------------------------------------------------------------------------------------- |
| `distribution_id`  | *depends on operating system*           | no       | List which uniquely identifies a distribution release, e.g. `[ 'Debian', '10' ]` for `Debian 10 (Buster)` |

## Dependencies

None.

## Example Playbook

```yml
- hosts: all
  become: yes
  roles:
  - name: Satisfy software requirements
    role: jm1.pkg.setup
    tags: ["jm1.pkg.setup"]
```

For instructions on how to run Ansible playbooks have look at Ansible's
[Getting Started Guide](https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html).

## License

GNU General Public License v3.0 or later

See [LICENSE.md](../../LICENSE.md) to see the full text.

## Author

Jakob Meng
@jm1 ([github](https://github.com/jm1), [galaxy](https://galaxy.ansible.com/jm1), [web](http://www.jakobmeng.de))

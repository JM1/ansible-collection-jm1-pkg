# Ansible Role: jm1.pkg.setup

This role helps to install necessary tools and libraries for all roles and modules in collection
[jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

**NOTE:** This role will *not* fetch and install any Ansible role or collection, because Ansible preloads all modules,
roles and tasks etc. before it executes any of them. Please make sure that all necessary roles and collections are
installed before running Ansible. To do so, you may follow the steps described in [`README.md`](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/README.md)
using the provided [`requirements.yml`](https://github.com/JM1/ansible-collection-jm1-pkg/blob/master/requirements.yml).

**Tested OS images**
- Cloud image of [`Debian 10 (Buster)` \[`amd64`\]](https://cdimage.debian.org/cdimage/openstack/current/)
- Generic cloud image of [`CentOS 7 (Core)` \[`amd64`\]](https://cloud.centos.org/centos/7/images/)
- Generic cloud image of [`CentOS 8 (Core)` \[`amd64`\]](https://cloud.centos.org/centos/8/x86_64/images/)
- Ubuntu cloud image of [`Ubuntu 20.04 LTS (Focal Fossa)` \[`amd64`\]](https://cloud-images.ubuntu.com/focal/)

Available on Ansible Galaxy in Collection [jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

## Requirements

Python library `python-apt` is required by Ansible's [`apt`](https://docs.ansible.com/ansible/latest/modules/apt_module.html) module.

| OS                                           | Install Instructions                 |
| -------------------------------------------- | ------------------------------------ |
| Debian 10 (Buster)                           | `apt install python-apt python3-apt` |
| Red Hat Enterprise Linux (RHEL) 7 / CentOS 7 | Not applicable                       |
| Red Hat Enterprise Linux (RHEL) 8 / CentOS 8 | Not applicable                       |
| Ubuntu 20.04 LTS (Focal Fossa)               | `apt install python3-apt`            |

Python library `python-dnf` is required by Ansible's [`dnf`](https://docs.ansible.com/ansible/latest/modules/dnf_module.html) module.

| OS                                           | Install Instructions      |
| -------------------------------------------- | ------------------------- |
| Debian 10 (Buster)                           | Not applicable            |
| Red Hat Enterprise Linux (RHEL) 7 / CentOS 7 | Not applicable            |
| Red Hat Enterprise Linux (RHEL) 8 / CentOS 8 | `yum install python3-dnf` |
| Ubuntu 20.04 LTS (Focal Fossa)               | Not applicable            |

## Variables

None.

## Dependencies

| Name            | Description                                                                         |
| --------------- | ----------------------------------------------------------------------------------- |
| `jm1.common`    | Provides `distribution_id` fact which is used to choose OS-specific defaults        |

## Example Playbook

```
- hosts: all
  tasks:
    - name: Satisfy software requirements
      import_role:
        name: jm1.pkg.setup
```

For instructions on how to run Ansible playbooks have look at Ansible's
[Getting Started Guide](https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html).

## License

GPL3

## Author

Jakob Meng
@jm1 ([github](https://github.com/jm1), [galaxy](https://galaxy.ansible.com/jm1), [web](http://www.jakobmeng.de))

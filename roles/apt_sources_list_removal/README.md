# Ansible Role `jm1.pkg.apt_sources_list_removal`

This role removes file `/etc/apt/sources.list`, i.e. to use `*.list` files from `/etc/apt/sources.list.d/` only.

**NOTE:** File `/etc/apt/sources.list` does not exist on Debian 12 (Bookworm), Ubuntu 24.04 LTS (Noble Numbat) and later
releases by default. It has been replaced with `/etc/apt/sources.list.d/debian.sources` and
`/etc/apt/sources.list.d/ubuntu.sources` respectively.

**Tested OS images**
- [Cloud image (`amd64`)](https://cdimage.debian.org/images/cloud/buster/daily/) and
  [Docker images](https://hub.docker.com/_/debian) of Debian 10 (Buster)
- [Cloud image (`amd64`)](https://cdimage.debian.org/images/cloud/bullseye/daily/) and
  [Docker images](https://hub.docker.com/_/debian) of Debian 11 (Bullseye)
- [Cloud image (`amd64`)](https://cdimage.debian.org/images/cloud/bookworm/daily/) and
  [Docker images](https://hub.docker.com/_/debian) of Debian 12 (Bookworm)
- [Cloud image (`amd64`)](https://cdimage.debian.org/images/cloud/trixie/daily/) and
  [Docker images](https://hub.docker.com/_/debian) of Debian 13 (Trixie)
- [Cloud image (`amd64`)](https://cloud-images.ubuntu.com/bionic/current/) of Ubuntu 18.04 LTS (Bionic Beaver)
- [Cloud image (`amd64`)](https://cloud-images.ubuntu.com/focal/) of Ubuntu 20.04 LTS (Focal Fossa)
- [Cloud image (`amd64`)](https://cloud-images.ubuntu.com/jammy/) of Ubuntu 22.04 LTS (Jammy Jellyfish)
- [Cloud image (`amd64`)](https://cloud-images.ubuntu.com/noble/) of Ubuntu 24.04 LTS (Noble Numbat)

Available on Ansible Galaxy in Collection [jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

## Requirements

None.

## Variables

| Name                             | Default value | Required | Description                                                                    |
| -------------------------------- | ------------- | -------- | ------------------------------------------------------------------------------ |
| `force_apt_sources_list_removal` | `false`       | false    | Whether `/etc/apt/sources.list` is removed without prompting for user approval |

## Dependencies

None.

## Example Playbook

```yml
- hosts: all
  become: true
  vars:
    # Variables are listed here for convenience and illustration.
    # In a production setup, variables would be defined e.g. in
    # group_vars and/or host_vars of an Ansible inventory.
    # Ref.:
    # https://docs.ansible.com/ansible/latest/user_guide/playbooks_variables.html
    # https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html
    force_apt_sources_list_removal: true

  roles:
  - name: Remove /etc/apt/sources.list
    role: jm1.pkg.apt_sources_list_removal
    tags: ["jm1.pkg.apt_sources_list_removal"]
```

For instructions on how to run Ansible playbooks have look at Ansible's
[Getting Started Guide](https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html).

## License

GNU General Public License v3.0 or later

See [LICENSE.md](../../LICENSE.md) to see the full text.

## Author

Jakob Meng
@jm1 ([github](https://github.com/jm1), [galaxy](https://galaxy.ansible.com/jm1), [web](http://www.jakobmeng.de))

# Ansible Role `jm1.pkg.apt_sources_list_removal`

This role removes file `/etc/apt/sources.list`, i.e. to use `*.list` files from `/etc/apt/sources.list.d/` only.

**Tested OS images**
- [Cloud images](https://cdimage.debian.org/cdimage/openstack/current/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 10 (Buster)` \[`amd64`\]
- [Cloud image](https://cdimage.debian.org/images/cloud/bullseye/latest/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 11 (Bullseye)` \[`amd64`\]
- Ubuntu cloud image of [`Ubuntu 18.04 LTS (Bionic Beaver)` \[`amd64`\]](https://cloud-images.ubuntu.com/bionic/current/)
- Ubuntu cloud image of [`Ubuntu 20.04 LTS (Focal Fossa)` \[`amd64`\]](https://cloud-images.ubuntu.com/focal/)

Available on Ansible Galaxy in Collection [jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

## Requirements

None.

## Variables

| Name                             | Default value | Required | Description                                                                    |
| -------------------------------- | ------------- | -------- | ------------------------------------------------------------------------------ |
| `force_apt_sources_list_removal` | `no`          | no       | Whether `/etc/apt/sources.list` is removed without prompting for user approval |

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
    force_apt_sources_list_removal: yes

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

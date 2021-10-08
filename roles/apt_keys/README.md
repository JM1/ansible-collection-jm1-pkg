# Ansible Role `jm1.pkg.apt_keys`

This role helps to manage [apt keys](https://blog.jak-linux.org/2021/06/20/migrating-away-apt-key/). It allows to add or
remove apt keys in variable `apt_keys` as a list where each list item is a dictionary of parameters that will be passed
to Ansible's [`apt_key`](https://docs.ansible.com/ansible/latest/modules/apt_key_module.html) module.

**Tested OS images**
- [Cloud images](https://cdimage.debian.org/cdimage/openstack/current/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 10 (Buster)` \[`amd64`\]
- [Cloud image](https://cdimage.debian.org/images/cloud/bullseye/latest/) and
  [Docker images](https://hub.docker.com/_/debian) of `Debian 11 (Bullseye)` \[`amd64`\]
- Ubuntu cloud image of [`Ubuntu 18.04 LTS (Bionic Beaver)` \[`amd64`\]](https://cloud-images.ubuntu.com/bionic/current/)
- Ubuntu cloud image of [`Ubuntu 20.04 LTS (Focal Fossa)` \[`amd64`\]](https://cloud-images.ubuntu.com/focal/)

Available on Ansible Galaxy in Collection [jm1.pkg](https://galaxy.ansible.com/jm1/pkg).

## Requirements

Tool `gpg` is required by Ansible's [`apt_key`](https://docs.ansible.com/ansible/latest/modules/apt_key_module.html) module.

| OS                                           | Install Instructions |
| -------------------------------------------- | -------------------- |
| Debian 10 (Buster)                           | `apt install gnupg`  |
| Debian 11 (Bullseye)                         | `apt install gnupg`  |
| Ubuntu 18.04 LTS (Bionic Beaver)             | `apt install gnupg`  |
| Ubuntu 20.04 LTS (Focal Fossa)               | `apt install gnupg`  |


## Variables

| Name       | Default value                       | Required | Description                                                   |
| ---------- | ----------------------------------- | -------- | ------------------------------------------------------------- |
| `apt_keys` | *depends on `distribution_id` fact* | no       | List of parameter dictionaries for Ansible's `apt_key` module |

## Dependencies

| Name            | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| `jm1.common`    | Provides `distribution_id` fact which is used to choose OS-specific defaults |

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
    apt_keys:
    - id: DCC9EFBF77E11517
      url: https://ftp-master.debian.org/keys/release-10.asc
      keyring: /etc/apt/trusted.gpg.d/debian-archive-buster-stable.gpg
    - id: 4DFAB270CAA96DFA
      url: https://ftp-master.debian.org/keys/archive-key-10-security.asc
      keyring: /etc/apt/trusted.gpg.d/debian-archive-buster-security-automatic.gpg
    - id: DC30D7C23CBBABEE
      url: https://ftp-master.debian.org/keys/archive-key-10.asc
      keyring: /etc/apt/trusted.gpg.d/debian-archive-buster-automatic.gpg
  roles:
  - name: Manage apt keys
    role: jm1.pkg.apt_keys
    tags: ["jm1.pkg.apt_keys"]
```

For instructions on how to run Ansible playbooks have look at Ansible's
[Getting Started Guide](https://docs.ansible.com/ansible/latest/network/getting_started/first_playbook.html).

## License

GNU General Public License v3.0 or later

See [LICENSE.md](../../LICENSE.md) to see the full text.

## Author

Jakob Meng
@jm1 ([github](https://github.com/jm1), [galaxy](https://galaxy.ansible.com/jm1), [web](http://www.jakobmeng.de))

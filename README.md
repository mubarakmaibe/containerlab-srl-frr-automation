# Containerlab SR Linux & FRR Automation Lab

This project uses Containerlab to simulate a BGP network with Nokia SR Linux and FRR routers.  
Automation is handled using Ansible and gNMI (pygnmi) to configure network devices.

## Features
- BGP Peering (SR Linux ↔ FRR)
- Static routing
- Automated configuration with Ansible
- gNMI-based config for SR Linux
- Easily extendable topology

## Usage
1. Deploy lab: `containerlab deploy -t clab.yml`
2. Set up a superuser (required before Ansible can log in): `docker exec clab-minimal-lab-srl1 sr_cli` `enter candidate` `set system aaa authentication user mohammed password "strongpassword"` `set system aaa authentication user mohammed superuser true`
3. Set root password for frr: `docker exec -it clab-minimal-lab-frr1 bash -c 'echo "root:root" | chpasswd'`
4. Run Ansible playbook: `ansible-playbook -i inventory.yml configure_lab.yml`
## To do
- Add more nodes (e.g. srl2, leaf2, alpine hosts)
- CI/CD (optional)

## License
MIT

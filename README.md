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
2. Run Ansible playbook: `ansible-playbook -i inventory.yml configure_lab.yml`
3. Use `configure_srl_bgp.py` for gNMI automation

## To do
- Add more nodes (e.g. leaf2, alpine hosts)
- Export policies for BGP route advertisement
- CI/CD (optional)

## License
MIT

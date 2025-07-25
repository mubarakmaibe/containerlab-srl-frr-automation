import os, json
from pygnmi.client import gNMIclient

def configure_srl_bgp():
    host       = os.getenv("SRL_HOST")
    username   = os.getenv("SRL_USER")
    password   = os.getenv("SRL_PASS")
    router_id  = os.getenv("ROUTER_ID")
    local_as   = int(os.getenv("LOCAL_AS"))
    neighbors  = json.loads(os.getenv("NEIGHBORS"))

    target = (host, 57401)

    with gNMIclient(target=target, username=username,
                    password=password, insecure=True) as gc:

        # 1. Configure system0 interface (loopback)
        gc.set(update=[
            ("/interface[name=system0]/subinterface[index=0]", {
                "admin-state": "enable",
                "ipv4": {"address": [{"ip-prefix": f"{router_id}/32"}]}
            })
        ])

        # 2. Configure ethernet-1/1 for BGP peering
        gc.set(update=[
            ("/interface[name=ethernet-1/1]/subinterface[index=0]", {
                "admin-state": "enable",
                "ipv4": {
                    "admin-state": "enable",
                    "address": [{"ip-prefix": "192.168.1.1/30"}]
                }
            })
        ])

        # 3. Add ethernet-1/1 to default network-instance
        gc.set(update=[
            ("/network-instance[name=default]/interface[name=ethernet-1/1.0]", {})
        ])

        # 2. Create export routing policy
        gc.set(update=[
            ("/routing-policy/policy[name=export-connected]", {
                "statement": [
                    {
                        "name": "10",
                        "match": {
                            "protocol": "local"
                        },
                        "action": {
                            "policy-result": "accept"
                        }
                    }
                ]
            })
        ])

        # 3. Create import routing policy
        gc.set(update=[
            ("/routing-policy/policy[name=import-all]", {
                "statement": [
                    {
                        "name": "10",
                        "action": {
                            "policy-result": "accept"
                        }
                    }
                ]
            })
        ])

        # 4. BGP instance with both import and export policies
        gc.set(update=[
            ("/network-instance[name=default]/protocols/bgp", {
                "admin-state": "enable",
                "autonomous-system": local_as,
                "router-id": router_id,
                "afi-safi": [{"afi-safi-name": "ipv4-unicast", "admin-state": "enable"}],
                "group": [
                    {
                        "group-name": "default-peer-group", 
                        "admin-state": "enable",
                        "export-policy": ["export-connected"],
                        "import-policy": ["import-all"]
                    }
                ],
                "neighbor": [
                    {
                        "peer-address": n["address"],
                        "admin-state": "enable",
                        "peer-as": n["peer_as"],
                        "peer-group": "default-peer-group",
                        "afi-safi": [{"afi-safi-name": "ipv4-unicast", "admin-state": "enable"}]
                    } for n in neighbors
                ]
            })
        ])

        print("SR Linux BGP configuration completed successfully")

if __name__ == "__main__":
    configure_srl_bgp()
from pygnmi.client import gNMIclient

with gNMIclient(target=("172.20.20.3", 57400), username="mohammed", password="strongpassword", insecure=True) as gc:
    print(gc.capabilities())

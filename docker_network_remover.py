import os

i = 2

for i in range(255):
    subnet = '{}.{}.{}.0/24'.format(*__import__('random').sample(range(0, 255), 4))

    print(f"docker network create main{i} --driver bridge --subnet {subnet} ; iptables -t nat -I POSTROUTING -s {subnet} -j NETMAP --to 5.105.24.0/24")

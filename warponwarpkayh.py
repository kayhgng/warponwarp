import requests
import time
import os
from rich import *
print("[green]KayHGNG Wireguard Account Maker v.1 [/green]")

key_input = input("Please enter '1' to make 2 Wireguard Accounts:")

# Check if key_input is '1'
if key_input == '1':
    # Define the URL for the request
    url = "https://api.zeroteam.top/warp?format=sing-box"

    # Make the first request
    response1 = requests.get(url)
    print("[red]First Account:[/red]")
    print(response1.text)

    # Wait for 5 seconds
    time.sleep(5)

    # Make the second request
    response2 = requests.get(url)
    print("[gray]\nSecond Account:[/gray]")
    print(response2.text)
    
    with open('FirstAccount.txt', 'w') as file1:
      file1.write(response1.text)

    with open('SecondAccount.txt', 'w') as file2:
      file2.write(response2.text)  

    print("[yellow]Responses have been saved to FirstAccount.txt SecondAccount.txt and file.[/yellow]")
else:
    print("[red]Invalid input. Exiting without making Account!.[red]")

time.sleep(5)
os.system("cls")

print("""[blue]
  _    _  _      _      _          __        
 | |  | |(_)    | |    | |        / _|       
 | |__| | _   __| |  __| | _   _ | |_  _   _ 
 |  __  || | / _` | / _` || | | ||  _|| | | |
 | |  | || || (_| || (_| || |_| || |  | |_| |
 |_|  |_||_| \__,_| \__,_| \__, ||_|   \__, |
                            __/ |       __/ |
                           |___/       |___/ 
[/blue]""")

print("""[green]





 __          __                  
 \ \        / /                  
  \ \  /\  / /__ _  _ __  _ __   
   \ \/  \/ // _` || '__|| '_ \  
    \  /\  /| (_| || |   | |_) | 
     \/  \/  \__,_||_|   | .__/  
                         | |                                                    
                         |_|     



      
  _  __              _    _    _____  _   _   _____ 
 | |/ /             | |  | |  / ____|| \ | | / ____|
 | ' /  __ _  _   _ | |__| | | |  __ |  \| || |  __ 
 |  <  / _` || | | ||  __  | | | |_ || . ` || | |_ |
 | . \| (_| || |_| || |  | | | |__| || |\  || |__| |
 |_|\_\\\__,_| \__, ||_|  |_|  \_____||_| \_| \_____|    
               __/ |                                
              |___/                                        
      
      V4 - Poweredby Ali Kay H - Github: https://github.com/kayhgng
                                           
                                      
                                                                                                                                                        

[/green]""")
config_template = """[yellow]
{
  "route": {
    "geoip": {
      "path": "geo-assets\\\sagernet-sing-geoip-geoip.db"
    },
    "geosite": {
      "path": "geo-assets\\\sagernet-sing-geosite-geosite.db"
    },
    "rules": [
      {
        "inbound": "dns-in",
        "outbound": "dns-out"
      },
      {
        "port": 53,
        "outbound": "dns-out"
      },
      {
        "clash_mode": "Direct",
        "outbound": "direct"
      },
      {
        "clash_mode": "Global",
        "outbound": "select"
      }
    ],
    "auto_detect_interface": true,
    "override_android_vpn": true
  },
  "outbounds": [
    {
      "type": "selector",
      "tag": "select",
      "outbounds": [
        "auto",
        "IP->Iran, KayH GNG",
        "IP->Main, KayH GNG"
      ],
      "default": "auto"
    },
    {
      "type": "urltest",
      "tag": "auto",
      "outbounds": [
        "IP->Iran, KayH GNG",
        "IP->Main, KayH GNG"
      ],
      "url": "http://cp.cloudflare.com/",
      "interval": "10m0s"
    },
    {
      "type": "wireguard",
      "tag": "IP->Iran, KayH GNG",
      "local_address": [
        "172.16.0.2/32",
        "[ipv6]"
      ],
      "private_key": "[iranprivate]",
      "server": "[ip]",
      "server_port": [port],
      "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
      "reserved": [reserved],
      "mtu": 1280,
      "fake_packets": "5-10"
    },
    {
      "type": "wireguard",
      "tag": "IP->Main, KayH GNG",
      "detour": "IP->Iran, KayH GNG",
      "local_address": [
        "172.16.0.2/32",
        "[ipv62]"
      ],
      "private_key": "[privategermany]",
      "server": "[ip]",
      "server_port": [port],
      "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
      "reserved": [reservedgermany],
      "mtu": 1280,
      "fake_packets": "5-10"
    },
    {
      "type": "dns",
      "tag": "dns-out"
    },
    {
      "type": "direct",
      "tag": "direct"
    },
    {
      "type": "direct",
      "tag": "bypass"
    },
    {
      "type": "block",
      "tag": "block"
    }
  ]  
}
[/yellow]"""

ipv6 = input("Please Enter the Ipv6 iran: ")
iran_private_key = input("Please Enter the Private key of Iran server: ")
ip_for_all = input("Clean IP: ")
ip_port = input("Port Clean IP: ")
reserved_iran = input("Please Enter the reserved of Iran Server: ")
reserved_germany = input("Please Enter the reserved of foreign Server: ")
germany_private_key = input("Please Enter the Private key of foreign server:  ")
ipv6_german = input("Please  Enter the Ipv6 foreign: ")

output = config_template.replace("[ipv6]", ipv6).replace("[iranprivate]", iran_private_key).replace("[ip]", ip_for_all).replace("[port]", ip_port).replace("[reserved]", reserved_iran).replace("[reservedgermany]", reserved_germany).replace("[privategermany]", germany_private_key).replace("[ipv62]", ipv6_german)

print(output)

with open('JsonKayH.txt', 'w') as file:
    file.write(output)

print("Config data has been saved to JsonKayH.txt file.")


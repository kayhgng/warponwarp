print("""
  _    _  _      _      _          __        
 | |  | |(_)    | |    | |        / _|       
 | |__| | _   __| |  __| | _   _ | |_  _   _ 
 |  __  || | / _` | / _` || | | ||  _|| | | |
 | |  | || || (_| || (_| || |_| || |  | |_| |
 |_|  |_||_| \__,_| \__,_| \__, ||_|   \__, |
                            __/ |       __/ |
                           |___/       |___/ 
""")

print("""





 __          __                   _  __              _    _    _____  _   _   _____ 
 \ \        / /                  | |/ /             | |  | |  / ____|| \ | | / ____|
  \ \  /\  / /__ _  _ __  _ __   | ' /  __ _  _   _ | |__| | | |  __ |  \| || |  __ 
   \ \/  \/ // _` || '__|| '_ \  |  <  / _` || | | ||  __  | | | |_ || . ` || | |_ |
    \  /\  /| (_| || |   | |_) | | . \| (_| || |_| || |  | | | |__| || |\  || |__| |
     \/  \/  \__,_||_|   | .__/  |_|\_\\__,_| \__, ||_|  |_|  \_____||_| \_| \_____|
                         | |                   __/ |                                
                         |_|                  |___/                                 
                                      
                                                                                                                                                        

""")
config_template = """
{
  "route": {
    "geoip": {
      "path": "geo-assets\\sagernet-sing-geoip-geoip.db"
    },
    "geosite": {
      "path": "geo-assets\\sagernet-sing-geosite-geosite.db"
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
"""

ipv6 = input("Please Enter the Ipv6 iran: ")
iran_private_key = input("Please Enter the Private key of Iran server: ")
ip_for_all = input("Clean IP: ")
ip_port = input("Port Clean IP ")
reserved_iran = input("Please Enter the reserved of Iran Server: ")
reserved_germany = input("Please Enter the reserved of Germany Server: ")
germany_private_key = input("Please Enter the Private key of Germany server:  ")
ipv6_german = input("Please  Enter the Ipv6 Germany: ")

output = config_template.replace("[ipv6]", ipv6).replace("[iranprivate]", iran_private_key).replace("[ip]", ip_for_all).replace("[port]", ip_port).replace("[reserved]", reserved_iran).replace("[reservedgermany]", reserved_germany).replace("[privategermany]", germany_private_key).replace("[ipv62]", ipv6_german)

print(output)

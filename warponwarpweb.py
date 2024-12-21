import streamlit as st
import json

# Streamlit app title
st.title("KayHGNG Wireguard Account Maker v.2")

# Open website in a new tab
url = "https://kayhgng.github.io/wireguardaccount/"
st.markdown(f"Click [here]({url}) to visit the website for copying and pasting.", unsafe_allow_html=True)

# Input fields for user data
key_input = st.text_input("Please enter 'Iran' to make Warp on Warp for you - Github.com/kayhgng:")
ipv6 = st.text_input("Please Enter the Ipv6 iran:")
iran_private_key = st.text_input("Please Enter the Private key of Iran server:")
reserved_iran = st.text_input("Please Enter the reserved of Iran Server:")
ip_for_all = st.text_input("Clean IP:")
ip_port = st.text_input("Port Clean IP:")
ipv6_german = st.text_input("Please Enter the Ipv6 foreign:")
germany_private_key = st.text_input("Please Enter the Private key of foreign server:")
reserved_germany = st.text_input("Please Enter the reserved of foreign Server:")

# Check if key_input is 'Iran'
if key_input == 'Iran':
    # Config template
    config_template = {
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
            "auto_detect_interface": True,
            "override_android_vpn": True
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
                    ipv6
                ],
                "private_key": iran_private_key,
                "server": ip_for_all,
                "server_port": int(ip_port) if ip_port.isdigit() else None,
                "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
                "reserved": [reserved_iran],
                "mtu": 1280,
                "fake_packets": "5-10"
            },
            {
                "type": "wireguard",
                "tag": "IP->Main, KayH GNG",
                "detour": "IP->Iran, KayH GNG",
                "local_address": [
                    ipv6_german
                ],
                "private_key": germany_private_key,
                "server": ip_for_all,
                "server_port": int(ip_port) if ip_port.isdigit() else None,
                "peer_public_key": "bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=",
                "reserved": [reserved_germany],
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

    # Display the generated JSON configuration
    st.write("Generated Config:")
    st.json(config_template)

    # Convert dict to JSON string for downloading
    json_string = json.dumps(config_template, indent=4)

    # Download button
    st.download_button(
        label="Download Config",
        data=json_string,
        file_name='JsonKayH.txt',
        mime='application/json'
    )

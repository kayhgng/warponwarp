#!/bin/bash

bash <(curl -fsSL https://raw.githubusercontent.com/Ptechgithub/warp/main/endip/install.sh)
pkg install git
apt-get install dos2unix
termux-setup-storage
cd storage
cd downloads
mkdir warponwarp
cd warponwarp
git clone https://github.com/kayhgng/warponwarp.git
pkg install python
cd warponwarp
pip install requests
pip install rich
python warponwarpkayh.py

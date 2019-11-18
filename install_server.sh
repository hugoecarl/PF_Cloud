#!/bin/bash
sudo apt update
sudo apt install python3-pip -y
pip3 install flask
pip3 install flask_restful
sudo ufw allow 5000
cd /home/ubuntu/PF_Cloud
python3 app.py

#!/bin/bash

echo "Detecting your local IP address..."

IP=$(hostname -I | awk '{print $1}')

echo "Your device's IP address is: $IP"
echo "Use this IP address when running 'enable_ssh.sh' on the remote machine."

#!/bin/bash


echo "Detecting your local IP address..."
IP=$(hostname -I | awk '{print $1}')
echo "Your device's IP address is: $IP"
echo "Use this IP address when running 'enable_ssh.sh' on the remote machine."
echo "========="

echo "Detecting your username..."
USERNAME=$(whoami)
echo "Your username is: $USERNAME"
echo "Use this username when running 'enable_ssh.sh' on the remote machine."
echo "========="

echo "When the HOST machine is ready, press any key to continue..."
read -n 1 -s
echo "ssh $USERNAME@$IP"


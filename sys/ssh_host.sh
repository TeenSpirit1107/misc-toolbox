#!/bin/bash

# Ensure root privileges
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run this script as root (e.g., using sudo)"
  exit 1
fi

# Get allowed IP from user
read -p "Enter the IP address of the device that should be allowed to SSH into this machine: " ALLOWED_IP

# Check if openssh-server is installed
if dpkg -l | grep -q openssh-server; then
  echo "OpenSSH Server is already installed."
else
  echo "Updating package index..."
  apt update

  echo "Installing OpenSSH Server..."
  apt install -y openssh-server
fi

echo "Enabling and starting SSH service..."
systemctl enable ssh
systemctl start ssh

echo "Checking SSH service status..."
systemctl status ssh --no-pager

# Ask user whether to enable secure mode
read -p "Do you want to enable secure mode (only allow specific IP to connect)? [y/N] " SECURE_MODE

if [[ "$SECURE_MODE" =~ ^[Yy]$ ]]; then
    echo "Please run this command on the other device:"
    echo "  hostname -I | awk '{print \$1}'"
    read -p "Enter the IP address here: " ALLOWED_IP""
    echo "Allowing SSH access only from IP: $ALLOWED_IP"
    ufw allow from "$ALLOWED_IP" to any port 22 proto tcp
else
    echo "Allowing SSH access from any IP address..."
    ufw allow ssh
fi

echo "Enabling UFW firewall (if not already enabled)..."
ufw enable

echo "Displaying current firewall status..."
ufw status

echo "SSH setup is complete."
echo "You can connect from the allowed device using:"
echo "  ssh username@$(hostname -I | awk '{print $1}')"

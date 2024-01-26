#!/usr/bin/env python3

import os
import subprocess

# Add Brave repository and install Brave
print("Adding Brave repository...")
subprocess.run(["sudo", "apt", "install", "apt-transport-https", "curl", "-y"])
subprocess.run(["sudo", "curl", "-fsSLo", "/usr/share/keyrings/brave-browser-archive-keyring.gpg", "https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg"])
subprocess.run(["echo", "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main", "|", "sudo", "tee", "/etc/apt/sources.list.d/brave-browser-release.list"])
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install", "brave-browser", "-y"])

# Download and install VS Code
print("Downloading Visual Studio Code...")
subprocess.run(["wget", "-qO-", "https://packages.microsoft.com/keys/microsoft.asc", "|", "gpg", "--dearmor", ">", "packages.microsoft.gpg"])
subprocess.run(["sudo", "install", "-o", "root", "-g", "root", "-m", "644", "packages.microsoft.gpg", "/usr/share/keyrings/"])
subprocess.run(["echo", "deb [arch=amd64 signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/vscode stable main", "|", "sudo", "tee", "/etc/apt/sources.list.d/vscode.list"])
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install", "code", "-y"])

# Install VirtualBox
print("Installing VirtualBox...")
subprocess.run(["sudo", "apt", "install", "virtualbox", "-y"])

# Remove older versions of Python
print("Removing older versions of Python...")
subprocess.run(["sudo", "apt", "remove", "--purge", "python2*", "-y"])
subprocess.run(["sudo", "apt", "remove", "--purge", "python3*", "-y"])

# Install Python 3.11.3 with pip
print("Installing Python 3.11.3...")
subprocess.run(["sudo", "apt", "update"])
subprocess.run(["sudo", "apt", "install", "build-essential", "zlib1g-dev", "libncurses5-dev", "libgdbm-dev", "libnss3-dev", "libssl-dev", "libreadline-dev", "libffi-dev", "wget", "-y"])
subprocess.run(["wget", "https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tgz"])
subprocess.run(["tar", "-xf", "Python-3.11.3.tgz"])
os.chdir("Python-3.11.3")
subprocess.run(["./configure", "--enable-optimizations"])
subprocess.run(["make", "-j", str(os.cpu_count())])
subprocess.run(["sudo", "make", "altinstall"])
os.chdir("..")
subprocess.run(["rm", "-rf", "Python-3.11.3", "Python-3.11.3.tgz"])
subprocess.run(["sudo", "apt", "install", "python3-pip", "-y"])

print("Installation completed successfully.")

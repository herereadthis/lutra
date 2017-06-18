# Do These Things When You Get a Raspberry Pi

### Change the default password
```bash
# The default user on a Rapberry Pi is pi, password: raspberry
# Change the sudoer password
passwd
```

### Install these

```bash
# xclip allows you to copy + paste from command line
sudo apt-get install xclip 
# X Windows screensaver application
# the option will show up under "Preferences" from the Desktop menu.
sudo apt-get install xscreensaver
# Network Mapper tool for network discovery
sudo apt-get install nmap
# Requests is an elegant and simple HTTP library for Python
# http://docs.python-requests.org/en/master/
sudo apt-get install python3-requests
# Matplotlib is a Python 2D plotting library: https://matplotlib.org/
sudo apt-get install python3-matplotlib
```

### Updating

```bash
# download the package lists from repositories and "updates" them to get
# information on the newest versions
sudo apt-get update
# upgrade your packages
sudo apt-get upgrade
# upgrade your distribution
sudo apt-get dist-upgrade
```

### Bash Aliases

[Copy the bash script from this repo's resources directory](https://github.com/herereadthis/lutra/blob/master/resources/.bash_aliases)

```bash
cd ~
# paste into this new file, so you don't have to mess with .bashrc
touch .bash_aliases

# relaunch bash
exec bash
```


### Virtual Network computing

[VNC Conect from RealVNC is included with Raspbian](https://www.raspberrypi.org/documentation/remote-access/vnc/README.md). The packages are `realvnc-vnc-server` and `realvnc-vnc-viewer` In Menu > Preferences > RPi Config > Interfaces, enable VNC.

```bash
# what is my IP address?
hostname -I

# scan the whole subnet for other devices
nmap -sn 192.168.1.0/24
```

* Direct connection: Download VNC Viewer onto your computer, and look for the IP address of the Raspberry Pi. Username/password is pi/raspberry as default.
* Cloud Connection: [Register an account with RealVNC](https://www.realvnc.com/raspberrypi/#sign-up). Then go to VNC Server on Raspberry Pi (top right corner), and sign into VNC Viewer on your other machine.
* Virtual Desktop: In RPi terminal run ```vncserver``` and it will generate an IP address. Use that address in VNC viewer. Run ```vncserver -kill :<display-number>``` to kill.

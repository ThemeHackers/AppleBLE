# AppleBLE
#### Apple BLE Proximity Pairing Message Spoofing

> ### :red_circle: Disclaimer
> These scripts are an experimental PoC that uses Bluetooth Low Energy (BLE) to send proximity pairing messages to Apple devices.\
> This project is created for educational purposes and cannot be used for law violation or personal gain.
> The author of this project is not responsible for any possible harm caused by the materials of this project.

## Updates

**7/17/24** <br>
<br>
Thanks to [0DayCTF](https://github.com/0dayctf) the random option has been added!<br> 
<br>
*To run with random :* <br>
```sudo python3 start.py --random``` <br>
*or* <br>
```sudo python3 start.py -r -i 20``` <br>
to set to it to random and the time interval to 20ms, making it more spammy.<br>
<br>

## About This Project
Here is a script for Apple Proximity Pairing Notification Spoofing using Bluetooth Low Energy (BLE) advertising. The script allows you to send BLE advertisements that mimic various Apple devices, such as AirPods and Beats headphones, or even Apple TV setup messages.

## Installation Instructions
Please follow in this exact order or you might run into issues with bluetooth dependencies.

### Clone the Main Repo
```bash
git clone https://github.com/ThemeHackers/AppleBLE.git && cd ./AppleBLE
```

### Install dependencies
```bash
sudo apt update && sudo apt install -y bluez libpcap-dev libev-dev libnl-3-dev libnl-genl-3-dev libnl-route-3-dev cmake libbluetooth-dev
```

### Dependencies requiring manual installation
> :warning: **Warning** <br>
> The `pybluez` library is broken on GitHub and needs to be installed manually
```bash
Download the latest version 
pip install git+https://github.com/pybluez/pybluez.git#egg=pybluez

pycrypto is not maintained, be sure to install pycryptodome instead 
pip install pycryptodome
```

### Install requirements
```bash
sudo pip install -r requirements.txt
```
### Execute scripts without `sudo`
> To be able to run without sudo, you need to set the capabilities of the python binary to allow it to access raw sockets. This is done with the following command 

```bash
sudo setcap cap_net_raw,cap_net_admin+eip $(eval readlink -f $(which python))
```
### If Bluetooth not working
```base
sudo service bluetooth start
sudo systemctl enable bluetooth
```
### Install pybluez 
```base
git clone https://github.com/pybluez/pybluez
cd pybluez/
sudo python3 setup.py install
```
### Reboot Machine
Several users have reported the need for a reboot after installing the bluetooth packages in order for everything to work properly.

## Usage

#### Before running the script, check that your Bluetooth adapter is connected and showing as `hci0`
Run `hcitool dev` to get a list of connected adapters
```bash
hcitool dev
Devices:
    hci0    00:00:7C:00:3A:13
```
> :memo: **Note** <br>
> If the adapter is showing as `hci1` you will need to edit the `dev_id` variable in the scripts to match

### Available options

All messages have been combined into a single app. You can now run `app.py` to get a list of available options.<br>
To run the script use `-d (number of message)`  
> **Example** <br> 
> `start.py -d 13`

```python
sudo python3 start.py
Please select a message option using -d.
Available message options:
1: Airpods
2: Airpods Pro
3: Airpods Max
4: Airpods Gen 2
5: Airpods Gen 3
6: Airpods Pro Gen 2
7: PowerBeats
8: PowerBeats Pro
9: Beats Solo Pro
10: Beats Studio Buds
11: Beats Flex
12: BeatsX
13: Beats Solo3
14: Beats Studio3
15: Beats Studio Pro
16: Beats Fit Pro
17: Beats Studio Buds+
18: AppleTV Setup
19: AppleTV Pair
20: AppleTV New User
21: AppleTV AppleID Setup
22: AppleTV Wireless Audio Sync
23: AppleTV Homekit Setup
24: AppleTV Keyboard
25: AppleTV 'Connecting to Network'
26: Homepod Setup
27: Setup New Phone
28: Transfer Number to New Phone
29: TV Color Balance
```
### Credit
- [FuriousMAC](https://github.com/furiousMAC/continuity) and [Hexway](https://github.com/hexway/apple_bleee) for all the prior research on Apple BLE, Continuity, and building the Wireshark disector.
- [Jae Bochs](https://infosec.exchange/@jb0x168/110879394826675242) for [exposing this to me at DEF CON 31](https://techcrunch.com/2023/08/14/researcher-says-they-were-behind-iphone-popups-at-def-con/) which made me jump into learning about BLE.
- Guillaume Celosia and Mathieu Cunche for reverse engineering [Proximity Pairing](https://petsymposium.org/2020/files/papers/issue1/popets-2020-0003.pdf") 


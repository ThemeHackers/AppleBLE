import bluetooth

def find_devices():

    nearby_devices = bluetooth.discover_devices(lookup_names=True, flush_cache=True)

    for addr, name in nearby_devices:
        try:
      
            hci_sock = bluetooth.hci_open_dev(bluetooth.hci_devid(addr))
            hci_info = hci_sock.getsockname()
            interface = hci_info[0]

           
            rssi = bluetooth.hci_read_remote_rssi(hci_sock, addr)
            if rssi != None:  
                print(f"Device: {name} ({addr}), Interface: {interface}, RSSI: {rssi}")

        except bluetooth.btcommon.BluetoothError as e:
            print(f"Error with {name} ({addr}): {e}")

if __name__ == "__main__":
    find_devices()

import socket
import struct

def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('!6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

#import subprocess

#data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
#profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
#for i in profiles:
#    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
#    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
#    try:
#        print ("{:<30}|  {:<}".format(i, results[0]))
#    except IndexError:
#        print ("{:<30}|  {:<}".format(i, ""))

from scapy.all import *
import csv

def get_mss(ip_address):
    try:
        response = sr1(IP(dst=ip_address)/TCP(dport=80, flags="S"), verbose=False, timeout=5)
        if response and response.haslayer(TCP) and response[TCP].options:
            for option in response[TCP].options:
                if isinstance(option, tuple) and option[0] == 'MSS':
                    print(f"{ip_address}: success.")
                    return option[1]
    except Exception as e:
        #wr.writerow([target_site, e])
        print(f"{ip_address}: Error occurs: {e}")
    return None

if __name__ == "__main__":

    f=open("MSS-of-256-ip", 'w', newline='')
    wr=csv.writer(f)

    for i in range(256):
        ip_address="172.217.25."+str(i)
        mss = get_mss(ip_address)
        if mss:
            print(f"mss: {mss}")
            wr.writerow([ip_address, mss])
        else:
            wr.writerow([ip_address, 'error'])
    f.close()

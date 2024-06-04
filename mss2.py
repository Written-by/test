from scapy.all import *

def get_mss(target_site):
    try:
        # Send SYN packet to initiate TCP connection
        response = sr1(IP(dst=target_site)/TCP(dport=80, flags="S"), verbose=False, timeout=5)
                                    
        # Extract MSS value from TCP options
        if response and response.haslayer(TCP) and response[TCP].options:
            for option in response[TCP].options:
                if isinstance(option, tuple) and option[0] == 'MSS':
                    return option[1]
    except Exception as e:
        f2.writelines(f"Error: {e}\n")
        print(f"Error occurs.\n")
    return None

if __name__ == "__main__":

    f=open("alexa-top-1000.txt", 'r')
    f2=open("MSS-of-1000.txt", 'w')

    while True:
        target_site=f.readline()
        if not target_site: break
        target_site=target_site.strip()
        mss = get_mss(target_site)
        if mss:
            f2.writelines(f"MSS for {target_site}: {mss}\n")
        else:
            f2.writelines(f"Failed to retrieve MSS for {target_site}.\n")
    f.close()
    f2.close()


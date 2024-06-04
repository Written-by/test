from scapy.all import *

def get_mss(target_site):
    # Send SYN packet to initiate TCP connection
    response = sr1(IP(dst=target_site)/TCP(dport=80, flags="S"), verbose=False)
                
    # Extract MSS value from TCP options
    if response and response.haslayer(TCP) and response[TCP].options:
        for option in response[TCP].options:
            if isinstance(option, tuple) and option[0] == 'MSS':
                return option[1]
                                                                        
    return None

if __name__ == "__main__":
    f=open("txt/alexa-top-1000.txt", 'r')

    while True:
        line=f.readline()
        if not line: break
        target_site = line
        mss = get_mss(target_site)
        if mss:
            print(f"MSS for {target_site}: {mss}")
        else:
            print(f"Failed to retrieve MSS for {target_site}.")
    
    f.close()

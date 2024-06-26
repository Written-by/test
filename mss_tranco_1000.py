from scapy.all import *
import csv

def get_mss(target_site):
    try:
        seq_num = random.randint(1000, 65535)
        # Send SYN packet to initiate TCP connection
        response = sr1(IP(dst=target_site)/TCP(dport=80, flags="S", seq=seq_num), verbose=False, timeout=5)
                                    
        # Extract MSS value from TCP options
        if response and response.haslayer(TCP) and response[TCP].options:
            for option in response[TCP].options:
                if isinstance(option, tuple) and option[0] == 'MSS':
                    print(f"success.")
                    return option[1]
    except Exception as e:
        #wr.writerow([target_site, e])
        print(f"Error occurs.")
    return None

if __name__ == "__main__":

    f=open("tranco_N3NGW.csv", 'r')
    rdr=csv.reader(f)
    f2=open("MSS-of-1000-tranco.csv", 'w', newline='')
    wr=csv.writer(f2)

    for line in rdr:
        print(line)
        target_site=line[1]
        if not target_site: break
        target_site=target_site.strip()
        mss = get_mss(target_site)
        if mss:
            wr.writerow([target_site, mss])
        else:
            wr.writerow([target_site, 'error'])
        if line[0]=='100': break
    f.close()
    f2.close()


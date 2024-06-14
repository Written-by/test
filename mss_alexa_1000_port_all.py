from scapy.all import *
import csv

def get_mss(target_site, portnum):
    try:
        seq_num = random.randint(1000, 65535)
        # Send SYN packet to initiate TCP connection
        response = sr1(IP(dst=target_site)/TCP(dport=portnum, flags="S", seq=seq_num), verbose=False, timeout=5)
                                    
        # Extract MSS value from TCP options
        if response and response.haslayer(TCP) and response[TCP].options:
            for option in response[TCP].options:
                if isinstance(option, tuple) and option[0] == 'MSS':
                    return option[1]
    except Exception as e:
        #f2.writelines(f"Error: {e}\n")
        #print(f"Error occurs.\n")
        print("no response: ", portnum)
    return None

if __name__ == "__main__":

    f=open("alexa-top-1000-no-response.txt", 'r')
    rdr=csv.reader(f)
    f2=open("MSS-of-1000-alexa-port_all.csv", 'w', newline='')
    wr=csv.writer(f2)

    for line in rdr:
        print(line)
        target_site=line[0]
        if not target_site: break
        target_site=target_site.strip()
        flag=False
        for portnum in range(1024):
            mss = get_mss(target_site, portnum)
            if mss:
                print(target_site, ": responsed at port ", portnum, "\n")
                wr.writerow([target_site, mss, portnum])
                flag=True
                break
            else:
                print("no response: ", portnum)
        if not flag:
            print(target_site, ": no response\n")
            wr.writerow([target_site, 'no response'])
    f.close()
    f2.close()


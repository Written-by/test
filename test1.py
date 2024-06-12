from scapy.all import *

def measure_mss(destination):
    # Send IPv6 SYN packet to the destination and capture the response
    response = sr1(IPv6(dst=destination)/TCP(dport=80, flags="S"), verbose=False)

    # Extract MSS value from the response
    if response:
        # Get the MSS option from the response
        mss_option = [opt for opt in response[TCP].options if isinstance(opt, TCPOption_MSS)]
        if mss_option:
            mss = mss_option[0].mss
            print(f"MSS for {destination}: {mss}")
        else:
            print("No MSS option found in the response.")
    else:
        print("No response received.")

# Replace "destination_website.com" with the website you want to measure MSS for
destination_website = "google.com"
measure_mss(destination_website)

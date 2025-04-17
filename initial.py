# Script to analyze the campus network and derive meaningful insights


# Script to analyze the campus network and derive meaningful insights

from scapy.all import rdpcap, IP, TCP, UDP
from collections import Counter

def analyze_traffic(pcap_file):
    """
    Analyze network traffic from a PCAP file and derive insights.
    """
    print(f"Analyzing traffic from {pcap_file}...")
    
    packets = rdpcap(pcap_file)
    ip_counter = Counter()
    protocol_counter = Counter()

    for packet in packets:
        if IP in packet:
            # Count source and destination IPs
            ip_counter[packet[IP].src] += 1
            ip_counter[packet[IP].dst] += 1
            
            # Count protocols
            if TCP in packet:
                protocol_counter['TCP'] += 1
            elif UDP in packet:
                protocol_counter['UDP'] += 1
            else:
                protocol_counter['Other'] += 1

    # Display insights
    print("\nTop 5 IPs by traffic:")
    for ip, count in ip_counter.most_common(5):
        print(f"{ip}: {count} packets")
    
    print("\nProtocol distribution:")
    for protocol, count in protocol_counter.items():
        print(f"{protocol}: {count} packets")

if __name__ == "__main__":
    # Replace 'network_traffic.pcap' with the path to your PCAP file
    pcap_file = "network_traffic.pcap"
    analyze_traffic(pcap_file)
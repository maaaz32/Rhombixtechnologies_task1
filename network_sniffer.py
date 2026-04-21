#!/usr/bin/env python3
"""
Basic Network Sniffer
Rhombix Technologies - Cyber Security Internship Task 1
Captures and displays basic IP, TCP, and UDP packet info.
NOTE: Must be run with sudo on Linux.
"""

import socket
import struct


def parse_ethernet(raw_data):
    """Extract destination MAC, source MAC, and protocol from Ethernet frame."""
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', raw_data[:14])
    return format_mac(dest_mac), format_mac(src_mac), socket.htons(proto), raw_data[14:]


def format_mac(bytes_addr):
    """Convert bytes to readable MAC address format."""
    return ':'.join(map('{:02x}'.format, bytes_addr))


def parse_ipv4(raw_data):
    """Extract source IP, destination IP, and protocol from IPv4 packet."""
    version_header_len = raw_data[0]
    header_len = (version_header_len & 15) * 4  # Header length in bytes
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', raw_data[:20])
    src_ip = socket.inet_ntoa(src)
    dest_ip = socket.inet_ntoa(target)
    return proto, src_ip, dest_ip, raw_data[header_len:]


def parse_tcp(raw_data):
    """Extract source port and destination port from TCP segment."""
    src_port, dest_port = struct.unpack('! H H', raw_data[:4])
    return src_port, dest_port


def parse_udp(raw_data):
    """Extract source port and destination port from UDP segment."""
    src_port, dest_port = struct.unpack('! H H', raw_data[:4])
    return src_port, dest_port


def start_sniffer():
    """Main function to start capturing packets."""
    print("=" * 55)
    print("       Basic Network Sniffer - Rhombix Technologies")
    print("=" * 55)
    print("Listening for packets... Press Ctrl+C to stop.\n")

    # Create a raw socket to capture all packets
    # AF_PACKET = Linux raw socket | ETH_P_ALL = capture all protocols
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    packet_count = 0

    try:
        while True:
            raw_data, addr = conn.recvfrom(65535)
            packet_count += 1

            # --- Parse Ethernet Frame ---
            dest_mac, src_mac, eth_proto, data = parse_ethernet(raw_data)

            # --- Only process IPv4 packets (protocol 8) ---
            if eth_proto == 8:
                proto, src_ip, dest_ip, ip_data = parse_ipv4(data)

                print(f"[Packet #{packet_count}]")
                print(f"  Source IP      : {src_ip}")
                print(f"  Destination IP : {dest_ip}")

                # --- TCP Packet (protocol 6) ---
                if proto == 6:
                    src_port, dest_port = parse_tcp(ip_data)
                    print(f"  Protocol       : TCP")
                    print(f"  Source Port    : {src_port}")
                    print(f"  Dest Port      : {dest_port}")

                # --- UDP Packet (protocol 17) ---
                elif proto == 17:
                    src_port, dest_port = parse_udp(ip_data)
                    print(f"  Protocol       : UDP")
                    print(f"  Source Port    : {src_port}")
                    print(f"  Dest Port      : {dest_port}")

                else:
                    print(f"  Protocol       : Other (#{proto})")

                print("-" * 45)

    except KeyboardInterrupt:
        print(f"\n[!] Sniffer stopped. Total packets captured: {packet_count}")
    except PermissionError:
        print("\n[ERROR] Permission denied.")
        print("Please run with: sudo python3 network_sniffer.py")


# --- Entry Point ---
if __name__ == "__main__":
    start_sniffer()

# Network Packet Sniffer

A Python-based network packet sniffer built to capture and analyse live network traffic in real time.
Developed as part of a Cybersecurity Internship at Rhombix Technologies.

## Features
- Captures raw network packets using Python's socket library
- Identifies protocol types (TCP, UDP, ICMP)
- Extracts source and destination IP addresses
- Detects suspicious payloads and simulated DDoS traffic patterns
- Cross-validated results with Wireshark for accuracy

## Tech Stack
- Python 3
- Raw sockets (`socket` library)
- Linux (Kali / Ubuntu)

## How to Run
1. Clone the repository:
   git clone https://github.com/maaaz32/network-packet-sniffer
2. Run with root privileges (required for raw socket access):
   sudo python3 sniffer.py

## Requirements
- Linux OS (Kali recommended)
- Python 3.x
- Root / sudo access

## Disclaimer
This tool is intended for educational and authorised security testing purposes only.
Unauthorised use on networks you do not own or have permission to test is illegal.

## Author
Maaz Ali — Cybersecurity Undergraduate, KIET Karachi
GitHub: https://github.com/maaaz32

import pyshark
import pandas as pd

capture = pyshark.FileCapture('/home/kali/traffic.pcapng')

data = []

for packet in capture:
    try:
        src = packet.ip.src
        dst = packet.ip.dst
        protocol = packet.highest_layer
        length = packet.length

        data.append([src, dst, protocol, length])

    except AttributeError:
        pass

df = pd.DataFrame(data, columns=[
    "Source IP",
    "Destination IP",
    "Protocol",
    "Packet Length"
])

df.to_csv("network_data.csv", index=False)

print(df.head())

print("\nData saved to network_data.csv")

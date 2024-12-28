import os
import random
import subprocess

def generate_mac():
    return ":".join(f"{random.randint(0, 255):02x}" for _ in range(6))

def change_mac(interface):
    mac = generate_mac()
    try:
        subprocess.call(["ifconfig", interface, "down"])
        subprocess.call(["ifconfig", interface, "hw", "ether", mac])
        subprocess.call(["ifconfig", interface, "up"])
        print(f"MAC address changed to: {mac}")
    except Exception as e:
        print(f"Error: Unable to change MAC address. Details: {e}")
        exit(1)

def main():
    print("""
                          _..._      .-'''-.                                     .-'''-.                           _..._                     
                       .-'_..._''.  '   _    \_______                           '   _    \                      .-'_..._''.            .---. 
                     .' .'      './   /` '.   \  ___ `'.        __.....__     /   /` '.   \              .--. .' .'      '..--.        |   | 
                    / .'         .   |     \  '' |--.\  \   .-''         '.  .   |     \  '  _.._    _.._|__|/ .'          |__|        |   | 
                   . '           |   '      |  | |    \  ' /     .-''"'-.  `.|   '      |  .' .._| .' .._.--. '            .--.        |   | 
                   | |           \    \     / /| |     |  /     /________\   \    \     / /| '     | '   |  | |            |  |   __   |   | 
.--------..--------| |            `.   ` ..' / | |     |  |                  |`.   ` ..' __| |__ __| |__ |  | |            |  |.:--.'. |   | 
|____    ||____    . '               '-...-'`  | |     ' .\    .-------------'   '-...-'|__   __|__   __||  . '            |  / |   \ ||   | 
    /   /     /   / \ '.          .            | |___.' /' \    '-.____...---.             | |     | |   |  |\ '.          |  `" __ | ||   | 
  .'   /    .'   /   '. `._____.-'/           /_______.'/   `.             .'              | |     | |   |__| '. `._____.-'|__|.'.''| ||   | 
 /    /___ /    /___   `-.______ /            \_______|/      `''-...... -'                | |     | |          `-.______ /   / /   | |'---' 
|         |         |           `                                                          | |     | |                   `    \ \._,\ '/     
|_________|_________|    MMAACCCCHHAANNGGEERR                                              |_|     |_|                         `--'  `"      
    """)

    interface = input("Enter the network interface (e.g., eth0, wlan0): ")
    change_mac(interface)

if __name__ == "__main__":
    main()

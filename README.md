# MAC Changer

**MAC Changer** is a Python script that randomly generates and applies a new MAC address to a specified network interface. This tool is ideal for enhancing privacy or conducting network experiments.

## Features

- Generates a random MAC address.
- Applies the new MAC address to the specified network interface.
- Lightweight and easy to use.

## Requirements

- Python 3.x
- Administrative/root permissions to modify network interfaces.

## Installation

Clone the repository:

```bash
git clone https://github.com/umutkayash/macchanger.git
cd macchanger
```

## Usage

Run the script:

```bash
python macchanger.py
```

You will be prompted to enter the network interface (e.g., `eth0`, `wlan0`). The script will then generate and apply a new MAC address.

## Example Output

```
"""
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
    """
Welcome to the MAC Address Changer!
Enter the network interface (e.g., eth0, wlan0): wlan0
MAC address changed to: 00:1a:2b:3c:4d:5e
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.

## Disclaimer

Use this tool responsibly. The author is not liable for any misuse or damage caused by the script.

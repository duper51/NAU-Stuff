# NAU Stuff
A bunch of various scripts that I needed to get things working at NAU.

# SC-Autoconnect
SC-Autoconnect.py is a python script that assists headless SafeConnect users connect to the network. It's very useful if you are on a low-memory platform such as a Raspberry Pi and want to run updates. To get the script to work, just change the text saying USERNAME and PASSWORD to your username and password.

# Using a VPN such as OpenVPN
This one was fantastic. There are no blocked ports at NAU from the internal side, so as usual the VPN connection was successful. However, due to the use of SafeConnect, the connection would drop frequently due to the SafeConnect protocol not being able to connect from the internal network. The solution was to add custom routes to internal networks and to the SafeConnect IP addresses to bypass the VPN.

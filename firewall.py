#!/usr/bin/python3

from systemd import journal
import re
import pyufw as ufw 

j = journal.Reader()
j.this_boot()
j.log_level(journal.LOG_INFO)
j.add_match(_SYSTEMD_UNIT="ssh.service")
ip_addresses = set()

for entry in j:
        message = entry["MESSAGE"]
        if message.startswith("Failed"):
                ip_addresses.update(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', message))

ufw.default = "deny" # Set default ufw policy to deny
ufw.enable = True # Enable ufw

for ip in ip_addresses:
        print(ip)
        # Adding new ufw rule to deny from specific IP
        ufw.add("deny from " + ip)

ufw.add("allow from any to any port 22") # Allow SSH traffic

#!/usr/bin/python3

from systemd import journal
import re
import pyufw as ufw 

j = jounral.Reader()
j.this_boot()
j.log_level(journal.LOG_INFO)
j.add_match(_SYSTEMD_UNIT="ssh.service")
ip_addresses = set()

for entry in j: # Read every entry in the journal
        message = entry["MESSAGE"]
        if message.startswith("Failed"):
                ip_addresses.update(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', message>

for ip in ip_addresses:
        print(ip)
        # Adding new ufw rule to deny from specific IP
        ufw.add("deny from " + ip)

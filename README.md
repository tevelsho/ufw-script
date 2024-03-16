# Auto UFW Script

This Python script automatically blocks IP addresses that have failed SSH login attempts using the ufw firewall on Ubuntu. It reads failed SSH login attempts from the system journal and adds firewall rules to block these IP addresses.

Instructions

    Install UFW and PyUFW:

    sudo apt update
    sudo apt install ufw
    sudo apt install python3-pip
    sudo pip3 install pyufw

Create the Firewall Script:

    Create a file named firewall.py and paste the provided Python script.
    Make the script executable:

    chmod +x firewall.py
    
Enable UFW and Allow SSH:

    Allow SSH connections (assuming SSH is on port 22):

    sudo ufw allow 22

Enable the UFW firewall:

    sudo ufw enable
    
Test the Script:

    Run the script to ensure it can be executed without errors:

    sudo python3 firewall.py 2> /dev/null

    Check the UFW status to see if the rules are applied:
    
    sudo ufw status

Set up Cron Job:

    Edit the crontab for the root user:

    sudo crontab -e

Add the following line to the crontab to run the script every hour:

    0 * * * * sudo python3 /path/to/firewall.py

    Save and exit the crontab editor.

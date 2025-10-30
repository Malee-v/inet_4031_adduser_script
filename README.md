# Inet_4031_adduser_script

## Program Description

This program automates the process of adding users to a system using a structured input file. Instead of manually typing commands like 'useradd' and 'groupadd' for each user, the script reads user data from a file and executes the necessary commands automatically.
Traditionally, a system administrator would add users by running:

'sudo adduser <account name>'

And then manually put in all the user's information, password, Full name, Room, etc. 

Then, manually assign the user to a group:

'sudo adduser <user> <group>' (assuming the group has been created), if not, create the group with: 'sudo addgroup [group name]'

This script uses those same commands internally, allowing administrators to batch-create users and assign them to groups efficiently. It reduces manual effort, minimizes errors, and ensures consistent user setup across the system.

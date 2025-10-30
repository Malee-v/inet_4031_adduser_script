# Inet_4031_adduser_script

## Program Description

This program automates the process of adding users to a system using a structured input file. Instead of manually typing commands like 'useradd' and 'groupadd' for each user, the script reads user data from a file and executes the necessary commands automatically.
Traditionally, a system administrator would add users by running:

'sudo adduser [account name]'

And then manually put in all the user's information, password, Full name, Room, etc. 

Then, manually assign the user to a group:

'sudo adduser [user] [group]' (assuming the group has been created), if not, create the group with: 'sudo addgroup [group name]'

This script uses those same commands internally, allowing administrators to batch-create users and assign them to groups efficiently. It reduces manual effort, minimizes errors, and ensures consistent user setup across the system.

## Program User Operation

This section explains how to operate the script. After reading this, users will understand how to prepare the input file and execute the script. The internal comments in the code explain the logic and flow in detail.
### Input File Format
Each line in the input file should follow this format:

User:Pass:LastName:FirstName:GroupID,..

username
: login name of the user.

Password
: User's password to log in.

LastName
: Last name of the user.

FirstName
: First name of the user.

GroupID
: The user's group (there can be more than one group, distinguished with ',' between groups listed)

## Command Execution

To run the script, use the following command:

'./create-users.py < createusers.input'

You may need to run it with elevated permissions:

'sudo ./create-users.py < create-users.input'

If those do not work, try:

'sudo python3 create-users.py < create-users.input'



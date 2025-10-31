#!/usr/bin/python3

# DRY RUN PROMPT DOES NOT WORK WITH < Input REDIRECTION

# INET4031
# Malee Vang
# Date Created: 10/29/2025
# Date Last Modified: 10/30/2025

# Imports
import os   # Operating system module - execute system level commands
import re   # Regular expressions module - detect comment lines
import sys  # Read input line by line from standard input

def main():
    # Prompt user for dry-run mode
   # dry_run_input = input("Would you like to run in dry-run mode? (Y/N): ").strip().upper()
   # dry_run = (dry_run_input == 'Y')

   # Alternative to dry run: 
   # sudo python3 create-users2.py --dry-run < create-users.input

    dry_run = "--dry-run" in sys.argv


    for line in sys.stdin:
        # Checks if the line starts with '#' which indicates a comment, all comments are put into the variable 'match' for later use
        match = re.match("^#", line)

        # Split each line into fields ':' indicatig a new field - user:pass:lastname:firstname:group
        fields = line.strip().split(':')

        # Skip the line if; starts with '#' (comment) or the fields does not equal to 5 (invalid format)
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print(">> SKIPPED: Comment line detected.") #A '#' was found 
                elif len(fields) != 5:
                    print(f">> ERROR: Invalid field count ({len(fields)}) in line: {line.strip()}") #does not have all 5 field
            continue # continue onto the next line

        #defining variable in which field, extracting user information from the field/input 
        username = fields[0] #user name in field 1
        password = fields[1] #user password in field 2
        gecos = "%s %s,,," % (fields[3], fields[2]) #stores general information like last name, first name
        groups = fields[4].split(',') #5 field is the group and it can have multiple field with a comma seperating the group

        # Account creation, prints a message confirming that the account is being created
        print(f"==> Creating account for {username}...")
        #Build the command to create the user with no password and GECOS info
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"

        if dry_run: 
            print(f"[DRY-RUN] Would run: {cmd}")#print the cmd if its on dry mode
        else:
            os.system(cmd) #else, run the command to create the user

        # Password setting
        print(f"==> Setting the password for {username}...") #Confirmed a password is being set for the user
        #Command sets the user's password. Echo to print the password twice (one for entry, one for confirmation) then pipes that into the passwd command
        cmd = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}" 

        if dry_run:
            print(f"[DRY-RUN] Would run: {cmd}") #if dry run, previous cmd would be printed out instead of executing
        else:
            os.system(cmd) #else, execute the previous cmd 

        # Group assignment
        for group in groups:
            if group != '-': #if group is not empty-
                print(f"==> Assigning {username} to the {group} group...") #verify that the user is being assign to a group
                cmd = f"/usr/sbin/adduser {username} {group}" #assign user to that group
                if dry_run:
                    print(f"[DRY-RUN] Would run: {cmd}") #prints cmd instead of executing if dry run is true
                else:
                    os.system(cmd) #else, execute and assign user to the group
            elif dry_run:
                print(f"[DRY-RUN] Skipped invalid group entry '-' for user {username}.") #if group is empty, print this message in dry run mode

if __name__ == '__main__':
    main()


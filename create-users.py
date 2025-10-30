#!/usr/bin/python3

# INET4031
# Malee Vang
# Data Created: 10/29/2025
# Date Last Modified: 10/29/2025

#import
import os #operating system module - execute system level commands
import re #regular expressions module - work with patterns in string, detecting comment lines
import sys #read input line by line from standard input


def main():
    for line in sys.stdin:

        #Checks if the line starts with '#' which indicates a comment, all comment are gather into a variable 'match' for later use
        match = re.match("^#",line)

        #Split each line into fields using ':' - user:passwd:lastname:firstname
        fields = line.strip().split(':')

        #skip the line if - starts with '#' (comment) or the fields does not equal to 5 (invalid format) continue to the next line 
        if match or len(fields) != 5:
            continue
        
        #defining variable in which field, extracting user information from the fields
        username = fields[0] #The account name to be created
        password = fields[1] #The password for the new account
        gecos = "%s %s,,," % (fields[3],fields[2]) #'gecos' field stores general information like full name 

        #the group field may have more than 1 group, seperating them with ',' allow to assign user to multiple groups later
        groups = fields[4].split(',')

        #Prints a message confirming that the account is being created
        print("==> Creating account for %s..." % (username))
        #Build the command to create the user with no password and GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

    
        #print cmd #If uncommented, it will print the cmd. When first testing, you should only print cmd to verify correctness
        #os.system(cmd) #If uncommented, would execute the actual user created command on the system, disabling password

        #Prints progress message before setting the password
        print("==> Setting the password for %s..." % (username))
        #Command sets the user's password. Echo to print the password twice (one for entry, one for confirmation) then pipes that into the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        
        #print cmd #print first to verify before executing
        #os.system(cmd) #runs the previous cmd (activating it into the system)

        for group in groups:
            #Loop through the list of groups and assign the user to each valid group
            #skips group entries with '-', if the group is valid, adds the user to that group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()

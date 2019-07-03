#! /usr/bin/env python3
# coding: utf-8

import mysql.connector
from config import M_user,M_password

########################

def executeScriptsFromFile(filename):
    # Open and read the file as a single buffer
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()

    # all SQL commands (split on ';')
    sqlCommands = sqlFile.split(';')
    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        
        try:
            command = command + ";"
            print(command)
            cursor.execute(command)
            print("Command executed")
        except :
            print ("Command skipped")

########################




cnx = mysql.connector.connect\
(user=M_user, password=M_password, host='localhost')
cursor = cnx.cursor()


executeScriptsFromFile("sql_script_purbeurre.sql")

cursor.close()
cnx.close()



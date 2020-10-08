import os
import sys

os.system("clear")
banner = """ 
 _____     _        _   ____                  
|_   _|__ | |_ __ _| | / ___|  ___ __ _ _ __  
  | |/ _ \| __/ _` | | \___ \ / __/ _` | '_ \ 
  | | (_) | || (_| | |  ___) | (_| (_| | | | |
  |_|\___/ \__\__,_|_| |____/ \___\__,_|_| |_|

A Python script for full network scan 
Version: 1.0.0v
Author: AzizVirus
Github: github.com/Azizvirus
Powered By Nmap & Dmitry In Kali Linux
To Make Information Gathering & Scanning Easier
"""
print banner
target = raw_input("Enter Target To Scan: ")
print ("Target Selected: " + target)
print ("")
print ("Nmap Scan Will Start NOW !")
print ("---------------------------")
print ("Full Ports Scan:")
print ("")
os.system("nmap -F -sV -r "+target)

print ("")
print ("Nmap Ports Scan Finished !\n")
print ("----------------------------")
print ("Nmap Agressive OS Scan Will Start NOW !")
print ("----------------------------")
os.system("nmap -F -O --osscan-guess "+target)
print ("")
print ("Nmap Os Scan Finished !")
print ("")
print ("-------------------------")
print ("")
print ("Nmap Full MISC Scan Will Start Now !\n")
print ("-------------------------\n")
os.system("nmap -6 -A -V "+target)
print ("")
print ("Nmap Full MISC Scan Finished !\n")
print ("-------------------------\n")
print ("Dmitry Agressive Scans Will Start NOW !\n")
print ("--------------------------\n")
os.system ("dmitry -i -w -s -e f "+target)
print ("")
print (" Finished All Scans !!! ")
sys.exit ("Quitting ...")





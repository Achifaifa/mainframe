#!/usr/bin/env python
import os
import sys
import subprocess

#Define mode variable. 0=manual installation, 1=full auto
mode=0

#Define key variables
memory=0
cpunum=0
timezone=0

#Define path to z/OS files
path=0

#Define status variables
#true = Variable is OK; 
#false = Variable is not OK
#configuration file can not be created or exported if any of this variables is set to false
memoryok="false"
cpunumok="false"
timezoneok="false"
hercpathok="false"

#Gets amount or RAM assigned
  #Checks that assigned RAM < available RAM
  #Checks that assigned RAM = 2^n
def getram():

    #PENDING

#Gets number of CPUs available for hercules
  #checks that assigned CPUs < available CPUs
  #Issues warning if available CPUs < assigned CPUs < available cores
def getcpu():
  
    #PENDING
    
#Gets timezone
  #Checks timezone with time server
def getzone():    

    #PENDING

#Looks for z/OS files and sets path
def getpath():
  
    #PENDING
  
#Display fucntion. This displays the current values of the variables
def display():
  
    global memory
    global cpunum
    global timezone

    
    print "	Current configuration:"
    print "	Max. memory:	",memory," MB"
    print "	Number of CPUs:	",cpunum
    print "	Timezone:       GMT+",timezone
    print "	Hercules path:	",hercpath
    
#Help function.
def help():
    
    os.system('clear')
    print "Hercules.cnf creator -- Achifaifa (2013) \n"
    print "User help \n"
    print "This program creates a custom-made hercules.cnf file "
    print "It writes key parameters into a pre-made file, which "
    print "should be enough for basic installations. \n"
    print "INSTRUCTIONS:\n"
    print "A) Install hercules."
    print "B) Place the z/OS files somewhere. I recommend /zOS/ or "
    print "   a similar short path."
    print "C) Run this script: Set up the variables and paths and "
    print "   export the file.\n "
    
	   
    input("Press any key to continue")

#Create file function. This takes all the data and uses it to create the file
def create():
  
    #PENDING
    
#This function installs hercules
def install():
  
    cmd = ['sudo apt-get install hercules']
    
#Menu function
def menu():
    menu=0
    
    while 1 == 1 :
      os.system('clear')
      print "Hercules.cnf creator -- Achifaifa (2013) \n"
      print "1.- Install hercules\n"
      print "2.- Set variables"
      display()
      print "3.- Create and save file"
      print "---"
      print "9.- Help "
      print "0.- Exit \n"

    
      menu=input ("")
      
      if menu == 1:
	install()
      elif menu == 2:
	assign()
      elif menu == 3:
	print "3"
      elif menu == 4:
	print "4"
      elif menu == 9:
	help()
      elif menu == 0:
	sys.exit()
      else: 
	break

#Main process (just calling menu over and over again)
while 1 == 1 :	
  menu()
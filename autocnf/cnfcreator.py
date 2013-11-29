#!/usr/bin/env python
import os
import sys
import subprocess
import platform
import multiprocessing
import time

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
memoryok=0
cpunumok=0
timezoneok=0
hercpathok=0

#Gets amount or RAM assigned
  #Checks that assigned RAM < available RAM
  #Checks that assigned RAM = 2^n
def getram():

    #PENDING
    #Apparently python does not have a function to get the system RAM. That's stupid!
    print "nope"
    
#Gets number of CPUs available for hercules
#Actually I don't know if cpu_count returns the system processors or the system cores.
def getcpu():
  
    global cpunum
    global cpunumok
  
    print "Getting CPU cores"
    if cpunumok == 0 : 
      cpunum = multiprocessing.cpu_count()
      cpunumok = 1
      print cpunum," core(s) identified"
    elif cpunumok == 1 :
      print "Warning: ",cpunum,"cores already identified"              
    else: 
      print "Value error on cpunumok status variable"
    
#Gets timezone
#positive timezones are simply n, negative ones are -n (n being hours)
#the text SHOULD be formatted later to give the +hhmm format the cnf file uses
def getzone():    

    global timezone
    global timezoneok
    
    print "Getting timezone"
    if timezoneok == 0:
      timezone = -time.timezone/60/60
      timezoneok=1
      print "timezone established to GMT ",timezone
    elif timezoneok == 1:
      print "Warning: timezone already set to ",timezone
    else:
      print "Value error on timezoneok status variable"         

#Looks for z/OS files and sets path
def getpath():
  
    #PENDING
    #no idea how to do this
    print "pending"
  
#Display fucntion. This displays the current values of the variables
#Used for test purposes. Helps displaying the variables in the menu.
def display():
  
    global memory
    global cpunum
    global timezone

    
    print "	Current configuration:"
    print "	Max. memory:	",memory," MB"
    print "	Number of CPUs:	",cpunum
    print "	Timezone:       GMT+",timezone
    
#Help function.
#I'm not even going to bother writing this until I'm done with the rest of the stuff
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
    print "pedning"
    
#This function installs hercules
#on debian
def install():
  
    cmd = ['sudo apt-get install hercules']
    
#Menu function
def menu():
    menu=0
    
    while 1 == 1 :
      #os.system('clear') #comment line so you can see the output of the set functions
      print "Hercules.cnf creator -- Achifaifa (2013) \n"
      print "1.- test getcpu()\n"
      print "2.- "
      display() #display value of variables
      print "3.- "
      print "---"
      print "9.- Help "
      print "0.- Exit \n"

    
      menu=input ("")
      
      if menu == 1:
	getcpu()
	getzone()
      elif menu == 2: 	#
	print "2"	#
      elif menu == 3:	#
	print "3"	# all these do nothing. 
      elif menu == 4:	#
	print "4"	#
      elif menu == 9:
	help()
      elif menu == 0:
	sys.exit()
      else: 
	break

#Function test space. write here variables so they display their stuff before the menu.

  #empty

#Main process (just calling menu over and over again)
while 1 == 1 :	
  menu()
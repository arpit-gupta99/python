import time
import os
import webbrowser
x="""
press 1 - To check date and timme
press 2 - To create a file
press 3 - To create a directory
press 4 - To search on google
press 5 - To log out of system
press 6 - To shut down your os
press 7 - To check your internet connection
press 8 - To login in whatsapp browser
press 9 - To check all connected ip in your network
"""
print x
option=int(raw_input("please enter your choice  "))
if option==1 :
	print"current date and time is .. "+time.ctime()
elif option==2:
	fname=raw_input("enter the file name - ")
	os.system("touch /root/Desktop/"+fname+".txt")
elif option==3:
	fname=raw_input("enter the directory name - ")
	os.system("mkdir /root/Desktop/"+fname)
elif option==4:
	srch=raw_input("enter the search item - ")
	webbrowser.open_new_tab("https://fwww.google.com/search?q="+srch)
elif option==6:
	fname=raw_input("enter the file name - ")
	os.system("shutdown")
else :
	print "invalid choice !!! "


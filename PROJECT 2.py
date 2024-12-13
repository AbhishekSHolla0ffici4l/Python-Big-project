import time
timestamp=time.strftime("%H:%M:%S")
print("The time is",timestamp)
atimestamp=int(time.strftime("%H"))
btimestamp=int(time.strftime("%M"))
ctimestamp=int(time.strftime("%S"))

if(atimestamp<=11 and btimestamp<=59):
    print("Good morning sir")
elif(atimestamp>=12 and atimestamp<=16):
    print("Good afternoon sir")
elif(atimestamp>=17 and atimestamp<=24 ):
    print("Good evening sir")
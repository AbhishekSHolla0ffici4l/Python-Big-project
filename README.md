num=int(input("give the number"))
if(num<0):
     print("The number is negetive")
elif(num>0):
  if(num<=20):
        print("Your number is between 1-20")    
  elif(num>20 and num<40):
        print("Your number is between 20-40")    
  elif(num>40 and num<60):
        print("Your number is between 40-60")    
  elif(num>60 and num<80):
        print("Your number is between 60-80")    
  elif(num>80 and num<100):
        print("Your number is between 80-100")  
#   elif(num!=int or num==str):
#     print("Invalid input!") #extra
  else:
        print ("THE NUMBER IS ABOVE 100")  
else:
    print("The number has no value\"0\"")

print("THANKS FOR USING ABHI'S PROGRAMME")   

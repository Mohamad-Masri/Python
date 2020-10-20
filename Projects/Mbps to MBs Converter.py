#1 Mbps = 0.125 MBs

print("Welcome to Data Units Conversion.")
print("Chose what you want to convert :")
print("1. Mbps to MBs.")
print("2. MBs to Mbps.")
print("")

Chose = input ("--------> ")

if Chose == "1" :
    value = 0
    value = input ("Input a Value : ")
    result = float(value) * 0.125
    print (float(value) , " Mbps = " , float(result) , " MBs")

if Chose == "2" :
    value = 0
    value = input ("Input a Value : ")
    result = float(value) / 0.125
    print (float(value) , " Mbps = " , float(result) , " MBs")
    
#else :
#    print("Please Chose a number from 1 to 2")
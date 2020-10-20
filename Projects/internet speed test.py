#Installation
#This module does not come built-in with Python. To install it type the below command in the terminal.

#pip install speedtest-cli
#After installing the above package one can check if the package is installed correctly or not by doing the version check. The version of the package can be checked using the following command

#speedtest-cli --version

# Python program to test 
# internet speed 

import speedtest 


st = speedtest.Speedtest() 

option = int(input('''What speed do you want to test: 

1) Download Speed 

2) Upload Speed 

3) Ping 

Your Choice: ''')) 


if option == 1: 

	print(st.download()) 

elif option == 2: 

	print(st.upload()) 

elif option == 3: 

	servernames =[] 

	st.get_servers(servernames) 

	print(st.results.ping) 

else: 

	print("Please enter the correct choice !") 

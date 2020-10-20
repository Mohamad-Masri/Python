# importing the library
from covid import Covid
# initializing
covid = Covid()
# printing data for the world
print("Total active cases in world:", covid.get_total_active_cases())
print("Total recovered cases in world:", covid.get_total_recovered())
print("Total deaths in world:", covid.get_total_deaths())
# getting data according to country name
# data will be stored as a dictionary
cases = covid.get_status_by_country_name("us")
# printing country's data using for loop
for x in cases:
    print(x, ":", cases[x])
    

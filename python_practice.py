# print("Hello World")

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
   # print(counties[1])
#if counties[3] != 'Jefferson':
   # print(counties[2])    

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")

#What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# 

# What is the score?
# score = int(input("What is your test score? "))

# Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else:
#     print('Your grade is an F.')

# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")
# if "Arapahoe" in counties and "El Paso" in counties:
#     print("Arapahoe and El Paso are in the list of counties.")
# else:
#     print("Arapahoe or El Paso is not in the list of counties.")
# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# for county in counties:
#     print(county)

#     # numbers = [0,1,2,3,4]
#     # for num in numbers:
#     #     print(num)

# for i in range(len(counties)):
#     print(counties[i])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# # for county in counties_dict.keys():
# #     print(county)

# # for voters in counties_dict.values():
# #     print(voters)

# for county, voters in counties_dict.items():
#     print(county,voters)

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]


# for county_dict in voting_data:

#      print(county_dict['county'])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
        

# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#     print(voting_data[i]['county'])

my_votes = int(input("How many votes did you get in the election? "))

total_votes = int(input("What is the total votes in the election? "))

print(f"I received {my_votes/total_votes*100}% of the total votes.")

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
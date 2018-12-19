# if condition:
#     action

click = True #the = is an assignment

Like = 0

if click == True: #here '=' checks for equality
    Like +=1
    click = False

# print(Like)


Temperature = 15
Thermo = 15
# print(Thermo)

if Temperature <= 15:
    Thermo = Thermo + 5

# print(Thermo)

if Temperature >= 20:
    Thermo = Thermo - 5
print(Thermo)


Time = "Day"
Sleepy = False
Pajamas = "Off"

if Time == "night" or Sleepy == True:
    Pajamas = "On"
    print(Pajamas)
elif Time == "Morning":
    Pajamas = "On"
    print(Pajamas)
else:
    print("We take off our pajamas")
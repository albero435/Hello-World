#This program takes the current time in hours between 0-23
#and the number of hours the user will wait.
#It will print what the time is in hours (between 0-23) after the user is done waiting
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait?")

#switched the name from ending with Str to Int
#idk why... it could have just been currentTime = int(input("what is the current time (in hours 0-23)?")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimeStr)



finalTimeInt = (currentTimeInt + waitTimeInt) % 23
print(finalTimeInt)

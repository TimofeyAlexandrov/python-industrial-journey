t = int(input("temp_value: "))
i = int(input("current_value: "))
overtemp = t >= 80
overcurrent = i >= 100
if overtemp and overcurrent:
    print("SHUTDOWN: thermal+overcurrent")
elif overcurrent:
    print("LIMIT_CURRENT")
elif overtemp:
    print("INCREASE_COOLING")
else:
    print("OK")

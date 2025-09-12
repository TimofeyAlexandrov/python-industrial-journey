value=int(input("sensor value: "))
if value==0:
    print("OK")
elif value==1:
    print("WARN")
elif value==2:
    print("FAIL")
else:
    print("UNKNOWN")


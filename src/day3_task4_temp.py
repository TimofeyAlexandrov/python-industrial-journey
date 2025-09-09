t = int(input("input temperature: "))
if t <= 0:
    print("COLD_START: preheat")
elif 1 <= t <= 40:
    print("NORMAL: continue")
elif 41 <= t <= 70:
    print("WARM: increase fan_speed")
else:
    print("OVERHEAT: stop_load and alarm")

import time 
while True:
    try:
        seconds = int(input("Enter the time in seconds: "))
        if seconds<1:
            print("PLease enter a number  greater than 0")
            continue
        break
    except ValueError:
        print("Invalid input , please enter a whole number")

print("\n🔔 Timer started... ")
for remaining in range(seconds, 0,-1):
    mins , secs = divmod(remaining,60)
    time_format = f"{mins:02}:{secs:02}"
    print(f"⏱️ Time left: {time_format} " , end="\r")
    time.sleep(1)

print("\nTime's up! Take a break or move on to next task. ")
print("\a") #optional makes a beep sound
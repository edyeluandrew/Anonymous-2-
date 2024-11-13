import time

def countdown_timer():

    seconds = int(input("Enter the number of seconds that you want to countdown from: "))

    print(f"Starting countdown from {seconds}...")

    while seconds > 0:

        print(seconds)

        time.sleep(1)  # Pause for 1 second

        seconds -= 1
    
    print("Time's up!")

# Call the countdown timer function

countdown_timer()


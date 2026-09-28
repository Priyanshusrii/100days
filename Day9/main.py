import time

def timee():
        try:
            minutes=int(input("Enter min:"))
            seconds=int(input("\nenter sec:"))
            if minutes<=0 or seconds<=0:
                print("enter positive time")

            return minutes *60 + seconds
        except Exception as e:
            print(e)
    
   
def countdown(total_sec):
    print("press ctrl+c to stop timer\n")
    try:
        while total_sec>0:
            minutes,seconds=divmod(total_sec,60)
            print(f" timer: {minutes:02d}:{seconds:02d}  ")
            time.sleep(1)
            total_sec-=1
        print("Time's up")
        print("\a",end="")
    except KeyboardInterrupt:
        print("timer stopped")

total_seconds=timee()
countdown(total_seconds)
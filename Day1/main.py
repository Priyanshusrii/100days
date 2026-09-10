import random as rd

num=rd.randint(1,10000)
count=5
while True:
    
    print(num)
    select=input("1.Play\n2.stop \n")
    if select.lower().strip()=="play":
        n=int(input("Guess a number!! between 1 and 10000\n"))
        if n==num:
            print("correct guess !! 🔥🔥🔥")
            replay=input("wanna play again?")
            if replay.lower().strip()=="no":
                break
            else:
                pass
                
        else:
                count-=1
                print(f"ahh sry man wrong guess\n {count} guess left ")
                if count==0:
                    print("you lose ")
                    print(f"the number was {num}")
                    print("retryss")
                    break
                elif count==1:
                    print("last chance left")

                

                
    else:
        print("okay")
        count=0
        break

            
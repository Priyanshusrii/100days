import random 


while True:
    roll=[]
    total=0
    try:
        user=int(input("How many times  you want to roll  or type 0 to exit?\n"))
        if user==0:
            break
        else:
            for d in range(user):
                r=random.randint(1,6)
                roll.append(r)
                total+=r

            print(f"Rolls:[{roll}]\nTotal:{total}") 
    except Exception as e:
        continue

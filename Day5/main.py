import  random as rd
choice= ["Rock","rock","Paper","paper","Scissor","scissor"]
user_Score=0
computer_score=0
while True: 
    
    computer=rd.choice(choice)
  
    try:
        user=input("Select\nRock , Paper ,Scissor or exit\n")

        if user in ["Rock","rock","Paper","paper","Scissor","scissor","exit"]:
            print("computer selected:",computer)
            if user=="exit":
                print(f"final score:\n user: {user_Score}\n computer: {computer_score}")
                break
            elif user == computer:
                print("Tie")
                print(f"your score : {user_Score}          Computer score : {computer_score}"     )
            elif user in ["Rock","rock"] and computer in ["Scissor","scissor"]:
                print("you win!")
                user_Score+=1
                print(f"your score : {user_Score}          Computer score : {computer_score}"     )
            elif user in ["Scissor","scissor"] and computer in ["paper","Paper"]:
                print("you win!")
                user_Score+=1
                print(f"your score : {user_Score}          Computer score : {computer_score}"     ) 
            elif user in ["Paper","paper"] and computer in ["Rock","rock"]:
                print("you win!")
                user_Score+=1
                print(f"your score : {user_Score}          Computer score : {computer_score}"     )
            elif user in ["Scissor","scissor"] and computer in ["Rock","rock"]:
                            print("you lose!")
                            computer_score+=1
                            print(f"your score : {user_Score}          Computer score : {computer_score}"     ) 
            elif user in ["paper","Paper"] and computer in ["Scissor","scissor"]:
                            print("you lose!")
                            computer_score+=1
                            print(f"your score : {user_Score}          Computer score : {computer_score}"     ) 
            elif user in ["Rock","rock"] and computer in ["paper","Paper"]:
                            print("you lose!")
                            computer_score+=1
                            print(f"your score : {user_Score}          Computer score : {computer_score}"     )
            else:
                    continue
    except Exception as e:
            print(e)
                      

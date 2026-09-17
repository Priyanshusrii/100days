file="expense.txt"
def load_file():
    expense=[]
    try:
        with open(file,'r') as filee:
            for l in filee:
                l=l.strip()
                if not l:
                    continue
                category,amount=l.split("|")
                exp={
                    "Category":category,
                    "Amount":int(amount)
                } 
                expense.append(exp)
    except:
        with open(file,"w") as f:
            pass
           
            
    return expense
        
def save_expense(expense):
    if not file:
        raise Exception
    with open(file,"w") as filee:
        for exp in expense:
            filee.write(f"{exp['Category']}|{exp['Amount']}\n")



def add_expense(expense):
    try:
        category=input("enter category\n")
    except Exception as e:
        print(e)
        return

    try:
        amount=int(input("enter amount:"))
    except ValueError as e:
        print(e)  
        return  
    
    exp={
        "Category":category,
        "Amount":amount
    } 
    expense.append(exp)
    save_expense(expense)
    print("added successfully")

def view_expense(expense):
    if not expense:
        print("no expense record!")
        return
    else:
        for exp in expense:
            print((f"{exp['Category']}|{exp['Amount']}\n"))
def total(expense):
    if not expense:
        print("no expense!!")
        return
    summ=0
    for i in expense:
        summ=summ+i["Amount"]

    print("===================================")
    print("total=",summ)
    print("===================================")
expense=load_file()
while True:
    choice=int(input("select option\n 1:Add expense\n 2:View expense\n 3:Total expenses\n 4:Exit\n"))
    if choice==1:
        add_expense(expense)
    elif choice==2:
        view_expense(expense)
    elif choice==3:
        total(expense)
    elif choice ==4:
        break
    else:
        print("select from given option pls")
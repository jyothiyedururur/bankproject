login=[224452,224453,224454]
pas=[123,456,789]
account=[100,200,300]
email=["jyothi@gmail.com","krishna@gmail.com","babu@gmail.com"]
phone=[8247883411,9000082748,6305620375]
def signup(l,p,el,ph):
        
    return "sign up successful"
def em(el):
    while(True):
        if '@' in el:
            email.append(el)
            break
        else:
            print("enter correct format")
            el=input("enter email")
    
def pw(ph):
    while True:
        n=str(ph)
        if(len(n)==10):
            phone.append(ph)
            break
        else:
            print("enter exactly 10 digits")
            ph=int(input("enter correct number"))
def log(l):
    while True:
        if l in login:
            print("account number already existed")
            l=int(input("enter another account number"))
        else:
            break
        
def paw(p):
    numbers = '0123456789'
    symbols = '!#$%&()*+'
    small_a = 'abcdefghijklmnopqrstuvwxyz'
    cap_a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while True:
        
        num_count = sum(1 for char in p if char in numbers)
        sym_count = sum(1 for char in p if char in symbols)
        small_a_count = sum(1 for char in p if char in small_a)
        cap_a_count = sum(1 for char in p if char in cap_a)
        
        if num_count >= 0 and sym_count >= 0 and small_a_count >= 0 and cap_a_count >= 0:
            break
        else:
            print("Password must contain at least 2 numbers, 2 lowercase letters, 2 uppercase letters, and 2 special symbols.")
            p = input("Enter correct password: ")
    while(True):
         c=input("conform the password")
         if(c==p):
            pas.append(p)
            break
         else:
            print("password not matched")
            c=input("conform password") 
    
    
while(True):
    mch=input("do you want login or signup")
    if(mch=="login"):
        account_number=int(input("enter your account number"))
        if account_number in login: 
                password=int(input("enter password"))
                d=login.index(account_number)
                if password==pas[d]:
                    print("login sucessfull")
                    #bank management system
                    while(True):
                        choice=input("enter you choice in \n withdraw\n deposit \n check balance \n logout\n")
                        if(choice=="withdraw"):
                            wa=int(input("enter the amount you want to withdraw"))
                            if(wa>account[d]):
                                print(" you don't have enough balance")
                            else:
                                print("withdraw successful")
                                account[d]-=wa
                        elif(choice=="deposit"):
                            addm=int(input("enter the amount you want to deposit"))
                            account[d]+=addm
                            print("successfully deposited")
                        elif(choice=="check balance"):
                            print(account[d])
                        elif(choice=="logout"):
                            break
                        else:
                            print("choose correct option")

                else:
                    print("invalid password")
        else:
                print("account number not existed")
    elif(mch=="signup"):
         l=int(input("enter your account number"))
         log(l)
         p = input("Enter a password: ")
         paw(p)
         el=input("enter your email")
         em(el)
         ph=int(input("enter your phone number"))
         pw(ph)
         account.append(0)
         print(signup(l,p,el,ph))
    else:
        print("choose correct option")
    '''a=0
    b=0
    c=0
    d=0
    for i in range(len(p)):
        if p[i] in numbers:
            a+=1
            print(a)
        if p[i] in symbols:
            b+=1
            print(b)
        if p[i] in small_a:
            c+=1
            print(c)
        if p[i] in cap_a:
            d+=1
            print(d)
    while True:
        if a>0 and b>0 and c>0 and d>0:
            break
        else:
            print("enter at least 2 numbers and  2 small alphabets and atleast 2 uppercase letters ,and include atleast 2 special symbolls")
            p=input("enter correct format")
     '''
    
        
            

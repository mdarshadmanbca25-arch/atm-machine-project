print('welcome to the sbi atm')
pin=1234
amount=100
insert_card=input('insert your card')
if insert_card=="card":
    print('welcome again')
    user_pin=int(input('enter the pin'))
    if user_pin==pin:
       print('1)check balance\n2)withdrawl')
       user_selection=int(input('select the option'))
       if user_selection==1:
           print('your balance is ',amount)
       elif user_selection==2: 
            user_amount=int(input('enter the amount'))   
            print('your balance',amount-user_amount)
       else:
           print('invalid selction')
    else:
        print('invalid card')             

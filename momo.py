name = 'Twizerimana olivier'
phone = 785273109
pin = 12345

class Momo():
    def __init__(self,user,phone_number, pin):
        self.user = name
        self.phone_number = phone
        self.pin = pin

    def displayWelcome(self):
        print('Welcome dear')
        return self.user
mm = Momo(name, phone, pin)
print(mm.displayWelcome())
ussd = input('USSD: ')
if ussd == '*182#':

    print('Notification')
    print(' ')
    print('''
    1. Send Money
    2. Buy
    3. Pay Bill
    4. Bank Services
    5. Loans and Saving
    6. My MoMo Account
    7. Pending Approvals
    8. MoMoPay
    9. My MoMo Security
    10. Insurance
    11. MoMo Terms and Conditions
    12. Macye Macye
    13. Babyl Health
    14. Help
    15. Exit
    ''')
else:
    print('External Application Down')
    
while True:
    choice = input('>> ')
    if choice == '6':
        print('''
        
        1. Check Balance
        2. Mini Statement
        3. Get Latest Electricity Token
        4. Preapprove Treansactions
        5. Change Language
        6. My Offers
        7. Exit
        0. Back
        ''')
        choose = int(input('> '))
        if choose == 1:
            confirm_pin = int(input('To confim to get Balance, Enter MM PIN: '))
            if confirm_pin == pin:
                print('''

                      Your balance is $3,000,450 and Welcome
                      account balance is-. Thank you for using mobile money
''')
            else:
                print('Wrong PIN 5 times your account will be blocked.')

    else:
        print('Exaternal application down')
        break

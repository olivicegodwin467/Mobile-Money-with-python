class Momo():
    def __init__(self,user,phone_number):
        pass
ussd = input('>> ')
while True:
    if ussd == '*182#':

        print('Notification')
        print(' ')
        print('''
        1. Kohereza Amafranga
        2. Kugura
        3. Kwishyura
        4. Serivisi za Bank
        5. Inguzanyo no kuzigama
        6. Konti Yanjye ya MoMo
        7. Ibyemezo bitaranozwa
        n Next
        ''')

        next = input('>> ')
        if next == 'n':
            
            print('''
            8. MoMoPay
            9. Sekirite Yanjye ya MoMo
            10. Ubwishingizi
            11. Amategeko namabyiriza bya MoMo
            12. Macye Macye
            13. Babyl Health
            14. Bariza Hano
            15. Sohokamo
            ''')

    choice = input('>> ')
    if choice == '6':
        print('''
        
        1. Kureba Asigaye
        2. Raporo ngufi
        3. Kubona Imibare ya Cash power iherutse
        4. Preapproved Transactions
        5. Guhindura ururimi
        6. My Offers
        ''')
    else:
        print('Exaternal application down')
    print('')

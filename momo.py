import os
import sqlite3

os.system("color a")
my_list = []

class User_info:
    # Display menu
    def menu(self):
        while True:
            print("""
                Welcome to our system.
                
                1. Register
                2. Login
                3. Display user accounts
                4. Search person
                5. Delete person
                6. Use mobile money
                7. Exit
    """)
            choice = int(input("Enter your choice.\n>> "))
            if choice == 1:
                self.register()
            elif choice == 2:
                self.login()
            elif choice == 3:
                self.display_accounts()
            elif choice == 4:
                self.search_person()
            elif choice == 5:
                self.delete_person()
            elif choice == 6:
                self.use_mobile_money()
            elif choice == 7:
                exit()

    # Register users
    def register(self):
        global my_list
        item = int(input("How many people do you want to add to the database?\n>> "))
        for i in range(item):
            id = i + 1
            name = input(f"Enter the name {i + 1}\n>> ")
            age = int(input(f"Enter the age for {name}\n>> "))
            profession = input(f"Enter the profession for {name}\n>> ")
            location = input(f"Enter the location for {name}\n>> ")
            phone_number = input(f"Enter the Phone number for {name}\n>> ")
            email = input(f"Enter the email for {name}\n>> ")

            # Create a tuple and add it to the list
            new_item = (id, name, age, profession, location, phone_number, email)
            my_list.append(new_item)

        # Save to the database
        self.save_to_database(my_list)

    # Save data to the database
    def save_to_database(self, data):
        conn = sqlite3.connect("my_db.db")
        cursor = conn.cursor()

        # Create table if it doesn't exist
        sql_query1 = """
        CREATE TABLE IF NOT EXISTS account(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            profession TEXT NOT NULL,
            location TEXT NOT NULL,
            phone_number TEXT NOT NULL,
            email TEXT NOT NULL
        )
        """
        cursor.execute(sql_query1)

        # Insert data
        sql_query2 = "INSERT INTO account(id, name, age, profession, location, phone_number, email) VALUES(?,?,?,?,?,?,?)"
        for item in data:
            cursor.execute(sql_query2, item)
        conn.commit()
        conn.close()
        print("Data inserted into database correctly!")

    # Display all user accounts
    def display_accounts(self):
        conn = sqlite3.connect("my_db.db")
        cursor = conn.cursor()

        # Fetch data
        cursor.execute("SELECT * FROM account")
        data = cursor.fetchall()
        conn.close()

        # Display the data
        if data:
            print("User Accounts:")
            for row in data:
                print(row)
        else:
            print("No user accounts found.")

    # Placeholder functions for other menu options
    def login(self):
        print("Login feature not implemented yet.")

    def search_person(self):
        print("Search person feature not implemented yet.")

    def delete_person(self):
        print("Delete person feature not implemented yet.")

    def use_mobile_money(self):
            ussd = input('Key> ')
            if ussd == "momo":

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
                        pin = "0000"
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
user = User_info()
# Main entry point
if __name__ == "__main__":
    user.menu()


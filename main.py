from banks import Bank
from users import User,Admin

BDBL_bank=Bank("BDBL")

def user_menu(user,bank):

  while True:
    print(f"\n\tWelcome {user.name} to {bank.bank_name.upper()} Bank\n")
    print("1. Check Balance")
    print("2. Deposite Money")
    print("3. Withdraw Money")
    print("4. Show Transaction History.")
    print("5. Take Loan")
    print("6. Transfer Money")
    print("7. My Account Information")
    print("8. Logout")

    option=int(input("\nEnter A Option : "))

    if option==1:
      print(f"\nYou have {user.balance}.00 Taka Only\n")
    elif option==2:
      amount=int(input("\nEnter Amount : "))
      user.deposite(amount)
    elif option==3:
      amount=int(input("\nEnter Amount : "))
      user.withdraw(amount)
    elif option==4:
      print(f"\n\tYour Transactions\n")
      user.transaction_history()
    elif option==5:
      user.take_loan(user)
    elif option==6:
      recipient_account_number=int(input("\nEnter Recipient Number : "))
      amount=int(input("\nEnter Amount : "))
      if amount<=user.balance:
        user.transfer_money(recipient_account_number,amount)
      else:
        print(f"\nYou don't have enough balance")
    elif option==7:
      user.account_info()
    elif option==8:
      break
    else:
      print("\n!!!! ( Invalid Option ) !!!!\n")



def admin_menu(admin,bank):
  while True:
    print(f"\n\t***.. Welcome Admin {admin.name} ..***\n")
    print("1. Create An Account")
    print("2. Delete An Account")
    print("3. Show All Account")
    print("4. Total Balance of The Bank")
    print("5. Total Loan of The Bank")
    print("6. Trun ON Loan Feature")
    print("7. Trun OFF Loan Feature")
    print("8. Logout")

    option=int(input("\nEnter A Option : "))

    if option==1:
      name=input("\nEnter Name : ")
      email=input("Enter Email : ")
      address=input("Enter Address : ")
      user=User(name=name,email=email,address=address,bank=bank)
      user.create_account()
      print(f"\nAccount Created by ADMIN {admin.name}" )

    elif option==2:
      acc_number=int(input("\nEnter Account Number : "))
      admin.bank.delete_account(acc_number)
    elif option==3:
      admin.bank.show_accounts
    elif option==4:
      balance=admin.bank.calculate_total_bank_balance()
      print(f"\nTotal Bank Balance : {balance} Taka")
    elif option==5:
     loan= admin.bank.calculate_total_bank_loan()
     print(f"\nTotal Bank Loan : {loan} Taka")

    elif option==6:
      command=True
      admin.bank.toggle_loan_feature(command)
    elif option==7:
      command=False
      admin.bank.toggle_loan_feature(command)
    elif option==8:
      break
    else:
      print("\n!!!! ( Invalid Option ) !!!!\n")

while True:
  print("\n\t.. Welcome ..")
  print("\n1. Create Account & Login")
  print("2. Login To Your Account")
  print("3. Create Admin & Login")
  print("4. Admin Login")
  print("5. Exit")

  option=int(input("\nEnter A Option : "))

  if option==1:
    name=input("\nEnter Your Name : ")
    email=input("Enter Your Email : ")
    address=input("Enter Your Address : ")
    user=User(name=name,email=email,address=address,bank=BDBL_bank)
    print("\nCreating Account Please Wait .....")
    user.create_account()
    user_menu(user,BDBL_bank)

  elif option==2:
    username=input("\nEnter Your Name : ")
    email=input("Enter  Email : ")
    current_user=BDBL_bank.login_user(username,email)

    if current_user is not None:
      user_menu(current_user,BDBL_bank)

  elif option==3:
    name=input("\nEnter Admin Name : ")
    email=input("Enter Admin Email : ")
    address=input("Enter Admin Address : ")
    admin=Admin(name=name,email=email,address=address,bank=BDBL_bank)
    admin.bank.admins.append(admin)
    print("\nCreating Admin Please Wait .........")
    admin_menu(admin,BDBL_bank)

  elif option==4:
    username=input("\nEnter Admin Name : ")
    email=input("Enter Email : ")
    current_admin=BDBL_bank.login_admin(username,email)
    if current_admin is not None:
      admin_menu(current_admin,BDBL_bank)
  elif option==5:
    break
  else:
    print("\n!!!! ( Invalid Option ) !!!!\n")



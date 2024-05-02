
class Bank():
  def __init__(self,bank_name):
    self.admins=[]
    self.accounts=[]
    self.bank_name=bank_name
    self.loan_status=True
    self.total_loan=self.calculate_total_bank_loan()
    self.total_balance=self.calculate_total_bank_balance()

  def calculate_total_bank_balance(self):
    total=0
    for account in self.accounts:
      total+=account.balance
    self.total_balance=total
    return total

  def calculate_total_bank_loan(self):
    total_loan=0
    for account in self.accounts:
      total_loan+=account._loan["loanAmount"]
    self.total_loan=total_loan
    return total_loan

  def toggle_loan_feature(self,command):
    if command is True:
      self.loan_status=True
      print("\nLoan Feature Turned ON")
    else:
      self.loan_status=False
      print("\nLoan Feature Turned OFF")

  def give_loan(self,amount,account):
    print(f"\n{amount} Taka Loan Given to {account.name}")

  def login_user(self,username,email):
    userAccount=None
    for account in self.accounts:
      if account.name == username and account.email == email:
        userAccount=account
    if userAccount is not None:
      print(f"\n{userAccount.name} Logged In Successfully")
      return userAccount
    else:
      print(f"\n{username} is not a valid user")
      return None

  def login_admin(self,username,email):
    adminAccount=None
    for admin in self.admins:
      if admin.name == username and admin.email == email:
        adminAccount=admin
    if adminAccount is not None:
      print(f"\n{adminAccount.name} Admin Logged In Successfully")
      return adminAccount
    else:
      print(f"\n****( {username} is Not An Admin )****")
      return None

  def create_account(self,user):
    print(f"\n\t..( Select Account Type )..\n")
    print(f"1.) Savings Account")
    print(f"2.) Current Account")
    account_type=int(input())
    if account_type==1:
      user.account_type="Savings"
    elif account_type==2:
      user.account_type="Current"
    else:
      user.account_type="Savings"
    self.accounts.append(user)
    print (f"\nAccount Created Successfully")

  def delete_account(self,acc_number):
    account=self.find_account(acc_number)
    if account is not None:
      self.accounts.remove(account)
      print(f"\nAccount Deleted Successfully")
    else:
      print(f"\n****( Account Does Not Exist )****")

  def show_account_info(self,account):
    print(f"\n\t( Account Information )\n")
    print(f"Name : {account.name}\nAccount Number : {account._account_number}\nAccount Type : {account.account_type}\nBalance : {account.balance}")
  @property
  def show_accounts(self):
    print(" {:10} {:<20}{:10} {:15} {:15} {:10}".format(" Name","Email","Address","Account Number","Account Type","Balance\n"))
    for account in self.accounts:
      print(" {:10}| {:<20}| {:10}| {:<10}| {:15}| {:<10}".format(account.name, account.email,account.address, account._account_number,account.account_type,account.balance))


  def find_account(self,account_number):
    userAccount=None
    for account in self.accounts:
      if account._account_number==account_number:
        userAccount=account
    return userAccount

  def transfer_money_to_account(self,rec_acc,amount,your_acc):

    account=self.find_account(rec_acc)

    if account is None:
      print(f"\n****( Account Does Not Exist )****")
    else:
      account.deposite(amount)
      myAccount=self.find_account(your_acc)
      myAccount.withdraw(amount)
      print(f"\n{amount} Taka Transfered to Account {account.name}")





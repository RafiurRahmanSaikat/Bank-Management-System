import random
from abc  import ABC
from datetime import datetime


class User(ABC):
  def __init__(self,name,email,address,bank,):
    self.name = name
    self.email = email
    self.address = address
    self.bank=bank # Bank Class With All Methods
    self.__balance=0
    self._account_number=random.randint(10000,99999)
    self._transaction_history=[]
    self._loan={"loanCount":0,"loanAmount":0}

  def create_account(self):
    self.bank.create_account(self)

  def take_loan(self,amount):
    if self._loan["loanCount"] <2 and self.bank.loan_status is True:
      amount=int(input(f"\nEnter Amount : "))
      self.bank.give_loan(amount,self)
      self._loan["loanCount"]+=1
      self._loan["loanAmount"]+=amount
      self.__balance+=amount
      self._transaction_history.append(f"{amount}    TK Loaned at {datetime.now()}")

    else:
      print(f"\n\t*****( You Can't Take Loans )*****")

  @property
  def balance(self):
    return self.__balance

  @balance.setter
  def balance(self,value):
    self.__balance=value

  def deposite(self,amount):
    if amount > 0:
      self.__balance += amount
      self._transaction_history.append(f"{amount}    TK Credited at {datetime.now()}")
      print(f"\n{amount} Taka Credited Successfully !")
    else:
      print(f"\n{amount} Negtive Amount Cannot Be Credited")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__balance:
      self.__balance -= amount
      self._transaction_history.append(f"{amount}    TK Debited at {datetime.now()}")
      print(f"\n{amount} Taka Debited Successfully !")
    elif amount>self.__balance:
      print(f"\nWithdrawal Amount Exceeded")
    else:
      print(f"\nThe Bank is Bankrupt !!.")

  def transaction_history(self):
    for transaction in self._transaction_history:
      print(transaction)

  def account_info(self):
    self.bank.show_account_info(self)

  def transfer_money(self,recipient_account_number,amount):
    self.bank.transfer_money_to_account(recipient_account_number,amount,self._account_number)





class Admin(ABC):
   def __init__(self,name,email,address,bank):
    self.name = name
    self.email = email
    self.address = address
    self.bank=bank






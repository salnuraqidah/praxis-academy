class Deposit:
	deposit = 0

	def __init__(self):
		print()

	def setDeposit(self,d):
		Deposit.deposit = d

	def getDeposit(self):
		return deposit

class Withdraw:
	withdraw = 0

	def __init__(self):
		print()

	def setWithdraw(self,w):
		Withdraw.withdraw = w

	def getWithdraw(self):
		return withdraw

class BalanceInquiry:
	balance = 0

	def __init__(self):
		print()


	def setBalance(self,b):
		BalanceInquiry.balance = b

	def getBalance(self):
		return balance

class ATMMachine(Deposit,Withdraw,BalanceInquiry):
		
	def __init__(self):
		select = 0
		choice = 0

		print(50*"=")
		print("\tWelcome to this Simple ATM machine")
		print()

		while True:
			try:

				print(50*"=")
				print("\tPlease select ATM Transactions")
				print(50*"=")
				print("\tPress [1] Deposit")
				print("\tPress [2] Withdraw")
				print("\tPress [3] Balance Inquiry")
				print("\tPress [4] Exit")

				select=int(input("\n\tWhat would you like to do?"))


				if select==1 :
					print("\n\tEnter the amount of money to deposit: ")
					Deposit.deposit = int(input(""))
					BalanceInquiry.balance = Deposit.deposit + BalanceInquiry.balance
					print("\tYou deposited the amount of Rp" , Deposit.deposit)
					print(BalanceInquiry.balance)

					
				elif select==2 :
					print("\n\tTo withdraw, make sure that you have sufficient balance in your account.")
					print("\tEnter amount of money to withdraw: ")
					Withdraw.withdraw = int(input(""))
					BalanceInquiry.balance = BalanceInquiry.balance - Withdraw.withdraw
					
					if BalanceInquiry.balance == 0 :
						print("\tYour current balance is zero.")
						print("\tYou cannot withdraw!")
						print("\tYou need to deposit money first")
					
					elif BalanceInquiry.balance <= 500:
					 	print("\tYou do not have sufficient money to withdraw")
					 	print("\tChecked your balance to see your money in the bank")

					elif Withdraw.withdraw > BalanceInquiry.balance:
					 	print("\tThe amount you withdraw is greater than your balance")
					 	print("\tPlease check the amount you entered")
					
					elif Withdraw.withdraw < BalanceInquiry.balance:
						BalanceInquiry.balance = BalanceInquiry.balance - Withdraw.withdraw
						print("\n\tYou withdraw the amount of Rp", Withdraw.withdraw)

				elif select==3 :
					print("\tYour current balance is Rp" , BalanceInquiry.balance)

				elif select==4 :
					print("\n\tTransaction exited")
					break
					

				else :
					print("\n\tPlease select correct transaction.")

				try :
					print("\n\tWould you like to try another transaction?")
					print("\n\tPress [1] Yes \n\tPress [2] No")
					choice = int(input("\tEnter choice: "))

					if choice == 1 :
						continue

					elif choice == 2 :
						break
					else:
						print("\n\tPlease select correct choice")

				except:
					print("\tError Input! Please enter a number only")				
					choice =int(input("\tEnter your choice :"))
		
			except:
				print("\tError Input! Please enter a number only")				
				choice =int(input("\tEnter your choice :"))




atm=ATMMachine()                    

print("\n\tThank you for using this simple ATM Machine.")




			
			



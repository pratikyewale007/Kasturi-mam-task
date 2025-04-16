class Bank:
    ROI = 10.5 
    def __init__(self):
        self.Name = ''
        self.Amount = 0
        self.Address = ''
        self.AccountNo = 0

    def CreateAccount(self):
        self.Name = input('Enter Name: ')
        self.Amount = int(input('Enter Amount: '))
        self.Address = input('Enter Address: ')
        self.AccountNo = int(input('Enter Account Number: '))

    def DisplayMethod(self):
        print('===Your Account Details===')
        print('Account Holder Name:', self.Name)
        print('Account Holder Amount:', self.Amount)
        print('Account Holder Address:', self.Address)
        print('Account Holder Account Number:', self.AccountNo)

    def Withdraw(self):
        withdraw = input('Do you want to Withdraw Amount? (y/n): ')
        if withdraw.lower() == 'y':
            amount = int(input('Enter the Amount u want to Withdraw: '))
            if amount<self.Amount:
                self.Amount -= amount
                print('Amount Withdrawn:', amount)
                print('Updated Balance :', self.Amount)
            else:
                print('Insufficient Balance', self.Amount)
        else:
            print('Thank You')
            
    def Deposit(self):
        deposit = input("Do u want to deposit the money (y/n) :")
        if deposit.lower() == 'y':
            amount = int(input("How much money u wanna deposit: "))
            self.Amount += amount
            print('Amount Deposited:', amount)
            print('Updated Balance:', self.Amount)
        else:
            print('Thank You')

    def Interest(self):
        interest = (self.Amount * Bank.ROI) / 100
        print('Interest on your account:', interest)
        self.Amount += interest
        print('Updated Balance after Interest:', self.Amount)

def main():
    user1= Bank()

    print('===Creating First Account===')
    user1.CreateAccount()
    user1.DisplayMethod()
    user1.Interest()
    user1.Withdraw()
    user1.Deposit()
    

if __name__ == '__main__':
    main()
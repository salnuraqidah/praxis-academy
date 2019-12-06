class atm:

    def __init__(self,deposit):
        self.deposit = deposit
     
    def saldo(self):
        print('Saldo ATM Anda Rp', self.deposit)
        
        
    def pinIn(self):
        pin=input('masukan pin anda : ')
        if pin == '123456':
            self.saldo()

        else:
            while pin != 123456:
                print("Pin yang anda masukkan salah")
                self.pinIn()
                break

a=atm(1000000)
a.pinIn()
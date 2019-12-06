class deposit:
    def __init__(self, depo):
        self.depo = depo

    def depos():
    	saldo='1000000'
        print('saldo anda adalah Rp', saldo)
        return

    def input_pin(self):
        pin=input('masukan pin anda : ')
        if pin == '123123':
            self.depos()
        else:
            while pin != 123123:
                print("Pin yang anda masukkan salah")
                self.input_pin()
                break

                	
# pinAtm = input('Masukkan Pin ATM Anda :')
# if pinAtm == '123456':
# 	saldo = int(1000000) 

# else:
# 	while pinAtm != 123456:
# 		print('Pin Anda Salah')
# 		break

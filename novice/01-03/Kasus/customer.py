class customer:
    def __init__(self, name, idNum, phoneNum):
        self.name = name
        self.idNum = idNum
        self.phoneNum = phoneNum

    def dataDiri(self):
    	print('Nama Lengkap :', self.name)
    	print('NIK :', self.idNum)
    	print('No HP :', self.phoneNum)

nama = input('Nama Lengkap :')
nik = input('NIK :')
hp = input('No hp :')    	
########
class reservation:
    def __init__(self, dateIn, duration, amountCust):
        self.dateIn = dateIn
        self.duration = duration
        self.amountCust = amountCust

    def dataReserv(self):
    	print('Tanggal Check-in :', self.dateIn)
    	print('Durasi :', self.duration)
    	print('Banyak tamu :', self.amountCust)

dur=input('durasi : ')
tamu=input('tamu :')
###########3
class payment:
    def __init__(self, total):
        self.total = total
    def totalHarga(self):
    	print('Total Rp.', self.total)
harga = int(dur)*int(tamu)*100000 #duration*amountCust*100000
c = payment(harga)
c.totalHarga()
####
import random
class virtualAcc:
    def __init__(self, noVA):
        self.noVA = noVA
    def numVA(self):
    	print('Silahkan melakukan pembayaran dengan No Virtual Account', self.noVA)
va = random.random() 
c = virtualAcc(va)
c.numVA()

print('Pembayaran berhasil')
print('Review Reservation')

a = customer(nama,nik,hp)
a.dataDiri()

b = reservation('03-01-2020',dur,tamu)
b.dataReserv()

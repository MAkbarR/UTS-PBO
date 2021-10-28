class saldo:
    def __init__(self, saldoumum, saldotab,nominal, hasil1, hasil2, kurang1, kurang2):
        self.saldoumum = saldoumum
        self.saldotab = saldotab
        self.nominal = nominal
        self.hasil1 = hasil1
        self.hasil2 = hasil2
        self.kurang1 = kurang1
        self.kurang2 = kurang2

    def printname(self):
        print(self.saldoumum)
        print(self.saldotab)
        print(self.nominal)
        print(self.hasil1)
        print(self.hasil2)
        print(self.kurang1)
        print(self.kurang2)

class info(saldo):
    def __init__(self, saldoumum, saldotab, nominal, hasil1, hasil2):
        saldo.__init__(self, saldoumum, saldotab, nominal, hasil1, hasil2) 
        self.saldoumum = "0"
        self.saldotab = "0"

    def psaldo(self):
        print("Saldo Umum Anda Saat ini Berjumlah ",self.saldoumum )
        print("Saldo Tabungan Anda Saat ini Berjumlah ",self.saldotab)

    
class tambah(saldo):
    def __init__(self, saldoumum, saldotab, nominal, hasil1, hasil2 ):
        saldo.__init__(self, saldoumum, saldotab, nominal, hasil1, hasil2)
        self.hasil1=self.saldoumum+self.nominal 
        self.hasil2=self.saldotab+self.nominal
    

class ambil(saldo):
    def __init__(self, saldoumum, saldotab, hasil):
        saldo.__init__(self, saldoumum, saldotab, hasil)
        self.kurang1=self.saldoumum-self.nominal
        self.kurang2=self.saldotab-self.nominal

class Intro:
    def ppp(self):
        print("""** Selamat Datang Di Aplikasi Pencatatan Uang Digital **
            1. Informasi Saldo
            2. Tambah Saldo 
            3. Ambil Saldo 
            0. Keluar 
        
        """)
    

obj_Intro = Intro()
obj_Info = info()


obj_Intro.ppp()
option=int(input("Silahkan Pilih menu : "))
if option==1:
    obj_Info.psaldo()
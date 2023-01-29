#import library yang digunakan
from tabulate import tabulate


#Buat class yang akan digunakan
class Transaksi :
    #Function untuk membuat dict
    def __init__ (self) :
        self.data_trans = dict()
    
    #Function untuk menambahkan item belanja
    def add_item (self, nama_item, jum_item, hrg_item):
        """
            Function ini digunakan untuk menambahkan item belanja.
            
            Mempunyai Parameter :
            nama_item : value berupa str, digunakan untuk menampung nilai nama item
            jum_item : value berupa int, digunakan untuk menampung nilai quantity item
            hrg_item : value berupa int, digunakan untuk menampung nilai harga item
        """
        self.data_trans.update({nama_item : [jum_item, hrg_item, (jum_item*hrg_item)]}) #Menambahkan data kedalam dict
        print("*** Pesanan Anda Berhasil Dimasukan Ke Keranjang ***") #Menampilkan pesan ini jika berhasil
        print("\n")
            
        return self.check_order() #Menampilkan list item
    
    #Function untuk mengupdate nama item belanja
    def update_nama_item (self, nama_item, updt_nama_item):
        """
            Function ini digunakan untuk mengganti nama item belanja.
            
            Mempunyai Parameter :
            nama_item : value berupa str, digunakan untuk menampung nilai nama item
            updt_nama_item : value berupa str, digunakan untuk menampung nilai perubahan nama item
        """
        try: #Jika value benar maka akan
            self.data_trans[updt_nama_item] = self.data_trans.pop(nama_item) #Mengganti nama item
            
            print("*** Data Anda Telah Berhasil Diupdate ***") #Menampilkan pesan ini jika berhasil
            print("\n")
            
            return self.check_order() #Menampilkan list item
        except:
            print ("*** Terdapat Kesalahan Pada Input, Silahkan Cek Kembali !!! ***") #Menampilkan pesan ini jika gagal
    
    #Function untuk mengupdate quantity item belanja
    def update_qty_item (self, nama_item, updt_jum_item):
        """
            Function ini digunakan untuk mengganti quantity item belanja.
            
            Mempunyai Parameter :
            nama_item : value berupa str, digunakan untuk menampung nilai nama item
            updt_jum_item : value berupa int, digunakan untuk menampung nilai perubahan jumlah item
        """
        try: #Jika value benar maka akan
            self.data_trans[nama_item][0] = updt_jum_item #Mengganti jumlah item
            self.data_trans[nama_item][2] = updt_jum_item*self.data_trans[nama_item][1] #Mengganti total harga item
            
            print("*** Data Anda Telah Berhasil Diupdate ***") #Menampilkan pesan ini jika berhasil
            print("\n")
            
            return self.check_order() #Menampilkan list item
        except:
            print ("*** Terdapat Kesalahan Pada Input, Silahkan Cek Kembali !!! ***") #Menampilkan pesan ini jika gagal
            
    #Function untuk mengupdate harga item belanja
    def update_hrg_item (self, nama_item, updt_hrg_item):
        """
            Function ini digunakan untuk mengganti harga item belanja.
            
            Mempunyai Parameter :
            nama_item : value berupa str, digunakan untuk menampung nilai nama item
            updt_hrg_item : value berupa int, digunakan untuk menampung nilai perubahan harga item
        """
        try: #Jika value benar maka akan
            self.data_trans[nama_item][1] = updt_hrg_item #Mengganti jumlah item
            self.data_trans[nama_item][2] = self.data_trans[nama_item][0]*updt_hrg_item #Mengganti total harga item
            
            print("*** Data Anda Telah Berhasil Diupdate ***") #Menampilkan pesan ini jika berhasil
            print("\n")
            
            return self.check_order() #Menampilkan list item
        except:
            print ("*** Terdapat Kesalahan Pada Input, Silahkan Cek Kembali !!! ***") #Menampilkan pesan ini jika gagal
            
    #Function untuk menghapus item belanja
    def dlt_item (self, nama_item):
        """
            Function ini digunakan untuk menghapus item belanja tertentu.
            
            Mempunyai Parameter :
            nama_item : value berupa str, digunakan untuk menampung nilai nama item
        """
        try: #Jika value benar maka akan
            self.data_trans.pop(nama_item)#Menghapus item belanja tertentu
            
            print("*** Data Anda Telah Berhasil Diupdate ***") #Menampilkan pesan ini jika berhasil
            print("\n")
            
            return self.check_order() #Menampilkan list item
        except:
            print ("*** Terdapat Kesalahan Pada Input, Silahkan Cek Kemabali !!! ***")
            
    #Function untuk mereset transaksi
    def rst_trans (self):
        """
            Function ini digunakan untuk menghapus transaksi.
        """
        try: #Jika value benar maka akan
            self.data_trans.clear()#Reset transaksi
            
            print ("Selamat, Transaksi Anda Berhasil Direset Kembali")
        except:
            print ("*** Terdapat Kesalahan Pada Input, Silahkan Cek Kemabali !!! ***")
    
    #Function untuk cek transaksi
    def check_order(self):
        """
            Function ini digunakan untuk menampilkan semua item belanja.
        """
        try: #Jika value benar maka akan
            table = []
            #Menambahkan data dict ke dalam list table
            for key, val in self.data_trans.items():
                tmp = []
                tmp.append(key)
                
                for i in val:
                    tmp.append(i)
                    
                table.append(tmp)
            
            header = ['Nama Item', 'Jumlah Item', 'Harga Item', 'Total Harga']
            print("*** Belanjaan Anda ***")
            print("")
            print((tabulate(table, header, tablefmt="github")))
            
        except:
            print ("*** Terdapat Kesalahan Pada Transaksi Anda, Silahkan Cek Kemabali !!! ***")

    def ttl_price(self):
        """
            Function ini digunakan untuk menampilkan total harga transaski dan memberikan diskon 
            jika user memenuhi kriteria tertentu.
        """
        
        #Menampilkan list item
        self.check_order()
        print("")
        
        #Jumlah total harga transaksi
        total = 0
        for key, val in self.data_trans.items():
            total += self.data_trans[key][2]
        
        # pengecekan diskon
        if total > 500_000:
            total_baru = total * 0.90
            print("Anda mendapatkan diskon 10%")
            print(f'Total belanja Anda setelah diskon 10% adalah {total_baru}')
        elif total > 300_000:
            total_baru = total * 0.92
            print("Anda mendapatkan diskon 8%")
            print(f'Total belanja Anda setelah diskon 8% adalah {total_baru}')
        elif total > 200_000:
            total_baru = total * 0.95
            print("Anda mendapatkan diskon 5%")
            print(f'Total belanja Anda setelah diskon 5% adalah {total_baru}')
        else:
            print(f'Total belanja Anda adalah Rp {total}')


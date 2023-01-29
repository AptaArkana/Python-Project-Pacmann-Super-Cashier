#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Transaksi import Transaksi
from tabulate import tabulate


# In[3]:


def menu(obj):
    """
        Function untuk menu transaksi
    """
    print("-"*60)
    print("Selamat Datang Di Pacmann - Super Cashier")
    print("-"*60)
    print(tabulate({"Menu": [1, 2, 3, 4, 5, 6, 7, 8, 9,],
            "Kegiatan": ["Menambahkan item baru", "Mengubah nama item", "Mengubah jumlah item", "Mengubah harga item", "Menghapus item", "Reset transaksi", "Check order", "Total belanja", "Exit"]}, 
                headers="keys", tablefmt="pretty"))
    
    #Masukan menu
    pil = input("Masukan Menu Transaksi Pilihan Anda : ")
    
    match pil:
            case "1":
                #Masukan nama item
                nama_item = input('Masukan nama item : ')
                
                while True:
                    try:
                        #Masukan jumlah item
                        jumlah_item = int(input('Masukan jumlah item : '))
                    except ValueError:
                        print ("Inputan harus berupa angka!")
                    else:
                        break
                        
                # Looping sampai masukkan berupa angka
                while True:
                    try:
                        #Masukan harga item
                        harga_item = int(input('Masukan harga item : '))
                    except ValueError:
                        print ("Inputan harus berupa angka!")
                    else:
                        break
                        
                # memanggil method yang ada di class Transaksi
                obj.add_item(nama_item, jumlah_item, harga_item)
                
                # kembali ke menu
                menu(obj)
                
            case "2":
                # Input nama item
                nama_item = input('Masukan nama item : ')

                # Input harga item yang baru
                nama_item_baru =input('Masukan nama item yang baru : ') 

                # memanggil method yang ada di class Transaction
                obj.update_nama_item(nama_item, nama_item_baru)

                # kembali ke menu
                menu(obj)
                
            case "3":
                # Input nama item
                nama_item = input('Masukan nama item : ')

                # Looping sampai masukkan berupa angka
                while True:
                    try:
                        # Input jumlah item yang baru
                        jumlah_item_baru = int(input('Masukan jumlah item : '))
                    except ValueError:
                        print ("Masukan harus angka!")
                    else:
                        break

                # memanggil method yang ada di class Transaction
                obj.update_qty_item(nama_item, jumlah_item_baru)

                # kembali ke menu
                menu(obj)
                
            case "4":
                # Input nama item
                nama_item = input('Masukan nama item : ')

                # Looping sampai masukkan berupa angka
                while True:
                    try:
                        # Input harga item yang baru
                        harga_item_baru = int(input('Masukan harga item : '))
                    except ValueError:
                        print ("Masukan harus angka!")
                    else:
                        break 

                # memanggil method yang ada di class Transaction
                obj.update_hrg_item(nama_item, harga_item_baru)

                # kembali ke menu
                menu(obj)
                
            case "5":
                # Input nama item
                nama_item = input('Masukan nama item : ')

                # memanggil method yang ada di class Transaction
                obj.dlt_item(nama_item)

                # kembali ke menu
                menu(obj)
                
            case "6":
                # memanggil method yang ada di class Transaction
                obj.rst_trans()

                # kembali ke menu
                menu(obj)
                
            case "7":
                # memanggil method yang ada di class Transaction
                obj.check_order()

                # kembali ke menu
                menu(obj)
                
            case "8":
                # memanggil method yang ada di class Transaction
                obj.ttl_price()

                # kembali ke menu
                menu(obj)
                
            case "9":
                print("-"*60)
                print("Terima kasih telah mengunjungi Supermarket Pacmann.")
                print("-"*60)
                pass
                
            case _:
                print("Inputan Anda Salah.\n")
                # kembali ke menu
                menu(obj)


# In[4]:


# Instance class Transaction    
transc1 = Transaksi()

# Memanggil function menu
menu(transc1)


# In[ ]:





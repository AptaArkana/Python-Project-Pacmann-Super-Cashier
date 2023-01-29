# Python-Project-Pacmann-Super-Cashier
Sistem kasir sederhana yang menerapkan self service dengan menggunakan bahasa pemrograman Python 

## Latar Belakang
Andi adalah seorang pemilik supermarket besar di salah satu kota di indonesia, Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya Sehingga customer bisa langsung memasukkan dem yang dibel, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut Setelah Andi melakukan riset, ternyata Andi memiliki masalah yaitu Andi membutuhkan Programmer untuk membuatkan fitur-fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar

## Tujuan Pembuatan
Tujuan dari pembuatan program ini adalah sebagai berikut :
1. Agar Customer bisa menambahkan barang yang akan dibeli
2. Melakukan penggantian nama, jumlah, atau harga dari barang yang akan dibeli
3. Melakukan penghapusan barang yang terdapat dalam daftar belanja
4. Melakukan pengecekan daftar belanja yang telah dimasukkan

## Deskripsi Task
1. Module ```Transaksi.py``` memuat function - function yang akan digunakan
2. Module ```main.py``` berisi daftar menu kasir

## Flowchart
<img width="231" alt="image" src="https://user-images.githubusercontent.com/79633073/215315088-20c05707-7db1-47a5-88cc-03920e2540e6.png">
Pertama user akan menjalankan program, lalu program akan meminta inputan berupa menu dari kasir. Jika inputan sesuai maka program akan memanggil function yang berada di module transaksi. sedangkan jika tidak sesuai maka akan menampilkan pesan error.

## Module Transaksi
Di dalam class Transaction terdapat beberapa fungsi yang dapat menjalankan tugas-tugas spesifik.
1. Fungsi ```add_item()``` menambahkan item/barang yang dipilih oleh user ke dalam daftar pesanan.
2. Fungsi ```update_nama_item()``` memperbarui nama item yang sudah terdaftar di dalam pesanan.
3. Fungsi ```update_qty_item()``` memperbarui jumlah item yang telah terdaftar di dalam pesanan.
4. Fungsi ```update_hrg_item()``` memperbarui harga item yang telah terdaftar di dalam pesanan.
5. Fungsi ```dlt_item()``` menghapus suatu item dari daftar pesanan.
6. Fungsi ```rst_trans()``` menghapus item yang terdaftar di dalam pesanan.
7. Fungsi ```check_order()``` melihat kembali semua item yang terdaftar di pesanan.
8. Fungsi ```ttl_price()``` menghitung total harga dari seluruh item yang terdaftar dalam pesanan.

## Test Case
1. Customer ingin menambahkan dua item baru menggunakan method add_item () Item yang ditambahkan adalah sebagai berikut:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000 
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000
Output :
![image](https://user-images.githubusercontent.com/79633073/215320302-c5697ef4-6ed7-47f6-9349-72df0e4c86bf.png)

2. Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method delete_item () untuk menghapus item. Item yang ingin dihapuskan adalah Pasta Gigi.
Output:
![image](https://user-images.githubusercontent.com/79633073/215320381-a7a20d65-5e7a-4044-a0c5-24c398ac1d8b.png)

3. Ternyata setelah dipikir - pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method reset_transaction () untuk menghapus semua item yang sudah ditambahkan.
Output:
![image](https://user-images.githubusercontent.com/79633073/215320881-522e62e9-b7cf-437f-8b4a-359161bed00e.png)

4. Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan menggunakan method total_price (). Sebelum mengeluarkan output total belanja akan menampilkan item - item yang dibeli
 Output:
 ![image](https://user-images.githubusercontent.com/79633073/215320983-edd2cbf6-ce24-4ce2-b057-f0ffc7c47258.png)

## Future Work
1. Membuat sistem kasir ini terkoneksi DB dan Internet
2. Menambahkan jasa pengiriman
3. Membuat promo kode referal

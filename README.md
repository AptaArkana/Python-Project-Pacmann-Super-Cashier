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

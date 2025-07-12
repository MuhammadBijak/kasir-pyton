#data menu 
menu = {
    "fried chicken"     : 15000,
    "burger king"       : 25000,
    "coca-cola"         : 15000,
    "ice jeruk"         : 15000,
}
print ("========================= Daftar Menu ==========================")  #navbar atas
for i in menu:
    print("Daftar Menu : ", i,"\t Harga : ",menu[i])    #\t itu kasih spasi
print("Pembelian diatas Rp. 100.000,- mendapatkan diskon 15%")
print("=================================================================") #navbar bawah
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesanan : "))
bayar = jumlah * menu[beli]

if bayar > 10000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar

print("====================Detail Pembayaran===========================")
print("Menu yang dipesan            : ",beli)
print("Jumlah yang dipesan          : ",jumlah)
print("Total Biaya                  : ",bayar)
print("Total yang harus dibayar     : ",total)

"""
jika tidak jalan dan erornya itu [beli], maka yang salah itu penyebutan data menunya
"""
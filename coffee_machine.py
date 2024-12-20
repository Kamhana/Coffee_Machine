#Program Coffee Machine
# User memasukkan menu minuman kopi yang diinginkan dan mengeluarkan seluruh prosesnya
# Asumsi seluruh masukan user selalu valid 

#Kamus
beans = 1000 #grams
water = 10000 #ml
milk = 1000 #ml
sugar = 100 #teaspoon
ice = 1000 #pieces
aren = 100 #tablespoon

#Algoritma
while beans and water and milk and sugar and ice and aren > 0: #Selama beans, water, milk, sugar, ice, dan aren masih ada
    print("Espresso (Hot) \nAmericano \nCappuccino \nKopi Gula Aren \nCafe Latte")
    pesanan = input("Silahkan pilih menu pesanan Anda: ") #User masih bisa memesan
    
    if pesanan.lower() == "espresso":
        #Pemilihan size cup
        cup_size = input("Small/Reguler/Large: ")
        if cup_size.lower() == "small": #Apabila ukuran cup yang dipilih adalah small
            beans -= 18
            water -= 40
            sugar -= 1
            print("Generating QR")
            print("Silahkan melakukan pembayaran.")
            print("Pembayaran selesai. Membuat pesanan...")
            print("Pesanan Anda telah siap. Selamat menikmati.")
        elif cup_size.lower() == "reguler": #Apabila ukuran cup yang dipilih adalah reguler
            beans -= 19 #Jumlah beans yang dipakai lebih banyak
            water -= 50 #Jumlah air yang dipakai juga lebih banyak
            sugar -= 2
            print("Generating QR")
            print("Silahkan melakukan pembayaran.")
            print("Pembayaran selesai. Membuat pesanan...")
            print("Pesanan Anda telah siap. Selamat menikmati.")
        elif cup_size.lower() == "large": #Apabila ukuran cup yang dipilih adalah large
            beans -= 20 #Jumlah beans yang dipakai lebih banyak
            water -= 60 #Jumlah air yang dipakai juga lebih banyak
            sugar -= 3
            print("Generating QR")
            print("Silahkan melakukan pembayaran.")
            print("Pembayaran selesai. Membuat pesanan...")
            print("Pesanan Anda telah siap. Selamat menikmati.")
        else:
            print("Silahkan masukkan ukuran dengan benar.")
    elif pesanan.lower() == "americano":
        #Pemilihan size cup
        cup_size = input("Small/Reguler/Large: ")
        if cup_size.lower() == "small": #Apabila ukuran cup yang dipilih adalah small
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 18
                water -= 180 #Jumlah air yang dipakai lebih banyak
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice": #Apabila suhu minuman yang dipilih adalah ice
                beans -= 18
                water -= 160 #Jumlah air yang dipakai lebih sedikit
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        elif cup_size.lower() == "reguler": #Apabila ukuran cup yang dipilih adalah reguler
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 19 #Jumlah beans yang dipakai lebih banyak (karena size cup reguler)
                water -= 190 #Jumlah air yang dipakai juga lebih banyak (karena hot)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice":
                beans -= 19 #Jumlah beans yang dipakai lebih banyak (karena size cup reguler)
                water -= 170 #Jumlah air yang dipakai lebih sedikit (karena ice)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        elif cup_size.lower() == "large": #Apabila ukuran cup yang dipilih adalah large
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 20 #Jumlah beans yang dipakai lebih banyak (karena size cup large)
                water -= 200 #Jumlah air yang dipakai juga lebih banyak (karena hot)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice":
                beans -= 20 #Jumlah beans yang dipakai lebih banyak (karena size cup large)
                water -= 180 #Jumlah air yang dipakai lebih sedikit (karena ice)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice":
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        else:
            print("Silahkan masukkan ukuran dengan benar.")
    elif pesanan.lower() == "cappuccino":
        #Pemilihan size cup
        cup_size = input("Small/Reguler/Large: ")
        if cup_size.lower() == "small": #Apabila ukuran cup yang dipilih adalah small
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 18
                water -= 40
                milk -= 120
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice": #Apabila suhu minuman yang dipilih adalah ice
                beans -= 18
                water -= 30 #Jumlah air yang dipakai lebih sedikit
                milk -= 110 #Jumlah susu yang dipakai lebih sedikit
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        elif cup_size.lower() == "reguler": #Apabila ukuran cup yang dipilih adalah reguler
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 19 #Jumlah beans yang dipakai lebih banyak (karena size cup reguler)
                water -= 50 #Jumlah air yang dipakai juga lebih banyak (karena hot)
                milk -= 130 #Jumlah susu yang dipakai lebih banyak (karena hot)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice": #Apabila suhu minuman yang dipilih adalah ice
                beans -= 19 #Jumlah beans yang dipakai lebih banyak (karena size cup reguler)
                water -= 40 #Jumlah air yang dipakai lebih sedikit (karena ice)
                milk -= 120 #Jumlah susu yang dipakai lebih sedikit (karena ice)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        elif cup_size.lower() == "large": #Apabila ukuran cup yang dipilih adalah large
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 20 #Jumlah beans yang dipakai lebih banyak (karena size cup large)
                water -= 60 #Jumlah air yang dipakai juga lebih banyak (karena hot)
                milk -= 140 #Jumlah susu yang dipakai lebih banyak (karena hot)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice": #Apabila suhu minuman yang dipilih adalah ice
                beans -= 20 #Jumlah beans yang dipakai lebih banyak (karena size cup large)
                water -= 50 #Jumlah air yang dipakai juga lebih sedikit (karena ice)
                milk -= 130 #Jumlah susu yang dipakai lebih sedikit (karena ice)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        else:
            print("Silahkan masukkan ukuran dengan benar.")
    elif pesanan.lower() == "kopi gula aren":
        #Pemilihan size cup
        cup_size = input("Small/Reguler/Large: ")
        if cup_size.lower() == "small": #Apabila ukuran cup yang dipilih adalah small
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 18
                water -= 40 #Jumlah air lebih banyak
                aren -= 1
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice": #Apabila suhu minuman yang dipilih adalah ice
                beans -= 18
                water -= 30 #Jumlah air lebih sedikit
                aren -= 1
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        elif cup_size.lower() == "reguler": #Apabila ukuran cup yang dipilih adalah reguler
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 19 #Jumlah beans yang dipakai lebih banyak (karena size cup reguler)
                water -= 50 #Jumlah air yang dipakai juga lebih banyak (karena hot)
                aren -= 1
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice": #Apabila suhu minuman yang dipilih adalah ice
                beans -= 19 #Jumlah beans yang dipakai lebih banyak (karena size cup reguler)
                water -= 40 #Jumlah air yang dipakai juga lebih sedikit (karena ice)
                aren -= 1
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        elif cup_size.lower() == "large": #Apabila ukuran cup yang dipilih adalah large
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 20 #Jumlah beans yang dipakai lebih banyak (karena size cup large)
                water -= 60 #Jumlah air yang dipakai juga lebih banyak (karena hot)
                aren -= 1
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice":
                beans -= 20 #Jumlah beans yang dipakai lebih banyak (karena size cup large)
                water -= 50 #Jumlah air yang dipakai juga lebih sedikit (karena ice)
                aren -= 1
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        else:
            print("Silahkan masukkan ukuran dengan benar.")
    elif pesanan.lower() == "cafe latte":
        #Pemilihan size cup
        cup_size = input("Small/Reguler/Large: ")
        if cup_size.lower() == "small": #Apabila ukuran cup yang dipilih adalah small
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 18
                water -= 40 #Jumlah air yang dipakai lebih banyak 
                milk -= 150 #Jumlah susu yang dipakai lebih banyak 
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice":
                beans -= 18
                water -= 30 #Jumlah air yang dipakai lebih sedikit
                milk -= 140 #Jumlah susu yang dipakai lebih banyak
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Jika yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Jika yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        elif cup_size.lower() == "reguler": #Apabila ukuran cup yang dipilih adalah reguler
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 19 #Jumlah beans yang dipakai lebih banyak (karena size cup reguler)
                water -= 50 #Jumlah air yang dipakai juga lebih banyak (karena hot)
                milk -= 160 #Jumlah susu yang dipakai lebih banyak (karena hot)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice": #Apabila suhu minuman yang dipilih adalah ice
                beans -= 19 #Jumlah beans yang dipakai lebih banyak (karena size cup reguler)
                water -= 40 #Jumlah air yang dipakai juga lebih sedikit (karena ice)
                milk -= 150 #Jumlah susu yang dipakai lebih sedikit (karena ice)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        elif cup_size.lower() == "large": #Apabila ukuran cup yang dipilih adalah large
            #Pemilihan suhu minuman
            temp = input("Hot/Ice: ")
            if temp.lower() == "hot": #Apabila suhu minuman yang dipilih adalah hot
                beans -= 20 #Jumlah beans yang dipakai lebih banyak (karena size cup large)
                water -= 60 #Jumlah air yang dipakai juga lebih banyak (karena hot)
                milk -= 170 #Jumlah susu yang dipakai lebih banyak (karena hot)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                print("Generating QR")
                print("Silahkan melakukan pembayaran.")
                print("Pembayaran selesai. Membuat pesanan...")
                print("Pesanan Anda telah siap. Selamat menikmati.")
            elif temp.lower() == "ice": #Apabila suhu minuman yang dipilih adalah ice
                beans -= 20 #Jumlah beans yang dipakai lebih banyak (karena size cup large)
                water -= 50 #Jumlah air yang dipakai juga lebih sedikit (karena ice)
                milk -= 160 #Jumlah susu yang dipakai juga lebih sedikit (karena ice)
                #Pemilihan takaran gula
                custom_sugar = int(input("Silahkan pilih takaran gula yang Anda inginkan (0/1/2/3/4): "))
                sugar = sugar - custom_sugar
                #Pemilihan takaran es
                custom_ice = input("Less Ice/Normal Ice? ")
                if custom_ice.lower() == "less ice": #Apabila yang dipilih adalah less ice
                    ice = ice - 4 #Jumlah ice yang dipakai lebih sedikit
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
                elif custom_ice.lower() == "normal ice": #Apabila yang dipilih adalah normal ice
                    ice = ice - 8 #Jumlah ice yang dipakai lebih banyak
                    print("Generating QR")
                    print("Silahkan melakukan pembayaran.")
                    print("Pembayaran selesai. Membuat pesanan...")
                    print("Pesanan Anda telah siap. Selamat menikmati.")
            else:
                print("Silahkan masukkan opsi dengan benar.")
        else:
            print("Silahkan masukkan ukuran dengan benar.")
    elif pesanan.lower() == "cancel": #Apabila tidak jadi memesan minuman
        print("Sampai jumpa!")
        break
    else:
        print("Maaf menu tersebut tidak tersedia.") #Apabila user salah input menu
    
    repeat_order = input("Apakah Anda ingin memesan menu lain? Yes/No ")
    if repeat_order.lower() == "no": #Apabila tidak ada pesanan lainnya
        print("Sampai jumpa!")
        break
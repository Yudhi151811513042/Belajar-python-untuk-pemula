uang = input("kamu uangnya berapa? ")
utang = 10000

if int(uang) < utang:
    print("wah maaf bos ngga cukup")
elif int(uang) == utang:
    print("terimakasih, udah bayar")
else:
    print("wahh uangnya lebih")
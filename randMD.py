import hashlib, random
print """RandMD
 _   __                   ___                  
| | / /                  / _ \                 
| |/ /  __ _ _ __ __ _  / /_\ \_   _  __ _ ____
|    \ / _` | '__/ _` | |  _  | | | |/ _` |_  /
| |\  \ (_| | | | (_| | | | | | |_| | (_| |/ / 
\_| \_/\__,_|_|  \__,_| \_| |_/\__, |\__,_/___|
                                __/ |          
                               |___/
Random MD5 Scanner                  | karaayaz_"""
print ""
def crack():
    md5hash = raw_input("MD5 Hash: ")
    minimum = input("Minimum Uzunluk: ")
    maximum = input("Maximum Uzunluk: ")

    if len(md5hash) != 32:
        print "Hata! - Hash problemli..."
        print
        crack()

    md5hash = md5hash.lower()
    sifre = ""
    sifreler = []
    d_bir = True
    d_iki = True

    while d_bir:
        while d_iki:
            sinir = random.randint(minimum, maximum)
            for md in range(sinir):
                md5 = random.randint(97,122)
                sifre += chr(md5)
            break
        pass_kont = sifre in sifreler
        if pass_kont == False:
            hashedpass = hashlib.md5(sifre.encode())
            if md5hash == hashedpass.hexdigest():
                print "Sifre: {}".format(sifre)
                break
            print "Sifre bulunamadi..."
            print "Denenen sifre:", sifre
            sifreler.append(sifre)
            print "Deneme sayisi {}".format(str(len(sifreler)))
            sifre = ""
    wordlist = open("wordlist.txt","w")
    for wl in sifreler:
        wordlist.write(wl)
        wordlist.write("\n")
    wordlist.close()
    raw_input("")
crack()

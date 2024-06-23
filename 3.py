# Input nilai N
N = int(input("Masukkan nilai N: "))

# Input string
string = input("Masukkan string: ")

# Inisialisasi variabel untuk menghitung kemunculan kata 'tuan'
count_tuan = 0

# Iterasi melalui setiap karakter dalam string
i = 0
while i < len(string):
    # Cek apakah karakter saat ini adalah 't'
    if string[i] == 't':
        j = i + 1
        # Cek apakah karakter berikutnya adalah 'u'
        while j < len(string):
            if string[j] == 'u':
                k = j + 1
                # Cek apakah karakter berikutnya adalah 'a'
                while k < len(string):
                    if string[k] == 'a':
                        l = k + 1
                        # Cek apakah karakter berikutnya adalah 'n'
                        while l < len(string):
                            if string[l] == 'n':
                                # Kata 'tuan' ditemukan!!!
                                count_tuan += 1
                            l += 1
                    k += 1
            j += 1
    i += 1

# Tampilkan hasil
print(f"Ada {count_tuan} buah kemunculan.")

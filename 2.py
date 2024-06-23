# Meminta pengguna untuk memasukkan nilai N
N = int(input("Masukkan N: ")) 

# Membuat daftar L dan R dengan panjang N dan mengisi semua elemen dengan 0
L = [0 for i in range(N)]
R = [0 for i in range(N)]

# Melakukan iterasi sebanyak N kali
for i in range(N):
    # Meminta pengguna untuk memasukkan nilai L dan R untuk setiap indeks
    L[i] = int(input(f"Masukan L[{i+1}]: "))
    R[i] = int(input(f"Masukan R[{i+1}]: "))

# Meminta pengguna untuk memasukkan nilai Q
Q = int(input("Masukkan Q: "))

# Melakukan iterasi sebanyak Q kali
for i in range(Q):
    # Meminta pengguna untuk memasukkan nilai X
    X = int(input(f"Masukkan X ke {i+1}: "))
    
    # Mengecek apakah X sama dengan L[i] atau R[i]
    if L[i] == X or R[i] == X:
        # Jika ya, mencetak bahwa titik ada di garis
        print(f"Titik ke {i+1} ada di garis.")
    else:
        # Jika tidak, mencetak bahwa titik tidak ada di garis
        print(f"Titik ke tidak ada di garis.")

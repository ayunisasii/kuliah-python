# tebak Angka

from random import randint
angka_komputer = randint(0, 20)
angka_tebakan = -6
percobaan = 0

while angka_tebakan != angka_komputer:
    percobaan += 1
    if percobaan > 5:
        print('Anda kalah!')
        print('Anda sudah menebak lebih dari 3 kali')
        break
    angka_tebakan = int(input('Masukkan angka tebakan: '))
    if angka_tebakan > angka_komputer:
        print('Tebakan terlalu besar')
    elif angka_tebakan < angka_komputer:
        print('Tebakan terlalu kecil')
else:
    print('Selamat, anda menang!')
    print(f'Anda telah menebak sebanyak {percobaan} kali')
    


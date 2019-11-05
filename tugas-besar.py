import math
def persegi_panjang():
	a =int(input("masukkan nilai panjang :"))
	b =int(input("masukkan nilai lebar :"))
	luas = a*b
	print(" Kamu menggunakan rumus : panjang * lebar")
	return luas

def lingkaran():
	c =int(input("masukkan nilai radius:"))
	luas =(c**2 * math.pi)
	print("Kamu menggunakan rumus : Pi * radius * radius")
	return luas

def segitiga():
	d = int(input("masukkan tinggi segitiga:"))
	e = int(input("masukkan lebar segitiga:"))
	print("Kamu menggunakan rumus : 1/2 * alas * tinggi")
	luas = d * e * 1/2
	return luas

def faktorial(n):
	if n == 0:
		return 1
	else:
		return n * faktorial(n-1)
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)      
def proses():
	n = int(input("Ingin melakukan proses yang mana ?(1,2,3,4,5, press any number to stop):"))
	if n == 1:
		print("menghitung luas lingkaran\n", persegi_panjang())
	elif n == 2:
		print("menghitung luas lingkaran\n", lingkaran())
	elif n == 3:
		print("menghitung luas segitiga\n", segitiga())
	elif n == 4:
		print("Kamu menggunakan rumus: n * (n-1) * (n-2).... * 1")
		print("Menghitung faktorial\n", faktorial(n = int(input("masukkan nilai n :"))))
	elif n == 5:
		print("Menghitung fibonacci\n", fibonacci(n = int(input("masukkan nilai n:"))))
	else:
		print("yakin ?")

print("Menu\n")
print("1.Persegi Panjang \n", "2.Lingkaran\n", "3.Segitiga\n", "4.Faktorial\n", "5.Fibonacci\n", "6.Exit ")

proses()
t = input("ingin hitung lagi ? (y/press any key to stop):")
while True:
	if t =="y":
		proses()
	else:
		print("selesai")
		break
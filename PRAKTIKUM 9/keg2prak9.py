data = open("L200220045", "a")
data.write("\nGrobogan")
data.close()

data = open("L200220045", "r")
nim = data.readline()
tanggal = data.readline()
nama = data.readline()
asal = data.readline()

dd = tanggal[:2]
mm = tanggal [3:5]
yyyy = tanggal [6:]


tanggal = mm+"/"+dd+"/"+"/"+yyyy

print(nama)
print(asal, tanggal)
print(nim)

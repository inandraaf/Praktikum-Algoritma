import shelve

data = open("L200220045", "r")
nim = data.readline()
tanggal = data.readline()
nama = data.readline()
kota = data.readline()
data = shelve.open("Nandra")
data["Biodata"] = [nim, tanggal, nama, kota]
data.close()

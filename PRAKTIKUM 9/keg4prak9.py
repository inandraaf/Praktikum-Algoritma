import shelve

data = shelve.open("Nandra")
print("NIM           : "+ data ["Biodata"][0])
print("Tanggal lahir : "+ data ["Biodata"][1])
print("Nama          : "+ data ["Biodata"][2])
print("Kota Asal     : "+ data ["Biodata"][3])
data.close()

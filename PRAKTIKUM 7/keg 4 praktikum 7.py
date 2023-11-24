## Kegiatan tambahan

import datetime
from time import sleep

#waktu sekarang
waktu = datetime.datetime.now()
detik = waktu.second

while detik != 0 :
    #mengubah waktu
    waktu = datetime.datetime.now()
    detik = waktu.second
    #membuat jadi format string
    NowHour = str(waktu.hour)
    NowMinute = str(waktu.minute)
    NowSecond = str(waktu.second)
    print (NowHour + ":" + NowMinute + ":" + NowSecond)
    #membuat delay
    sleep(1)

print("Jam praktikum sudah habis. Silahkan pulang.")

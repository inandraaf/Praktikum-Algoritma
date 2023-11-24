def hitung_luas(alas, tinggi):
    "fungsi menghitung luas dari limas segiempat"
    luas = float((4*(0.5*alas*tinggi))+ (alas*alas))
    print(f"Jika alas adalah {alas} dan tinggi adalah {tinggi}, maka luas adalah")
    return luas
print("<!DOCTYPE html>\n")
print("""
    <!DOCTYPE html>
    
    <html>
    <head>
        <title>Luas Limas Segi Empat</title>
    </head>
    <body>
        <h3>Bangun Geometri<h3>
        <br>
        <p>
            Nama bangun : Limas Segiempat<br>
            Dimensi : 3D<br>
            Rumus luas : (4 * Luas Selimut) + Luas Alas<br>
            Alas : 6<br>
            Tinggi : 5<br>
            Luas : 96<br>
        </p>
    </body>
    </html>
    """)
print(hitung_luas(alas=8,tinggi=5))
print("</html>")

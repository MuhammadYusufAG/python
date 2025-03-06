# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-o', '--output', action='store_true', help="tampilkan output")
# args = parser.parse_args()

# if args.output:
#      print("Halo, ini merupakan sebuah output dari args.py")

# dicmd python namaFile.py -o / -h

# argumen bersifat wajib
import argparse
from datetime import datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
    parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan tanggal lahir anda (DD-MM-YYYY)")
    args = parser.parse_args()

# validasi umur
    try:
        tanggal_lahir = datetime.strptime(args.tanggallahir, '%d-%m-%Y')
    except ValueError:
        print("Format tanggal lahir tidak valid. Harap gunakan format dd-mm-yyyy.")
        return


    today = datetime.today()
    umur = today.year - tanggal_lahir.year - ((today.month, today.day) < (tanggal_lahir.month, tanggal_lahir.day))

    # panggilan
    if umur < 30:
        panggilan = 'kakak'
    else:
        panggilan = 'bapak'

    print(f"Terima kasih telah menggunakan panggildicoding.py pada tahun 2025, {panggilan} {args.nama}")

# print()

if __name__ == "__main__":
    main()
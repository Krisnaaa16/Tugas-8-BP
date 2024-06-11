def input_data_mahasiswa():
    mahasiswa = []
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    for i in range(jumlah):
        nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
        nim = input(f"Masukkan NIM mahasiswa ke-{i+1}: ")
        prodi = input(f"Masukkan Prodi mahasiswa ke-{i+1}: ")
        nilai = float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
        mahasiswa.append({'nama': nama, 'nim': nim, 'prodi': prodi, 'nilai': nilai})
    return mahasiswa

def tampilkan_data_mahasiswa(mahasiswa):
    print("Data Mahasiswa:")
    for m in mahasiswa:
        print(f"Nama: {m['nama']}, NIM: {m['nim']}, Prodi: {m['prodi']}, Nilai: {m['nilai']}")

def hitung_rata_rata_nilai(mahasiswa):
    if not mahasiswa:
        return 0
    total_nilai = sum(m['nilai'] for m in mahasiswa)
    return total_nilai / len(mahasiswa)

def cari_mahasiswa_nilai_tertinggi_dan_terendah(mahasiswa):
    if not mahasiswa:
        return None, None
    mahasiswa_tertinggi = max(mahasiswa, key=lambda x: x['nilai'])
    mahasiswa_terendah = min(mahasiswa, key=lambda x: x['nilai'])
    return mahasiswa_tertinggi, mahasiswa_terendah

def input_data_barang():
    barang = []
    jumlah = int(input("Masukkan jumlah barang: "))
    for i in range(jumlah):
        nama = input(f"Masukkan nama barang ke-{i+1}: ")
        kode = input(f"Masukkan kode barang ke-{i+1}: ")
        jumlah_barang = int(input(f"Masukkan jumlah barang ke-{i+1}: "))
        barang.append({'nama': nama, 'kode': kode, 'jumlah': jumlah_barang})
    return barang

def tampilkan_data_barang(barang):
    print("Data Barang:")
    for b in barang:
        print(f"Nama: {b['nama']}, Kode: {b['kode']}, Jumlah: {b['jumlah']}")

def cari_barang_berdasarkan_kode(barang, kode):
    for b in barang:
        if b['kode'] == kode:
            return b
    return None

def hapus_barang_berdasarkan_kode(barang, kode):
    for b in barang:
        if b['kode'] == kode:
            barang.remove(b)
            return True
    return False

def input_data_transaksi():
    transaksi = []
    jumlah = int(input("Masukkan jumlah transaksi: "))
    for i in range(jumlah):
        jenis = input(f"Masukkan jenis transaksi ke-{i+1} (pemasukan/pengeluaran): ")
        jumlah_transaksi = float(input(f"Masukkan jumlah transaksi ke-{i+1}: Rp. "))
        transaksi.append({'jenis': jenis, 'jumlah': jumlah_transaksi})
    return transaksi

def tampilkan_data_transaksi(transaksi):
    print("Data Transaksi:")
    for t in transaksi:
        print(f"Jenis: {t['jenis']}, Jumlah: Rp. {t['jumlah']},-")

def hitung_total_pemasukan(transaksi):
    return sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pemasukan')

def hitung_total_pengeluaran(transaksi):
    return sum(t['jumlah'] for t in transaksi if t['jenis'] == 'pengeluaran')

def hitung_saldo_akhir(transaksi):
    pemasukan = hitung_total_pemasukan(transaksi)
    pengeluaran = hitung_total_pengeluaran(transaksi)
    return pemasukan - pengeluaran

def menu():
    print("Menu:")
    print("1. Data Mahasiswa")
    print("2. Inventaris Barang")
    print("3. Pengelolaan Keuangan Pribadi")
    print("0. Keluar")

def main():
    while True:
        menu()
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            mahasiswa = input_data_mahasiswa()
            tampilkan_data_mahasiswa(mahasiswa)
            rata_rata = hitung_rata_rata_nilai(mahasiswa)
            print(f"Rata-rata nilai mahasiswa: {rata_rata}")
            tertinggi, terendah = cari_mahasiswa_nilai_tertinggi_dan_terendah(mahasiswa)
            print(f"Mahasiswa dengan nilai tertinggi: {tertinggi}")
            print(f"Mahasiswa dengan nilai terendah: {terendah}")
        elif pilihan == "2":
            barang = input_data_barang()
            tampilkan_data_barang(barang)
            kode = input("Masukkan kode barang yang dicari: ")
            hasil = cari_barang_berdasarkan_kode(barang, kode)
            if hasil:
                print(f"Barang ditemukan: {hasil}")
            else:
                print("Barang tidak ditemukan.")
            kode = input("Masukkan kode barang yang akan dihapus: ")
            if hapus_barang_berdasarkan_kode(barang, kode):
                print("Barang berhasil dihapus.")
            else:
                print("Barang tidak ditemukan.")
        elif pilihan == "3":
            transaksi = input_data_transaksi()
            tampilkan_data_transaksi(transaksi)
            total_pemasukan = hitung_total_pemasukan(transaksi)
            print(f"Total pemasukan: Rp. {total_pemasukan},-")
            total_pengeluaran = hitung_total_pengeluaran(transaksi)
            print(f"Total pengeluaran: Rp. {total_pengeluaran},-")
            saldo_akhir = hitung_saldo_akhir(transaksi)
            print(f"Saldo akhir: Rp. {saldo_akhir},-")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
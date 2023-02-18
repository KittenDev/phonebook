import json


def welcome():
    print("=" * 70,
          "Welcome to PhoneBook".center(70),
          "Author : Dafaa".center(70),
          "=" * 70,
          "Silahkan pilih layanan dibawah dengan input angka yang sesuai:",
          "1. Tampilkan Seluruh Kontak",
          "2. Tambahkan Kontak Baru",
          "3. Edit Kontak",
          "4. Hapus Kontak",
          "5. Cari Kontak",
          "6. Keluar PhoneBook", sep="\n")


def inisialization():
    try:
        f = open('contact_save.txt', 'r')
        read_result = f.read()
        f.close()
        return json.loads(read_result)
    except IOError:
        f = open('contact_save.txt', 'w+')
        print("File tidak ditemukan! Mencoba membuat file baru :)")
        f.close()
        return json.loads('{}')


def print_dict(contact):
    i = 1
    for contact_name, contact_info in contact.items():
        print(f"\n{i}. Nama: {contact_name}")
        for info in contact_info:
            print(f"{info}: {contact_info[info]}")
        i += 1


def check_key(contact, name):
    return name in contact


def insert_contact(contact, name):
    if name == '':
        name = input("Masukkan Nama Kontak: ")
        if check_key(contact, name):
            print('Nama sudah ada pada kontak')
            return contact
    contact[name] = {}
    contact[name]['Nomor Telepon'] = input("Masukkan Nomor Telepon: ")
    contact[name]['Email'] = input("Masukkan Email: ")
    contact[name]['Alamat'] = input("Masukkan Alamat: ")
    return contact


def edit_contact(contact):
    name = input("Masukkan nama kontak yang mau diupdate:")
    if check_key(contact, name):
        contact[name]['Nomor Telepon'] = input("Masukkan Nomor Telepon: ")
        contact[name]['Email'] = input("Masukkan Email: ")
        contact[name]['Alamat'] = input("Masukkan Alamat: ")
        return contact
    else:
        user_input = input('Nama tidak ditemukan apakah anda ingin membuat yang baru? (y/n)')
        if user_input == 'y':
            return insert_contact(contact, name)
        if user_input == 'n':
            return contact


def delete_contact(contact):
    name = input('Masukkan nama yang ingin dihapus: ')
    if check_key(contact, name):
        del contact[name]
        print(f"Kontak {name} berhasil dihapus!")
        return contact
    else:
        print('Nama tidak ada dalam kontak, tidak dapat menghapus')
        return contact


def search_contact(contact):
    name = input('Masukkan nama yang ingin dicari: ')
    if check_key(contact, name):
        print(f"Nama: {name}")
        for info in contact[name]:
            print(f"{info}: {contact[name][info]}")
        return contact
    else:
        print('Nama kontak tidak ditemukan!!!')
        return contact


def save_contact(contact):
    with open('contact_save.txt', 'w') as f:
        f.write(json.dumps(contact))


def phonebook():
    dict_contact = inisialization()

    while True:
        welcome()
        user_input = input("Silahkan Input Pilihan yang Diinginkan: ")
        if user_input == "1":
            if not dict_contact:
                print("Kontak kosong tambah kontak dulu masbro!")
            else:
                print_dict(dict_contact)
        elif user_input == "2":
            dict_contact = insert_contact(dict_contact, '')
        elif user_input == "3":
            dict_contact = edit_contact(dict_contact)
        elif user_input == "4":
            dict_contact = delete_contact(dict_contact)
        elif user_input == "5":
            search_contact(dict_contact)
        elif user_input == "6":
            break
        else:
            print("Input tidak valid (bukan 1-6), silahkan coba lagi")
        save_contact(dict_contact)

    print('Terimakasih Sudah Menggunakan PhoneBook by Dafaa')

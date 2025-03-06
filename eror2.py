def convert_to_int(string):
    try:
        result = int(string)
        return result
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

umur = input('Masukkan umur kamu: ')  # inputan yang benar adalah angka
umur5tahunlagi = convert_to_int(umur)

if umur5tahunlagi is not None:  # Memastikan umur5tahunlagi tidak None
    print(f"Umur kamu 5 tahun lagi adalah {umur5tahunlagi + 5}")
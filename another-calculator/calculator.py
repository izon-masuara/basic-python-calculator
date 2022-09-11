import os

def tampilan(num:int):
    '''
        Menampilkan kalkulator pada terminal
    '''
    operator = ""
    display = ''''''
    if num == 2 :
        display = '''
            ======================================================
            ||                  Kalkulator                      ||
            ||                                                  ||
            ||          Pilihan Perhitungan :                   ||
            ||                                                  ||
            ||          1. Kubus                                ||
            ||          2. Balok                                ||
            ||          3. Limas                                ||
            ||                                                  ||
            ======================================================
        '''
        pilih = 0
        while pilih >= 1 or pilih <= 3 :
            print(display)
            if pilih == 1 :
                operator = "kubus"
                break
            elif pilih == 2 :
                operator = "balok"
                break
            elif pilih == 3 :
                operator = "limas"
                break
            pilih = int(input("Masukan Pilihan : "))
            os.system('clear')
    elif num == 1:
        display = '''
            ======================================================
            ||                  Kalkulator                      ||
            ||                                                  ||
            ||          Pilihan Operasi Perhitungan :           ||
            ||          1. + (Tambah)                           ||
            ||          2. - (Kurang)                           ||
            ||          3. * (Kali)                             ||
            ||          4. / (Bagi)                             ||
            ||          5. % (Modulus)                          ||
            ||          6. **(Pangkat)                          ||
            ||                                                  ||
            ======================================================
        '''
        pilih = 0
        while pilih >= 1 or pilih <= 6 :
            print(display)
            if pilih == 1 :
                operator = "+"
                break
            elif pilih == 2 :
                operator = "-"
                break
            elif pilih == 3 :
                operator = "*"
                break
            elif pilih == 4 :
                operator = "/"
                break
            elif pilih == 5 :
                operator = "%"
                break
            elif pilih == 6 :
                operator = "**"
                break
            pilih = int(input("Masukan Pilihan : "))
            os.system('clear')
    else : 
        display = '''
                ======================================================
                ||                  Kalkulator                      ||
                ||                                                  ||
                ||          Pilihan Perhitungan :                   ||
                ||                                                  ||
                ||          1. Untuk Operasi Matematika             ||
                ||          2. Untuk Operasi Bangun Ruang           ||
                ||                                                  ||
                ======================================================
            '''
    return display, operator

def operasiMatematika(operator : str):
    '''
      Operasi Matematika dasar
    '''
    num1 = int(input("Masukan angka pertama : "))
    num2 = int(input("Masukan angka kedua : "))
    result = 0
    message = ""
    if operator == "+" :
        result = num1 + num2
    elif operator == "-" :
        result = num1 - num2
    elif operator == "*" :
        result = num1 * num2
    elif operator == "/" :
        result = num1 / num2
    elif operator == "%" :
        result = num1 % num2
    elif operator == "**" :
        result = num1 ** num2
    message = f'''Jawaban dari {num1} {operator} {num2} adalah {result}'''
    os.system('clear')
    return message

def operasiBangunRuang(operator : str):
    '''
      Operasi Matematika bangun ruang Kubus, Balok dan Limas
    '''
    result = {
        'luas' : None,
        'volume' : None
    }
    message = ""
    if operator == "kubus" :
        s = int(input("Masukan panjang rusuk : "))
        result["luas"] = 6 * s**2
        result['volume'] = s**3
    elif operator == "balok" :
        p = int(input("Masukan panjang : "))
        l = int(input("Masukan lebar : "))
        t = int(input("Masukan tinggi : "))
        result["luas"] = 2 * ((p*l) + (p*t) + (l*t))
        result["volume"] = p * l * t
    elif operator == "limas" :
        la = int(input("Luas alas : "))
        tlsm = int(input("Total luas sisi miring : "))
        t = int(input("Tinggi : "))
        result["luas"] = la + tlsm
        result["volume"] = 1/3 * la * t
        
    message = f'''
    Jawaban dari operasi perhitungan {operator} adalah sebagai berikut :
    \t\tLuas {operator} \t\t= {result["luas"]}
    \t\tVolume {operator} \t\t= {result["volume"]}
    '''
    os.system('clear')
    return message

def pilihKalkulator():
    result = None
    '''
        Menentukan pilihan kalkulator
    '''
    payload = {
        "kalkulator" : 0,
        "operator" : ""
    }
    num = 0
    while num != 1 or num != 2 :
        a,b = tampilan(num)
        if b != "":
            payload["kalkulator"] = num
            payload["operator"] = b
            os.system('clear')
            break
        print(a)
        num = int(input("Masukan Pilihan : "))
        os.system('clear')

    if payload["kalkulator"] == 1 :
        result = operasiMatematika(payload["operator"])
    elif payload["kalkulator"] == 2 :
        result = operasiBangunRuang(payload["operator"])

    return result


print(pilihKalkulator())
def upahKotor(gajiPokok : int,tunjangan : int,overtime : int):
    '''
    Menghitung upah kotor kariyawan

    Parameters:
    gajiPokok (int)
    tunjangan(int)
    overtime(int)
  
    Returns:
    int : nilai dari perjumlahan gaji pokok + tunjangan + overtime
    '''
    return gajiPokok + tunjangan + overtime

def potongan(upahKotor : int):
    '''
    Menghitung potongan upah kariyawan

    Parameters:
    upahKotor (int)
  
    Returns:
    float : nilai potongan dari upah kotor
    '''
    return upahKotor*0.02

def potongan(upahKotor : int):
    '''
    Menghitung potongan upah kariyawan

    Parameters:
    upahKotor (int)
  
    Returns:
    float : nilai potongan dari upah kotor
    '''
    return upahKotor*0.02

def gajiBersih(upahKotor : int, potongan : int):
    '''
    Menghitung upah bersih kariyawan

    Parameters:
    upah kotor (int)
    potongan (float)
  
    Returns:
    str : Gaji bersih
    '''
    gajiBersih = upahKotor - potongan
    return "{:,.2f}".format(gajiBersih)

def menampilkanData(datakariyawan : dict):
    '''
    Menampilkan upah bersih kariyawan
    '''
    for data in datakariyawan :
        if data['golongan'] == 'I':
            uk = upahKotor(15000000,2250000,0)
            pt = potongan(uk)
            gb = gajiBersih(uk,pt)
            print(f'''Gaji bersih {data['nama']} adalah Rp.{gb}''')
        elif data['golongan'] == 'II':
            uk = upahKotor(7500000,750000,int(data['overtime'])*150000)
            pt = potongan(uk)
            gb = gajiBersih(uk,pt)
            print(f'''Gaji bersih {data['nama']} adalah Rp.{gb}''')
        elif data['golongan'] == 'III':
            uk = upahKotor(5000000,250000,int(data['overtime'])*100000)
            pt = potongan(uk)
            gb = gajiBersih(uk,pt)
            print(f'''Gaji bersih {data['nama']} adalah Rp.{gb}''')

dataKariyawan = [
    {'nama' : 'Anna','golongan' : 'II','overtime' : 10},
    {'nama' : 'Dimas','golongan' : 'III','overtime' : 15},
    {'nama' : 'Sriyono','golongan' : 'I','overtime' : 3},
    {'nama' : 'Oky','golongan' : 'II','overtime' : 8},
    {'nama' : 'Wati','golongan' : 'I','overtime' : 6},
    {'nama' : 'Yayan','golongan' : 'III','overtime' : 17}
]

menampilkanData(dataKariyawan)
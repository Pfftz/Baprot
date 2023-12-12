#include <iostream>
#include <string>

using namespace std;

void fungsidengandefaultArgument(int a = 10, int b = 20)
{
    cout << "Ini adalah fungsi dengan default argument" << endl;
    cout << "Nilai yang anda masukkan adalah " << a << " dan " << b << endl;
}

void fungsitanpaArgumen()
{
    cout << "Ini adalah fungsi tanpa argumen" << endl;
}

void fungsidenganArgumen(int a)
{
    cout << "Ini adalah fungsi dengan argumen" << endl;
    cout << "Nilai yang anda masukkan adalah " << a << endl;
}

int fungsidenganNilaiKembali()
{
    cout << "Ini adalah fungsi dengan nilai kembali" << endl;
    return 10;
}

int fungsidenganNilaiKembaliDanArgumen(int a)
{
    cout << "Ini adalah fungsi dengan nilai kembali dan argumen" << endl;
    cout << "Nilai yang anda masukkan adalah " << a << endl;
    return 10;
}

int fungsiRekursif(int a)
{
    cout << "Ini adalah fungsi rekursif" << endl;
    cout << "Nilai yang anda masukkan adalah " << a << endl;
    if (a == 0)
    {
        return a;
    }
    else
    {
        return fungsiRekursif(a - 1);
    }
}

int prototype(int a, int b);

void operasiString()
{
    cout << " Ini adalah operasi string" << endl;
    string nama1, nama2;
    cout << " Input string ke 1:" << endl;
    cout << " Masukkan nama anda : " << endl;
    getline(cin, nama1);
    cout << " Nama saya adalah " << nama1 << endl;
    cout << " Panjang string adalah " << nama1.length() << endl;
    cout << " String ke 2 adalah " << nama1[1] << endl;
    cout << " Mengganti string ke 2 dengan 'A' " << endl;
    nama1[1] = 'A';
    cout << " String setelah dirubah: " << endl;
    cout << " Nama saya adalah " << nama1 << endl;
    cout << "\n Mencari posisi string 'A' " << endl;
    cout << " Posisi string 'A' adalah " << nama1.find('A') << endl;
    cout << " Mengambil substring dari posisi 1 sebanyak 2 karakter " << endl;
    cout << " Substring adalah " << nama1.substr(1, 2) << endl;
    cout << " Mengambil substring dari posisi 1 sampai akhir " << endl;
    cout << " Substring adalah " << nama1.substr(1, nama1.length()) << endl;
    cout << "\n Input string ke 2:" << endl;
    cout << " Masukkan nama anda : " << endl;
    getline(cin, nama2);
    cout << " Menggabungkan string " << endl;
    cout << " Nama saya adalah " << nama1 + nama2 << endl;
    cout << " Mengganti string " << endl;
    nama1.replace(0, nama1.length(), nama2);
    cout << " Nama saya adalah " << nama1 << endl;
}

void array1Dimensi()
{
    cout << "Ini adalah array 1 dimensi" << endl;
    int array1[5] = {1, 2, 3, 4, 5};
    cout << "Array ke 2 adalah " << array1[1] << endl;
    cout << "Mengganti array ke 2 dengan 10 " << endl;
    array1[1] = 10;
    cout << "Array ke 2 adalah " << array1[1] << endl;
    cout << "Mengambil panjang array " << endl;
    cout << "Panjang array adalah " << sizeof(array1) / sizeof(array1[0]) << endl;
}

void array2Dimensi()
{
    cout << "Ini adalah array 2 dimensi" << endl;
    int array2[2][3] = {{1, 2, 3}, {4, 5, 6}};
    cout << "Array ke 2 adalah " << array2[1][1] << endl;
    cout << "Mengganti array ke 2 dengan 10 " << endl;
    array2[1][1] = 10;
    cout << "Array ke 2 adalah " << array2[1][1] << endl;
    cout << "Mengambil panjang array " << endl;
    cout << "Panjang array adalah " << sizeof(array2) / sizeof(array2[0]) << endl;
}

void array3Dimensi()
{
    cout << "Ini adalah array 3 dimensi" << endl;
    int array3[2][3][2] = {{{1, 2}, {3, 4}, {5, 6}}, {{7, 8}, {9, 10}, {11, 12}}};
    cout << "Array ke 2 adalah " << array3[1][1][1] << endl;
    cout << "Mengganti array ke 2 dengan 10 " << endl;
    array3[1][1][1] = 10;
    cout << "Array ke 2 adalah " << array3[1][1][1] << endl;
    cout << "Mengambil panjang array " << endl;
    cout << "Panjang array adalah " << sizeof(array3) / sizeof(array3[0]) << endl;
}

int main()
{
    int pilihan;
    bool isRunning = true;
    while (isRunning)
    {
        cout << "+----------------------------------------- +" << endl;
        cout << " Program Sederhana C++" << endl;
        cout << " Menu Utama" << endl;
        cout << " 1. Fungsi dengan default argument" << endl;
        cout << " 2. Fungsi tanpa argumen" << endl;
        cout << " 3. Fungsi dengan argumen" << endl;
        cout << " 4. Fungsi dengan nilai kembali" << endl;
        cout << " 5. Fungsi dengan nilai kembali dan argumen" << endl;
        cout << " 6. Fungsi rekursif" << endl;
        cout << " 7. Prototype" << endl;
        cout << " 8. Operasi String" << endl;
        cout << " 9. Array 1 Dimensi" << endl;
        cout << " 10. Array 2 Dimensi" << endl;
        cout << " 11. Array 3 Dimensi" << endl;
        cout << " 0. Keluar" << endl;
        cout << "+----------------------------------------- +" << endl;
        cout << " Masukkan pilihan anda : ";
        cin >> pilihan;
        switch (pilihan)
        {
        case 1:
            cout << "Anda memilih fungsi void" << endl;
            fungsidengandefaultArgument();
            break;
        case 2:
            cout << "Anda memilih fungsi tanpa argumen" << endl;
            fungsitanpaArgumen();
            break;
        case 3:
            cout << "Anda memilih fungsi dengan argumen" << endl;
            fungsidenganArgumen(10);
            break;
        case 4:
            cout << "Anda memilih fungsi dengan nilai kembali" << endl;
            cout << "Nilai kembali adalah " << fungsidenganNilaiKembali() << endl;
            break;
        case 5:
            cout << "Anda memilih fungsi dengan nilai kembali dan argumen" << endl;
            cout << "Nilai kembali adalah " << fungsidenganNilaiKembaliDanArgumen(10) << endl;
            break;
        case 6:
            cout << "Anda memilih fungsi rekursif" << endl;
            cout << "Nilai kembali adalah " << fungsiRekursif(10) << endl;
            break;
        case 7:
            cout << "Anda memilih prototype" << endl;
            cout << "Nilai kembali adalah " << prototype(10, 20) << endl;
            break;
        case 8:
            cout << "Anda memilih operasi string" << endl;
            operasiString();
            break;
        case 9:
            cout << "Anda memilih array 1 dimensi" << endl;
            array1Dimensi();
            break;
        case 10:
            cout << "Anda memilih array 2 dimensi" << endl;
            array2Dimensi();
            break;
        case 11:
            cout << "Anda memilih array 3 dimensi" << endl;
            array3Dimensi();
            break;
        case 0:
            cout << "Anda memilih keluar" << endl;
            isRunning = false;
            return 0;
        default:
            cout << "Pilihan anda tidak ada" << endl;
            break;
        }

        return 0;
    }
}

int prototype(int a, int b)
{
    cout << "Ini adalah prototype" << endl;
    cout << "Nilai yang anda masukkan adalah " << a << " dan " << b << endl;
    return a + b;
}
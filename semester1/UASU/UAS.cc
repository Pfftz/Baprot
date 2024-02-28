#include <iostream>
#include <string>

using namespace std;

void fungsidengandefaultArgument(int a = 10, int b = 20)
{
    cout << " Ini adalah fungsi dengan default argument" << endl;
    cout << " Nilai yang anda masukkan adalah " << a << " dan " << b << endl;
}

void fungsitanpaArgumen()
{
    cout << " Ini adalah fungsi tanpa argumen" << endl;
}

void fungsidenganArgumen(int a)
{
    cout << " Ini adalah fungsi dengan argumen" << endl;
    cout << " Nilai yang anda masukkan adalah " << a << endl;
}

int fungsidenganNilaiKembali()
{
    int a, b, c;
    a = 66;
    b = 77;
    c = a + b;
    return c;
}

int fungsidenganNilaiKembaliDanArgumen(int a)
{
    cout << " Ini adalah fungsi dengan nilai kembali dan argumen" << endl;
    cout << " Masukkan nilai : ";
    cin >> a;
    cout << " Nilai yang anda masukkan adalah " << a << endl;
    return a;
}

int fungsiRekursif(int a)
{
    if (a == 0)
    {
        return 1;
    }
    else
    {
        return a * fungsiRekursif(a - 1);
    }
}

int prototype(int a, int b);

void operasiString()
{
    cout << "Ini adalah operasi string" << endl;

    // Get the first string from the user
    string namaPertama;
    cout << "Masukkan nama pertama anda: ";
    cin.ignore(); // Ignore the leftover newline character in the input buffer
    getline(cin, namaPertama);

    // Display the length of the first string
    cout << "Panjang string pertama adalah " << namaPertama.length() << endl;

    // Replace the second character of the first string with 'A'
    namaPertama[1] = 'A';
    cout << "String pertama setelah dirubah: " << namaPertama << endl;

    // Find the position of 'A' in the first string
    size_t pos = namaPertama.find('A');
    if (pos != string::npos)
    {
        cout << "Posisi string 'A' adalah " << pos << endl;
    }
    else
    {
        cout << "'A' tidak ditemukan dalam string" << endl;
    }

    // Get the second string from the user
    string namaKedua;
    cout << "Masukkan nama kedua anda: ";
    getline(cin, namaKedua);

    // Concatenate the first and second strings
    string namaGabungan = namaPertama + namaKedua;
    cout << "Nama gabungan adalah " << namaGabungan << endl;

    // Replace the first string with the second string
    namaPertama.replace(0, namaPertama.length(), namaKedua);
    cout << "Nama pertama setelah diganti: " << namaPertama << endl;

    // Extract a substring from the first string
    string subNamaPertama = namaPertama.substr(0, 5);
    cout << "Sub-string dari nama pertama: " << subNamaPertama << endl;

    // Insert the second string into the first string
    namaPertama.insert(0, namaKedua);
    cout << "Nama pertama setelah disisipkan: " << namaPertama << endl;

    // Erase a part of the first string
    namaPertama.erase(0, 5);
    cout << "Nama pertama setelah dihapus: " << namaPertama << endl;

    // Compare the first and second strings
    int hasil = namaPertama.compare(namaKedua);
    if (hasil == 0)
    {
        cout << "Nama pertama dan kedua sama." << endl;
    }
    else if (hasil < 0)
    {
        cout << "Nama pertama kurang dari nama kedua." << endl;
    }
    else
    {
        cout << "Nama pertama lebih dari nama kedua." << endl;
    }
}

// Function for 1D array operations
// Function for 1D array operations
void array1Dimensi()
{
    cout << "Ini adalah array 1 dimensi" << endl;
    int array1[5] = {1, 2, 3, 4, 5};
    for (int i = 0; i < 5; i++)
    {
        cout << "Element at index " << i << " is " << array1[i] << endl;
    }
}

// Function for 2D array operations
void array2Dimensi()
{
    cout << "Ini adalah array 2 dimensi" << endl;
    int array2[2][3] = {{1, 2, 3}, {4, 5, 6}};
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cout << "Element at position [" << i << "][" << j << "] is " << array2[i][j] << endl;
        }
    }
}

// Function for 3D array operations
void array3Dimensi()
{
    cout << "Ini adalah array 3 dimensi" << endl;
    int array3[2][3][2] = {{{1, 2}, {3, 4}, {5, 6}}, {{7, 8}, {9, 10}, {11, 12}}};
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            for (int k = 0; k < 2; k++)
            {
                cout << "Element at position [" << i << "][" << j << "][" << k << "] is " << array3[i][j][k] << endl;
            }
        }
    }
}

int main()
{
    int pilihan, hasil;
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
        cout << endl;
        switch (pilihan)
        {
        case 1:
            cout << " Anda memilih fungsi dengan default argument" << endl;
            fungsidengandefaultArgument();
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 2:
            cout << " Anda memilih fungsi tanpa argumen" << endl;
            fungsitanpaArgumen();
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 3:
            cout << " Anda memilih fungsi dengan argumen" << endl;
            fungsidenganArgumen(10);
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 4:
            cout << " Anda memilih fungsi dengan nilai kembali" << endl;
            cout << " Nilai kembali adalah " << fungsidenganNilaiKembali() << endl;
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 5:
            cout << " Anda memilih fungsi dengan nilai kembali dan argumen" << endl;
            hasil = fungsidenganNilaiKembaliDanArgumen(10);
            cout << hasil << endl;
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 6:
            cout << " Anda memilih fungsi rekursif" << endl;
            cout << " Nilai kembali adalah " << fungsiRekursif(10) << endl;
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 7:
            cout << " Anda memilih prototype" << endl;
            cout << " Nilai kembali adalah " << prototype(10, 20) << endl;
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 8:
            cout << " Anda memilih operasi string" << endl;
            operasiString();
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 9:
            cout << " Anda memilih array 1 dimensi" << endl;
            array1Dimensi();
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 10:
            cout << " Anda memilih array 2 dimensi" << endl;
            array2Dimensi();
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 11:
            cout << " Anda memilih array 3 dimensi" << endl;
            array3Dimensi();
            cout << endl;
            system("pause");
            system("cls");
            break;
        case 0:
        {
            cout << " Anda memilih keluar" << endl;
            cout << endl;
            isRunning = false;
            break;
        }
        default:
            cout << endl;
            cout << " +----------------------------------------- +" << endl;
            cout << " Pilihan anda tidak ada" << endl;
            cout << " +----------------------------------------- +" << endl;
            cout << endl;
            system("pause");
            system("cls");
            break;
        }
    }
    return 0;
}

int prototype(int a, int b)
{
    return a + b;
}
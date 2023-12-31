#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <windows.h> // Windows-specific library, may not work on all platforms
using namespace std;

// Get a handle for console output
HANDLE h = GetStdHandle(STD_OUTPUT_HANDLE);

// Function to input pet data
void input(int xyz, string nama[], int kode[], string jenis[])
{
    int pilih;
    for (int o = 0; o < xyz; o++)
    {
        cout << endl;
        cout << " =============================================" << endl;
        cout << "\tData " << o + 1 << endl;
        cout << "\tNama Hewan " << o + 1 << ": ";
        cin >> nama[o];
        cout << "\tKode\t    : ";
        kode[o] = rand() % (100 - 0 + 1) + 0; // Generate a random code for the pet
        cout << kode[o] << endl;
        cout << "\tJenis Hewan : " << endl;
        cout << "\t  1. Kucing" << endl;
        cout << "\t  2. Anjing" << endl;
        cout << "\t  3. Kelinci" << endl;
        cout << "\t  4. Hamster" << endl;
        cout << "\t  5. Burung" << endl;
        cout << "\t  6. Ikan" << endl;
        cout << "\t  7. Reptil" << endl;
        cout << "\t  8. Dragon" << endl;
        cout << "\t  Pilih Jenis Hewan : ";
        cin >> pilih;
        switch (pilih)
        {
        case 1:
            jenis[o] = "Kucing";
            break;
        case 2:
            jenis[o] = "Anjing";
            break;
        case 3:
            jenis[o] = "Kelinci";
            break;
        case 4:
            jenis[o] = "Hamster";
            break;
        case 5:
            jenis[o] = "Burung";
            break;
        case 6:
            jenis[o] = "Ikan";
            break;
        case 7:
            jenis[o] = "Reptil";
            break;
        case 8:
            jenis[o] = "Dragon";
            break;
        default:
            jenis[o] = "Tidak Ada";
            break;
        }
        cout << " =============================================" << endl;
    }
}

// Function to output pet data in a table
void output(int xyz, string nama[], int kode[], string jenis[])
{
    cout << endl
         << "\n\tDaftar Data Hewan Peliharaan" << endl;
    cout << " ==============================================" << endl;
    cout << " No\tNama                "
         << "Kode\tJenis" << endl;
    cout << " ==============================================" << endl;
    for (int g = 0; g < xyz; g++)
    {
        cout << " " << g + 1 << "\t" << setw(20) << left << nama[g] << right << kode[g] << "\t    " << setw(10) << right << jenis[g]
             << endl;
    }
    cout << " ==============================================" << endl;
}

int main()
{
    int xyz;
    string opening = R"(
       _______    _______  ___________       ______        __        _______    _______      ___  ___  ___  ___  ________   
      |   __ "\  /"     "|("     _   ")     /" _  "\      /""\      /"      \  /"     "|    |"  \/"  ||"  \/"  |("      "\  
      (. |__) :)(: ______) )__/  \\__/     (: ( \___)    /    \    |:        |(: ______)     \   \  /  \   \  /  \___/   :) 
      |:  ____/  \/    |      \\_ /         \/ \        /' /\  \   |_____/   ) \/    |        \\  \/    \\  \/     /  ___/  
      (|  /      // ___)_     |.  |         //  \ _    //  __'  \   //      /  // ___)_       /\.  \    /   /     //  \__   
     /|__/ \    (:      "|    \:  |        (:   _) \  /   /  \\  \ |:  __   \ (:      "|     /  \   \  /   /     (:   / "\  
    (_______)    \_______)     \__|         \_______)(___/    \___)|__|  \___) \_______)    |___/\___||___/       \_______) 
                                                                                                                            
    )";
    SetConsoleTextAttribute(h, 3); // Set console text color to blue
    cout << endl
         << opening << endl;
    SetConsoleTextAttribute(h, 7); // Set console text color to white
    cout << "\n\n Input Data Hewan yang Akan Dititipkan: ";
    cin >> xyz;
    string nama[xyz];
    int kode[xyz];
    string jenis[xyz];
    input(xyz, nama, kode, jenis);
    output(xyz, nama, kode, jenis);
    return 0;
}

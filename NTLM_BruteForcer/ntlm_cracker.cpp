#include "headers/ntlm_object.hpp"
#include <fstream>
// Author : Unam3dd
// Windows Compile : g++ .\headers\NTLM.cpp .\headers\ntlm_object.cpp .\ntlm_cracker.cpp -std=c++11 -o ntlm_cracker.exe

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
   //define something for Windows (32-bit and 64-bit, this part is common)
   #ifdef _WIN64
      #define CLEAR_COMMAND "cls"
   #else  
      #define CLEAR_COMMAND "cls"
   #endif
#else
    #define CLEAR_COMMAND "clear"
#endif

using namespace std;

string banner = "0a5f20205f205f5f5f205f202020205f20205f202020205f5f5f5f205f5f5f5f205f5f5f5f205f5f5f5f205f20205f205f5f5f5f205f5f5f5f200a7c5c207c20207c20207c202020207c5c2f7c202020207c202020207c5f5f2f207c5f5f7c207c202020207c5f2f20207c5f5f5f207c5f5f2f200a7c205c7c20207c20207c5f5f5f207c20207c202020207c5f5f5f207c20205c207c20207c207c5f5f5f207c205c5f207c5f5f5f207c20205c200a2020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020200a";


string decode_hex(string hex){
    string decoded;
    int size_hex = hex.length();
    for (int i = 0;i<size_hex;i+=2){
        string b = hex.substr(i,2);
        char chr = (char) (int)strtol(b.c_str(),NULL,16);
        decoded.push_back(chr);
    }
    return decoded;
}

void show_banner()
{
    string b = decode_hex(banner);
    cout << "   \033[38;5;82m" << b << endl;
    cout << "                      Author : \033[38;5;196mUnam3dd\033[38;5;82m" << endl;
    cout << "                    [ Github : \033[38;5;196mUnam3dd\033[38;5;82m ]" << endl << endl;
    cout << "                 Simple NTLM Hash Tools in C++\033[00m" << endl;
}

void show_help()
{
    cout << "\033[38;5;82m                     --help                    | Show Help" << endl;
    cout << "                     --hash <string>           | Get hash from a String" << endl;
    cout << "                     --crack <hash> <wordlist> | Brute Force Hash with wordlist" << endl;
    cout << "                     --vcrack <hash> <wordlist>| Brute Force Hash with wordlist and Verbose options\033[00m" << endl;
    return;
}

void get_hash(string str)
{
    NTLM_Hash _hash(str);
    cout << "[ \033[38;5;82mOK\033[00m ] Hash of \033[38;5;82m" << str << "\033[00m" << endl;
    cout << "[ \033[38;5;82mOK\033[00m ] Hash   : \033[38;5;82m" << _hash.get_hash() << "\033[00m" << endl;
    cout << "[ \033[38;5;82mOK\033[00m ] String : \033[38;5;82m" << str << "\033[00m" << endl;
    return;
}

int crack_hash(string target_hash, string wordlist)
{
    char gline[255];
    string password_hash;
    int x = 0;

    ifstream i(wordlist);
        
    if (i.is_open())
    {
        memset(gline,0,sizeof(gline));
        cout << "\n\n" << endl;
        while (i)
        {
            i.getline(gline,255);
            NTLM_Hash h((string)gline);
            password_hash = h.get_hash();
            if (password_hash == target_hash)
            {
                cout << "\n\n[ \033[38;5;82mOK\033[00m ] Hash Found !" << endl;
                cout << "[ \033[38;5;82mOK\033[00m ] Target Hash : \033[38;5;82m" << target_hash << "\033[00m" << endl;
                cout << "[ \033[38;5;82mOK\033[00m ] Password Hash : \033[38;5;82m" << (string)gline << "\033[00m" << endl;
                x = 1;
                break;
            }
            else
            {
                password_hash.clear();
                memset(gline,0,sizeof(gline));
            }
        }
        
        if (x == 1)
        {
            return 0;
        }
        else
        {
            cout << "\n\n[ \033[38;5;196mFAILED\033[00m ] Password Not Found in " << wordlist << endl;
            return 1;
        }
    }
    else
    {
        cout << "[ \033[38;5;196mFAILED\033[00m ] Error : " << wordlist << " Can't be opened !" << endl;
        return 1;
    }
}

int vcrack_hash(string target_hash, string wordlist)
{
    char gline[255];
    string password_hash;
    int x = 0;

    ifstream i(wordlist);
        
    if (i.is_open())
    {
        memset(gline,0,sizeof(gline));
        cout << "\n\n" << endl;
        while (i)
        {
            i.getline(gline,255);
            NTLM_Hash h((string)gline);
            password_hash = h.get_hash();
            if (password_hash == target_hash)
            {
                system(CLEAR_COMMAND);
                show_banner();
                cout << "\n\n[ \033[38;5;82mOK\033[00m ] Hash Found !" << endl;
                cout << "[ \033[38;5;82mOK\033[00m ] Target Hash : \033[38;5;82m" << target_hash << "\033[00m" << endl;
                cout << "[ \033[38;5;82mOK\033[00m ] Password Hash :\033[38;5;82m " << (string)gline << "\033[00m" << endl;
                x = 1;
                break;
            }
            else
            {
                cout << "[ \033[38;5;196mFAILED\033[00m ] Try : \033[38;5;202m" << (string)gline << "\033[00m" << endl;
                password_hash.clear();
                memset(gline,0,sizeof(gline));
            }
        }
        
        if (x == 1)
        {
            return 0;
        }
        else
        {
            cout << "\n\n[ FAILED ] Hash Not Cracked : Password Not Found in " << wordlist << endl;
            return 1;
        }
    }
    else
    {
        cout << "[ FAILED ] Error : " << wordlist << " Can't be opened !" << endl;
        return 1;
    }
}

int main(int argc, char *argv[])
{
    string options;
    show_banner();
    if (argc < 2)
    {
        show_help();
    }
    else
    {
        options = argv[1];

        if (options == (string)"--help")
        {
            cout << "usage : " << argv[0] << endl;
            show_help();
        }

        else if (options == (string)"--hash")
        {
            get_hash((string)argv[2]);
        }

        else if (options == (string)"--crack")
        {
            if (argc < 3)
            {
                cout << "[ \033[38;5;196mFAILED\033[00m ] Invalid Options " << endl;
                cout << "usage  : " << argv[0] << endl;
                show_help();
            }
            else
            {
                int i = crack_hash((string)argv[2],(string)argv[3]);
                if (i == 0)
                {
                    exit(0); // Hash Cracked !
                }
                else
                {
                    exit(1); // Hash Not Cracked !
                }
            }
        }

        else if (options == (string)"--vcrack")
        {
            if (argc < 3)
            {
                cout << "[ \033[38;5;196mFAILED\033[00m ] Invalid Options " << endl;
                cout << "\033[38;5;82musage  : " << argv[0] << endl;
                show_help();
            }
            else
            {
                int i = vcrack_hash((string)argv[2],(string)argv[3]);
                if (i == 0)
                {
                    exit(0);
                }
                else
                {
                    exit(1);
                }
            }
            
        }

        else
        {
            cout << "[ \033[38;5;196mFAILED\033[00m ] Invalid Options !" << endl;
            cout << "\033[38;5;82musage : " << argv[0] << endl;
            show_help();
        }
        return 0;
    }
    
    return 1;
}
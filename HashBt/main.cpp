#include "hashbt.h"

using namespace std;

int main(int argc,char *argv[])
{
    if (argc < 2)
    {
        cout << "By Unam3dd Simple Hash Bruter With HashLibrary" << endl;
        cout << "My Project : https://github.com/Unam3dd/HashBt" << endl;

        cout << "HashLibrary Project : https://github.com/stbrumme/hash-library" << endl;

        cout << "usage : " << argv[0] << " --help" << endl;
        cout << "        " << argv[0] << " md5 <hash> <wordlist>" << endl;
        cout << "        " << argv[0] << " sha256 <hash> <wordlist>" << endl;
        cout << "        " << argv[0] << " get <string> <format>" << endl;
        cout << "\n\n" << endl;
    }
    else
    {
        HashBt bt;
        
        if (strcmp(argv[1],"md5")==0)
        {
            string target_hash = argv[2];
            string filename = argv[3];
            if (bt.check_file_exists(filename) == 1)
            {
                bt.crack_md5hash(target_hash,filename);
            }
            else
            {
                cout << "[!] " << filename << " Not Found !" << endl;
            }
        }

        else if (strcmp(argv[1],"sha256")==0)
        {
            string target_hash = argv[2];
            string filename = argv[3];
            if (bt.check_file_exists(filename)==1)
            {
                bt.crack_sha256hash(target_hash,filename);
            }
            else
            {
                cout << "[!] " << filename << " Not Found !" << endl;
            }
        }

        else if (strcmp(argv[1],"get")==0)
        {
            if (strcmp(argv[3],"md5")==0)
            {
                HashBt h;
                cout << "[+] Hash MD5   : " << h.md5hash((string)argv[2]) << endl;
                cout << "[+] Raw String : " << argv[2] << endl;
            }

            else if (strcmp(argv[3],"sha256")==0)
            {
                HashBt h;
                cout << "[+] Hash SHA256 : " << h.sha256_hash((string)argv[2]) << endl;
                cout << "[+] Raw String  : " << argv[2] << endl;
            }

            else
            {
                cout << "[!] Unknown Type Hash" << endl;
            }
            
        }

        else if (strcmp(argv[1],"--help")==0)
        {
            cout << "By Unam3dd Simple Hash Bruter With HashLibrary" << endl;
            cout << "My Project : https://github.com/Unam3dd/HashBt" << endl;

            cout << "HashLibrary Project : https://github.com/stbrumme/hash-library" << endl;

            cout << "usage : " << argv[0] << " --help" << endl;
            cout << "        " << argv[0] << " md5 <hash> <passlist>" << endl;
            cout << "        " << argv[0] << " sha256 <hash> <passlist>" << endl;
            cout << "        " << argv[0] << " sha1 <hash> <passlist>" << endl;
            cout << "        " << argv[0] << " get <string> <format>" << endl;
            cout << "\n\n" << endl;
        }

        else
        {
            cout << "[!] Unknown Type Hash !" << endl;
        }
    }   
    return 0;
}
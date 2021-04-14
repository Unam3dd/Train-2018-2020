#include "hashbt.h"

using namespace std;

string HashBt::get_time_now()
{
    time_t t = time(0);
    struct tm time_struct;
    char buffer[100];
    memset(buffer,0,sizeof(buffer));
    time_struct = *localtime(&t);
    strftime(buffer,sizeof(buffer),"%X",&time_struct);
    return buffer;
}

string HashBt::md5hash(string raw_str)
{
    MD5 md5;
    string output = md5(raw_str);
    return output;
}

string HashBt::sha256_hash(string raw_str)
{
    SHA256 sha256;
    string output = sha256(raw_str);
    return output;
}

bool HashBt::check_file_exists(string filename)
{
    struct stat file;
    return (stat(filename.c_str(),&file) == 0);
}

void HashBt::crack_md5hash(string hashstr,string passlist)
{
    HashBt b;
    ifstream f(passlist);
    char password[1024];
    string password_hash;
    cout << "[+] MD5 Hash : " << hashstr << endl;
    cout << "[+] Wordlist : " << passlist << endl;
    while (f)
    {
        f.getline(password,1024);
        password_hash = b.md5hash((string)password);
        if (hashstr == password_hash)
        {
            cout << "[" << get_time_now() << "] Hash MD5 => " << hashstr << endl;
            cout << "[" << get_time_now() << "] Hash Cracked => " << (string)password << endl;
            break;
        }
        else
        {
            cout << "[" << get_time_now() << "] Try Word => " << (string)password << endl;
            password_hash.clear();
            memset(password,0,sizeof(password));
        }
    }
    
    if (hashstr == password_hash)
    {
        cout << "[+] Hash Cracked SucessFully !" << endl;
    }
    else
    {
        cout << "[!] Hash Not Found !" << endl;
    }
}

void HashBt::crack_sha256hash(string hashstr,string passlist)
{
    HashBt b;
    ifstream f(passlist);
    char password[1024];
    string password_hash;
    cout << "[+] SHA256 Hash : " << hashstr << endl;
    cout << "[+] Wordlist : " << passlist << endl;
    while (f)
    {
        f.getline(password,1024);
        password_hash = b.sha256_hash((string)password);
        if (hashstr == password_hash)
        {
            cout << "[" << get_time_now() << "] Hash SHA256 => " << hashstr << endl;
            cout << "[" << get_time_now() << "] Hash Cracked => " << (string)password << endl;
            break;
        }
        else
        {
            cout << "[" << get_time_now() << "] Try Word => " << (string)password << endl;
            password_hash.clear();
            memset(password,0,sizeof(password));
        }
    }
    
    if (hashstr == password_hash)
    {
        cout << "[+] Hash Cracked SucessFully !" << endl;
    }
    else
    {
        cout << "[!] Hash Not Found !" << endl;
    }
}
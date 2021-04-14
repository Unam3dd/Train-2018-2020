#include <iostream>
#include <fstream>
#include <ctime>
#include <cstring>
#include <sys/stat.h>
#include "sha256.h"
#include "md5.h"

using namespace std;

class HashBt
{
    public:
        string md5hash(string raw_str);
        void crack_md5hash(string raw_str,string passlist);
        bool check_file_exists(string filename);
        string sha256_hash(string raw_str);
        void crack_sha256hash(string hashstr,string passlist);
    
    private:
        string get_time_now();
};
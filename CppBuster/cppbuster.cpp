//compile : g++ cppbuster.cpp -o cppbuster -lcpr -lcurl -lpthread
#include <iostream>
#include <time.h>
#include <fstream>
#include <stdio.h>
#include <string>
#include <cpr/cpr.h>
#include <unistd.h>
#include <thread>
#include <sys/stat.h>
#include <vector>
#include <stdexcept>

using namespace std;

vector<string> PUSH_URL_LIST;
vector<string> URL_FOR;

bool check_file_exists(const char *filename)
{
    struct stat file;
    return (stat(filename,&file) ==0);   
}

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


int send_http_requests(string url)
{
    auto r = cpr::Get(cpr::Url{url});
    int status_code = r.status_code;
    if (status_code == 200)
    {
        return 1;
    } else {
        return 0;
    }
}

string get_time_now()
{
    time_t t = time(0);
    struct tm time_struct;
    char buffer[100];
    time_struct = *localtime(&t);
    strftime(buffer,sizeof(buffer),"%X",&time_struct);
    return buffer;
}

void *get_url_cpp_thread(string url)
{
    int r = send_http_requests(url);
    if(r == 1)
    {
        cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] Dir Found -> \e[38;5;87m" << url << "\033[00m" << endl;
        PUSH_URL_LIST.push_back(url);
    }
    return NULL;
}

void *get_url_cpp_thread_verbose(string url)
{
    int r = send_http_requests(url);
    if(r == 1)
    {
        cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] Dir Found -> \e[38;5;87m" << url << "\033[00m" << endl;
        PUSH_URL_LIST.push_back(url);
    } else {
        cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] Dir Failed -> \e[38;5;160m" << url << "\033[00m" << endl;
    }
    return NULL;
}

void cpp_start_buster_verbose_no_extension(char *dirlist,char *url)
{
    string str_url = url;
    if (check_file_exists(dirlist)==1)
    {
        cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] " << dirlist << " found !" << endl;
        ifstream in(dirlist);
            
        if(!in)
        {
            cout << "\e[38;5;160m[!] " << dirlist << " Cannot open input file !" << endl;
        } else {
            char dir[255];
            cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] Loading Dir list.." << endl;
            while (in)
            {
                in.getline(dir, 255);
                URL_FOR.push_back(str_url+dir);
            }
            int size_vector = URL_FOR.size();
            cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] Dir Loadeds : \e[38;5;87m" << size_vector << "\033[00m" << endl;
            
            for (int i = 0;i<size_vector;i++)
            {
                thread thread_id(get_url_cpp_thread_verbose,URL_FOR[i]);
                thread_id.join();
            }

            cout << "\n\n\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] ===================== URL FOUND =====================\033[00m" << endl;

            for (int x=0;x<PUSH_URL_LIST.size();x++)
            {
                cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] URL : \e[38;5;87m" << PUSH_URL_LIST[x] << "\033[00m" << endl;
            }
        }
    } else {
        cout << "\e[38;5;160m[!] " << dirlist << " Not found !" << endl;
    }
}

void cpp_start_buster_no_verbose_no_extension(char *dirlist,char *url)
{
    string str_url = url;
    if (check_file_exists(dirlist)==1)
    {
        cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] " << dirlist << " found !" << endl;
        ifstream in(dirlist);
            
        if(!in)
        {
            cout << "\e[38;5;160m[!] " << dirlist << " Cannot open input file !" << endl;
        } else {
            char dir[255];
            cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] Loading Dir list.." << endl;
            while (in)
            {
                in.getline(dir, 255);
                URL_FOR.push_back(str_url+dir);
            }
            int size_vector = URL_FOR.size();
            cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] Dir Loadeds : \e[38;5;87m" << size_vector << "\033[00m" << endl;
            
            for (int i = 0;i<size_vector;i++)
            {
                thread thread_id(get_url_cpp_thread,URL_FOR[i]);
                thread_id.join();
            }

            cout << "\n\n\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] ===================== URL FOUND =====================\033[00m" << endl;

            for (int x=0;x<PUSH_URL_LIST.size();x++)
            {
                cout << "\e[38;5;82m[\e[38;5;87m" << get_time_now() << "\e[38;5;82m] URL : \e[38;5;87m" << PUSH_URL_LIST[x] << "\033[00m" << endl;
            }
        }
    } else {
        cout << "\e[38;5;160m[!] " << dirlist << " Not found !" << endl;
    }
}

int main(int argc,char *argv[])
{
    string banner = "0a205f5f202020205f5f5f2020205f5f5f2020205f5f5f2020205f20202020205f5f20205f5f5f5f5f20205f5f5f5f20205f5f5f20200a2f202f6020207c207c5f29207c207c5f29207c207c5f29207c207c207c202820286020207c207c20207c207c5f20207c207c5f29200a5c5f5c5f2c207c5f7c2020207c5f7c2020207c5f7c5f29205c5f5c5f2f205f295f2920207c5f7c20207c5f7c5f5f207c5f7c205c200a";
    string d_h = decode_hex(banner);
    cout << "\e[38;5;82m" << d_h << endl;
    cout << "\n" << "      [ Github : Unam3dd ] " << endl;
    cout << "      [ Version 0.1 ]\033[00m\n" << endl;
    if (argc < 2)
    {
        cout << "\n" << endl;
        cout << "       usage           : " << argv[0] << " <url> <dirlist>" << endl;
        cout << "       exemple         : " << endl;
        cout << "       Basic Usage     : " << argv[0] << " <url> <dirlist>" << endl;
        cout << "       Verbose Usage   : " << argv[0] << " <url> <dirlist> -v" << endl;
        cout << "\n\n" << endl;
    } else
    {
        if (argc > 3)
        {
            try
            {
                if (strcmp(argv[3],"-v")==0)
                {
                    cpp_start_buster_verbose_no_extension(argv[2],argv[1]);
                } else {
                    cout << "\e[38;5;160m[!] Error Options !" << endl;
                    cout << "\n" << endl;
                    cout << "       usage           : " << argv[0] << " <url> <dirlist>" << endl;
                    cout << "       exemple         : " << endl;
                    cout << "       Basic Usage     : " << argv[0] << " <url> <dirlist>" << endl;
                    cout << "       Verbose Usage   : " << argv[0] << " <url> <dirlist> -v" << endl;
                    cout << "\n\n" << endl;
                }
            }
            catch (const out_of_range& orr)
            {
                cout << "\e[38;5;160m[!] Error Out Of Range ! : " << orr.what() << endl;
            }
        } else {
            cpp_start_buster_no_verbose_no_extension(argv[2],argv[1]);
        }
        return 0;
    }
    return -1;
}
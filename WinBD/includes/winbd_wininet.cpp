#include "winbd_wininet.h"

using namespace std;

vector<string> split_link(const string& s, char delim) {
    vector<string> result;
    stringstream ss(s);
    string item;

    while (getline(ss, item, delim)) {
        result.push_back(item);
    }

    return result;
}

string path_link(string link) {
    string result;

    int end_char = link.size() - 1;
    vector<string> split_string = split_link(link, '/');
    int vector_split_size = split_string.size();
    vector<string> split_string2 = split_link(split_string[0].c_str(), ':');

    for (int iter = 3; iter < vector_split_size; iter++) {
        //cout << split_string[iter] << endl;
        result.append("/");
        result.append(split_string[iter]);
    }

    return result;
}


int download_to_ftp(char* filename, char* ftp_host, int ftp_port, char* ftp_user, char* ftp_pass)
{
    HINTERNET hNet;
    hNet = InternetOpen("Ftp", INTERNET_OPEN_TYPE_DIRECT, 0, 0, 0);
    if (hNet != INVALID_HANDLE_VALUE)
    {
        HINTERNET hFtp = InternetConnect(hNet, ftp_host, ftp_port, ftp_user, ftp_pass, INTERNET_SERVICE_FTP, INTERNET_FLAG_PASSIVE, 0);
        if (hFtp != INVALID_HANDLE_VALUE)
        {
            if (FtpPutFile(hFtp, filename, filename, FTP_TRANSFER_TYPE_BINARY, 0))
            {
                return 0; // file envoyer au ftp
            }
            else {
                return -1; // file error
            }
            InternetCloseHandle(hFtp);
        }
    }
}

int download_on_ftp(char* filename, char* ftp_host, int ftp_port, char* ftp_user, char* ftp_pass)
{
    HINTERNET hNet;
    hNet = InternetOpen("Ftp", INTERNET_OPEN_TYPE_DIRECT, 0, 0, 0);
    if (hNet != INVALID_HANDLE_VALUE)
    {
        HINTERNET hFtp = InternetConnect(hNet, ftp_host, ftp_port, ftp_user, ftp_pass, INTERNET_SERVICE_FTP, INTERNET_FLAG_PASSIVE, 0);
        if (hFtp != INVALID_HANDLE_VALUE)
        {
            if (FtpGetFile(hNet, filename, filename, TRUE, FILE_ATTRIBUTE_NORMAL, FTP_TRANSFER_TYPE_BINARY, 0)) {
                return 0;
            }
            else {
                return -1;
            }
            InternetCloseHandle(hFtp);
        }
    }
}


void send_http_get(string url,struct http_struct *wbd)
{
    HINTERNET hInternet, hFile;
    string return_buffer = "";
    char buffer[4096];
    DWORD bytes_reads;
    int finish = 0;


    DWORD statlen = 0;
    char status_code[4096];
    statlen = sizeof(status_code);
    char status_text[4096];

    hInternet = InternetOpen("Winbd Version 0.6", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    if (hInternet == NULL)
    {
        cout << "Error !" << endl;
    }

    hFile = InternetOpenUrl(hInternet,(LPCSTR)url.c_str(), NULL, 0, 0, 0);

    if (hFile == NULL)
    {
        cout << "Error !" << endl;
    }

    
    HttpQueryInfo(hFile, HTTP_QUERY_STATUS_CODE, status_code, &statlen, NULL);
    wbd->status_code = status_code;
    HttpQueryInfo(hFile, HTTP_QUERY_STATUS_TEXT, status_text, &statlen, NULL);
    wbd->status_text = status_text;

    while (!finish)
    {
        if (InternetReadFile(hFile, buffer, sizeof(buffer), &bytes_reads))
        {
            if (bytes_reads > 0)
            {
                return_buffer += buffer;
            }
            else
            {
                finish = 1;
            }
        }
        else
        {
            printf("InternetReadFile Failed\n");
            finish = 1;
        }
    }

    wbd->content = return_buffer;

    InternetCloseHandle(hInternet);
    InternetCloseHandle(hFile);
    return;
}

void send_https_get(string url, struct http_struct* wbd)
{
    HINTERNET hInternet, hFile;
    string return_buffer = "";
    char buffer[4096];
    DWORD bytes_reads;
    int finish = 0;


    DWORD statlen = 0;
    char status_code[4096];
    statlen = sizeof(status_code);
    char status_text[4096];

    hInternet = InternetOpen("Winbd Version 0.6", INTERNET_OPEN_TYPE_DIRECT, NULL, NULL, 0);
    if (hInternet == NULL)
    {
        cout << "Error !" << endl;
    }

    hFile = InternetOpenUrl(hInternet, (LPCSTR)url.c_str(), NULL, 0,INTERNET_FLAG_SECURE, 0);

    if (hFile == NULL)
    {
        cout << "Error !" << endl;
    }


    HttpQueryInfo(hFile, HTTP_QUERY_STATUS_CODE, status_code, &statlen, NULL);
    wbd->status_code = status_code;
    HttpQueryInfo(hFile, HTTP_QUERY_STATUS_TEXT, status_text, &statlen, NULL);
    wbd->status_text = status_text;

    while (!finish)
    {
        if (InternetReadFile(hFile, buffer, sizeof(buffer), &bytes_reads))
        {
            if (bytes_reads > 0)
            {
                return_buffer += buffer;
            }
            else
            {
                finish = 1;
            }
        }
        else
        {
            printf("InternetReadFile Failed\n");
            finish = 1;
        }
    }

    wbd->content = return_buffer;

    InternetCloseHandle(hInternet);
    InternetCloseHandle(hFile);
    return;
}
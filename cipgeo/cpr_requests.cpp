//apt install libjson-c-dev or libjson
//json-c for Microsoft vcpkg install json-c
//compile : g++ project.cpp -o pro -lcpr -lcurl -ljson-c

#include <stdio.h>
#include <cpr/cpr.h>
#include <iostream>
#include <string>
#include <json-c/json.h>

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        printf("usage : %s <ip>\n",argv[0]);
    }
    else{
        char link[4096];
        sprintf(link,"https://ipinfo.io/%s/geo",argv[1]);
        auto r = cpr::Get(cpr::Url{link});

        int status_code = r.status_code;
        if (status_code ==200){
            printf("Status Code : %d\n",status_code);
            std::string res_json = r.text;
            const char *res_json_char = res_json.c_str();
            struct json_object *parsed;
            struct json_object *ip;
            struct json_object *city;
            struct json_object *region;
            struct json_object *country;
            struct json_object *loc;

            parsed = json_tokener_parse(res_json_char);
            json_object_object_get_ex(parsed, "ip", &ip);
            json_object_object_get_ex(parsed, "city", &city);
            json_object_object_get_ex(parsed, "region", &region);
            json_object_object_get_ex(parsed, "country", &country);
            json_object_object_get_ex(parsed, "loc", &loc);

            char ip_get[4096];
            char city_get[4096];
            char loc_get[4096];
            char country_get[4096];
            char region_get[4096];

            sprintf(ip_get,"IP : \033[31m%s\033[00m\n",json_object_get_string(ip) );
            sprintf(city_get, "CITY : \033[31m%s\033[00m\n", json_object_get_string(city));
            sprintf(loc_get,"Location : \033[31m%s\033[00m\n", json_object_get_string(loc));
            sprintf(country_get, "Country: \033[31m%s\033[00m\n", json_object_get_string(country));
            sprintf(region_get, "Region : \033[31m%s\033[00m\n",json_object_get_string(region));

            std::cout << ip_get << std::endl;
            std::cout << city_get << std::endl;
            std::cout << country_get << std::endl;
            std::cout << region_get << std::endl,
            std::cout << loc_get << std::endl;
        } else {
            printf("Status Code : %d\n",status_code);
        }
        return 0;
    }
}
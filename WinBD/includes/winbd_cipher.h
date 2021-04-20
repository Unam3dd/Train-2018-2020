#pragma once
#include <iostream>
#include <string.h>
#include <sstream>

using namespace std;

class Cipher
{
public:
	string xor_data_hex(string raw_data, char key[]);
	string hex_data(string buffer);
	string xor_data(string raw_data, char key[]);
	string hex_format_raw(string hex_data);
	string not_data(string raw_data,char key[]);
};
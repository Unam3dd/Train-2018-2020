#include "winbd_cipher.h"

using namespace std;

string Cipher::xor_data_hex(string raw_data, char key[])
{
	string xor_e = raw_data;
	string xor_string;
	string xor_ee;
	for (int x = 0; x < xor_e.size(); x++)
	{
		xor_e[x] = raw_data[x] ^ key[x % (strlen(key) / sizeof(char))];
		xor_ee = xor_e[x];
		xor_string += hex_data(xor_ee);
	}

	return  xor_string;
}


string Cipher::hex_data(string buffer)
{
	char char_;
	string hex_string;
	for (int i = 0; i < buffer.size(); i++)
	{
		stringstream hs;
		char_ = buffer.at(i);
		hs << hex << (int)char_;
		hex_string += hs.str();
	}
	return hex_string;
}

string Cipher::xor_data(string raw_data, char key[])
{
	string xor_e = raw_data;
	for (int i = 0; i < xor_e.size(); i++)
	{
		xor_e[i] = xor_e[i] ^ key[i % (strlen(key) / sizeof(char))];
	}
	return xor_e;
}


string Cipher::hex_format_raw(string hex_data)
{
	string thexx = hex_data;
	int size_hex = thexx.size();
	string format_hex;

	for (int i = 0; i < size_hex; i++)
	{
		if (i % 2 == 0)
		{
			format_hex.append("\\x");
			format_hex += thexx[i];
		}
		else
		{
			format_hex += thexx[i];
		}
	}

	return format_hex;
}


string Cipher::not_data(string raw_data, char key[])
{
	string not_e = raw_data;
	for (int x = 0; x < not_e.size(); x++)
	{
		not_e[x] = ~raw_data[x] ^ key[x % (strlen(key) / sizeof(char))];
	}
	return not_e;
}
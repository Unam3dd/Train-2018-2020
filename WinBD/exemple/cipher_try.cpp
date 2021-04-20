#include "winbd_cipher.h"

using namespace std;

int main()
{
	Cipher cp;
	string lol = "hello";
	char key[5] = { 'A','B','C','D','E' };
	string d = cp.xor_data_hex(lol, key);
	cout << cp.xor_data(lol, key) << endl;
	cout << d << endl;
	cout << cp.hex_format_raw(d) << endl;
	cout << cp.not_data(lol, key) << endl;
	return 0;
}
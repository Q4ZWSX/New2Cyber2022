# Tunneler

AUTHOR NOTE: If any of these are incorrect or you have solutions to ones I couldn't solve send me a message

## 0x01 Bastion

![img](https://lh6.googleusercontent.com/mP6nqQKtTR6vEQr8vM5jpKq_EThINWRo0Jurrv8PE25bLFbvE1j-7xLHI1OgtXxsn5MG18FPkXgbdeHSv5o9djYSjSIiCYtfBeGCXljqg_a5gBFnEprmtdEz1PfKtbbn1Z8K8Vc9)

##### Prompt: Connect to the bastion host tunneler.threatsims.com User: tunneler Password: tunneler SSH Port: 2222

ssh tunneler@tunneler.threatsims.com -p 2222
tunneler is password
**ts{SSHtoANonStandardPort}**



## 0x02 Browsing Websites

![img](https://lh3.googleusercontent.com/TRhRJmyfB9tGRLDVL1D-qctXY_0TRdRrxpcdPzN89j9MGikZAGEtstV-hTccymyrWI1uPxEMVgsfb-S9BRk1XmUD0tDJsSWRwnMeCxbkFiOSLa69_Fs5l3rOB8qHHysz1sOARyij)

##### Prompt: Browse to http://10.174.12.14/

ssh tunneler@tunneler.threatsims.com -p 2222 -L 8000:10.174.12.14:80
Forwards the port to 10.174.12.14:80
Connect to in browser
http://localhost:8000/
**ts{TheFirstTunnelIsTheEasiest}**



## 0x03 SSH in tunnels

![img](https://lh5.googleusercontent.com/T4CpOyN9S880XTymdOd3y-HIWA2F87O9r50FB6LsL09sTnl1XbjHJFuOvxo1uOIviQaLoONFR8vOmlENIE-BMl9Rchb6nR8TcGhskJA7Lj2ibycIr2PfQo1IKWzw1vJiyPfkE0yJ)

##### Prompt: SSH through the bastion to the pivot. IP: 10.218.176.199 User: whistler Pass: cocktailparty

ssh -J tunneler@tunneler.threatsims.com:2222 whistler@10.218.176.199
First password: tunneler
Second password: cocktailparty
**ts{IThoughtWeLostYouOnTheWay}**



## 0x04 Beacons everywhere

![img](https://lh5.googleusercontent.com/Jgg8TcGFFKDbcTmu2H138eL680TxEUBtNAdT4LSdIRanOzvlfFzb67Ttf0qfbAZjXHSva_X_mrh1wzNIB6K097WzY2eZyuJMtanPYMIu0dB9zo4NOdXoayto_q3XwVaFZ7CBipD3)

##### Prompt: Something is Beaconing to the pivot on port 58671-58680 to ip 10.112.3.199, can you tunnel it back? NOTE: IT IS THE SAME ON EACH PORT ONLY USE ONE PORT AND REMOVE YOUR TUNNEL WHEN YOU ARE DONE

ssh -J tunneler@tunneler.threatsims.com:2222 whistler@10.218.176.199 -R 10.112.3.199:58671:127.0.0.1:3000
First password: tunneler
Second password: cocktailparty

Another terminal window
nc -lvnp 3000 
Wait a minute or so and you’ll get the flag inside a bunch of gibberish
**ts{GreatFirstReverseTunnel}**



## 0x07 Another Pivot

![img](https://lh5.googleusercontent.com/XsuOOhSDyXVFdxjrXbr4Gn3FLIhN36oGvrpABv7OAsxzyhQZubV9RCHg1rlkOp3faxKgVQA79wknl7tnzEWFjcibpiqNbKltS35fWk8dTXA6Rh1kTqJYYhfAB2XogB_5vBBTEczf)

##### Prompt: Connect to the second pivot IP: 10.112.3.12 User: crease Pass: NoThatsaV

No idea why there was a weird change in numbers but this one is fairly easy
ssh -J tunneler@tunneler.threatsims.com:2222,whistler@10.218.176.199 crease@10.112.3.12
First password: tunneler
Second password: cocktailparty
Third password: NoThatsaV
**ts{TunnelsInTunnelsInTunnels}**



## 0x05 Beacons annoying

![img](https://lh5.googleusercontent.com/Ov3YcXGvHXL9njrSmAjqDY0O9CewqMyj1N5X1cWbFhW49R_bU6YxbiMJszbVAe3fF5pOoRUe1yjNBwSczXzNrfoGms4eG1i_q71Q1dR828xbIuzLuj2ljjnW6xnoVwrm01NmLD6n)

##### Prompt: Connect to ip: 10.112.3.88 port: 7000, a beacon awaits you

ssh -J tunneler@tunneler.threatsims.com:2222 whistler@10.218.176.199 -L 7000:10.112.3.88:7000
First password: tunneler
Second password: cocktailparty
nc -vn 127.0.0.1 7000
Returns a port which in 15 seconds will spit out a flag
ssh -J tunneler@tunneler.threatsims.com:2222 whistler@10.218.176.199 -R 10.112.3.199:PORTGIVEN:127.0.0.1:1234
nc -vn 127.0.0.1 1234
I HATED THIS CHALLENGE
Eventually with some persistence you’ll get it quick enough
ts{YourTunnelGameisAlright}



## 0x06 Scan me

![img](https://lh3.googleusercontent.com/jLbLQzaejg0XR-u2ApJrjHnUHM0rhX9-UegATYLdMFRE8DEypKADQn-wkSJvwejCfTfDGh_wd-zpUDKKR54GpRecPVeJDyxAThMRVrqR9TopWbVaSb2oJ2zMkYTgKsQuEe6-twbM)

##### Prompt: We deployed a ftp server but we forgot which port, find it and connect ftp: 10.112.3.207 user: bishop pass: geese

We now see why 0x07 was placed before 0x06
In 0x07 there was a copy of socat, a relay tool which we can use
ssh -J tunneler@tunneler.threatsims.com:2222,whistler@10.218.176.199 crease@10.112.3.12
First password: tunneler
Second password: cocktailparty
Third password: NoThatsaV
for i in `seq 1 65535`; do socat - TCP:10.112.3.207:$i ; done 2>/dev/null
Result is flag
**ts{SocatTunnelsForTheWin}**



## 0x08 snmp

![img](https://lh4.googleusercontent.com/IGhN1HohM1TQmvlq653Yt7IzqdjfeK18E_fSlrEiYOJwmbjeyzYN-8c_eTDmLt0NGGX4Q1-8e6L8sjITJyFXdfzyG52Ui5-bGw8uyntldeyE4QaTAu1IhSfGLRjmah9vCgUTRTrO)

##### Prompt: There is a snmp server at 10.24.13.161

Note: It was at this point in the challenge I found a writeup for a similar challenge which I used for the remaining two

https://github.com/hyperreality/ctf-writeups/tree/master/2020-defcon-redteamvillage


# crypto-ciphers-n-encodings

AUTHOR NOTE: If any of these are incorrect or you have solutions to ones I couldn't solve send me a message

## Mind the padding

![img](https://lh4.googleusercontent.com/qjZqTi_LS0cF194pldSFSIpiKBix65XyoSvxCLaN7e5fYgftvxS3OHmGNM7fEfhYtDfw1EPkRdDvkUqZ2dLIvgQ0a1hL-LWmppS8ygQAhNbz5ArjTI05VBL6AhYOsWorWzoLxBcA)



##### Prompt: You'll need a pad for this one. Key is the most famous animal of 2020 ma{qmeg}

Interesting problem because I’m pretty sure there was an error on the writers part

‘Tigers’ are the most popular animal in 2020, however plugging that in to one time pad:

https://www.boxentriq.com/code-breaking/one-time-pad

Gives ts{kino} which is incorrect

However typing in ‘Tigera’ gives the correct flag

**ts{king}**



## Don't touch the third rail

![img](https://lh3.googleusercontent.com/tcD0wuGMV3foymTxjd8fwLX5o_SYtGxXVUJqSNGjXXwn3ehA7Jf9WZulJbmlBQVq2aKWwA11SvkXBHaTiVFGmVxDulhYjYRaugP57xh0qNE-IJOkEiOlT46douLKEmRP_cbJME6l)

##### Prompt: tiair}sZgzgCpeFW{yyhT

Interesting cipher known as rail-fence which can be implied from the name

Plug into this site for rail-fence ciphers with the parameter of 3 rails

https://www.boxentriq.com/code-breaking/rail-fence-cipher 

**ts{ZigyzagyCipherFTW}**



## Non-standard NetBIOS Offset

![img](https://lh6.googleusercontent.com/tBVXVRQ0vgQA_tzA6xnSzIyKRfXF2j7R8ooF3wZUDG5pOV5uF-imOkP-sMQLeCnTDOgzqnZ8My3cBIfQ_4fjCVnXjDAEfNocS6YYXoRsUHYAOemOLOL9SHUA0E-rTQqh_e0rdYI1)

##### Prompt : @=@<;F@@?H@;?D@<@=?:@=?B?H?G;F<< Note: Not the standard flag format

**Unsolved**

## All about that base remix

![img](https://lh5.googleusercontent.com/zY9-Q3gBx1BgRvCcHAO6SBTNm_U5img7NOaTuBmq3pHBCzU_i-UrnhG0lyDOQ-KHsrMjY_kDiHxvam-YPj1xpyBUamtZXO6kxAj4XzYMJ6TmLW_v2jdjN1su1xL84EI8SJyzZktL)

##### Prompt: ORZXWVDINFZUS43UN52GC3DMPFCW4Y3SPFYHI2LPNYQX2===

Equals at the end and title implies it it some kind of base encryption

Threw it into cipher identifier on dcode.fr

https://www.dcode.fr/cipher-identifier

Throws out base32, which I plug into dcode.fr

https://www.dcode.fr/base-32-encoding

**ts{ThisIstotallyEncryption!}**



## Two Streams

![img](https://lh3.googleusercontent.com/FEUdoS6nR983h0x-tQanc2sdNWWjg0aT9Fvq_fda8G9X4XMniJsOWPUthKhXMt1Vz8_VNiwENyeP1aRfqbwRrS27GtZY-893CDRjSGiOvrPPlqzbe3_nLF6J3NWmc-stmu5mJlYT)

##### Prompt: tu{OtaOdadqtfNltQcsrsrVhbwYuiLopokb}

**Unsolved**



## All about that base

![img](https://lh3.googleusercontent.com/-pKviOd_TMW8f7XM_AHoVy73ASvT1qgXoF8WN0Q4D6N1p4pp-VsOu_0uo634jLR8Cx3SnFP-JtlKrNGUWqiTwfpUUAKwQ73UDYWdH1Q6bamH7qbDkgVhsZygQUdG2-b1G-axuccf)

##### Prompt: dHN7SXNUaGlzRW5jcnlwdGlvbn0=

One of the easier crypto challenges

Base name and = makes us believe it’s base

https://www.dcode.fr/cipher-identifier

dcode.fr agrees and recognizes its base 64

https://www.dcode.fr/base-64-encoding

**ts{IsThisEncryption}**



## Why are they even in that order in the first place?

![img](https://lh5.googleusercontent.com/2D_FI2S7-t40MaKAoP1_01WRmGuA-3kerEtR_O2XWbfukW42y_9R3jgS2yDULVfYtXz0apPYU69kHuxxCrF42vq78-dItBfIyR48JJh1MpdQhaD01sNrcIZdnHjU9UwAInxZOYe9)

##### Prompt: 20:19:12:15:14:7:5:19:20:3:15:13:2:15:5:22:5:18:18:5:3:15:18:4:5:4 Note: Not the standard flag format

Really didn’t have an idea on this one
https://www.dcode.fr/cipher-identifier
Something called ‘Letter Number Code (A1Z26)’ came up as most recommended
https://www.dcode.fr/letter-number-cipher
Basically it looks like it converts the numbers to ascii
**TS{LONGESTCOMBOEVERRECORDED}**



## AFSC 29331

![img](https://lh3.googleusercontent.com/wFd5vevdM5dzDbk6oivgjgow6l_kSDUjMTZTr8uIHFEPtRemmMTAysr6ujNGu5QL9RKwE57A6wyMfUKbnW8mfPcdYwouvwLfXMApjCOCo2B2eJgPWIH8AOMH7sb6UwacVDGCHe_a)

##### Prompt: (-.. .. - - -.--/-... --- .--. .--. . .-. ...) Note: Not the standard flag format

My guess is morse
https://www.dcode.fr/cipher-identifier
Dcode.fr agrees
https://www.dcode.fr/morse-code
**DITTY BOPPERS**    



## et tu brute

![img](https://lh4.googleusercontent.com/jGeI_S7pm8whjb1JnN_qvQR0K71OiBLJzpoFfTInjpXVTM3CGIJANzKSksCkbe3FhEdkCiUIpMRoTLj0_j-InxJDN7bZXxUKTPuVa5awfggvE9CGtr_951hHZduS8gCL7sV0E-7P)

##### Prompt: gf{NaByqvrOhgNTbbqvr}

Pretty clearly caesar’s cipher from the name ("And you Brutus?")
https://www.dcode.fr/cipher-identifier
Dcode.fr agrees
https://www.dcode.fr/caesar-cipher
**ts{AnOldieButAGoodie}**



## N Eggs

![img](https://lh3.googleusercontent.com/yZ7mzakWpTL_xlULjk6XE6z_uJW8L6SwZzchEZqGhdJeagFfbVDaFOeG2ccLXd6NwOTIP_VSn8eua5ZmWiNWxABhHsQ91PQX1CM_6d-lOT-gBJU0AnAhguz-fgysyZJsq_4Jla1w)

**Prompt: BAABA BAAAB AAAAB AAAAA AAABA ABBAB ABBAA ABAAA BAAAB ABABB BABBA ABBAA AAAAA ABABB AABAA**

https://www.dcode.fr/cipher-identifier
Dcode.fr points us to something called bacon cipher
https://www.dcode.fr/bacon-cipher
Interest cipher different variations of 5 letters convert to ascii
**TS{BACONISMYNAME}**




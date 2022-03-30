# Bacon Recipe

AUTHOR NOTE: If any of these are incorrect or you have solutions to ones I couldn't solve send me a message

## 0x01 Brown Sugar

![img](https://lh3.googleusercontent.com/FPmKI5V1K_AZQ5W8F5uxsm32QQUfBql6z2te4Pz6F3KYAVY9AoYSUQmuP9sFO2Etzj3F7llsvfeQPP4yc7O4qzmIOC4ZcOTR2I0-YuaJH4TK3tunXWWVmnt93jZc4dDfcpZ2H8gI)

**Prompt: The accounts received a suspicious email with attachments today, and after opening the attachment it was all gibberish to them. After noticing some unusual behavior, scared of being infected, the operator shut down the system. Here's the network log of the system in question: bacon_recipe.pcapng There is a free gift from the organizers, find it!**

*What we're being asked: Find a free gift (flag) from the organizers*

Gotta love wireshark
Install wireshark
https://www.wireshark.org/docs/wsug_html_chunked/ChBuildInstallWinInstall.html
Open the file with it
Now hit control f
Make sure dropdown setting says String
Search for flag won’t reveal anything
Hmm
Maybe we should look for emails because the questions mentions a suspicious email
Search ‘email’
Right click that email found and click follow then TCP Stream
If you search (at the bottom) for the keyword flag you get the flag
**flag{g1f7_fr0m_th3_0rg4niz3r5}**

![img](https://lh5.googleusercontent.com/KyllNEPEceuLgThGVYm64Zs9jol10m8Z5QapEFb3DwYBD4U0bidpk1bnyicQgwany9rhax-iE9I6YA1dPQqgqWElbRm0nEqN7yqnrqWPV3wuiIw_e8BTg_CYUvtN53BLeLf9w97-)

## 0x02 Morton Tender Quick

![img](https://lh3.googleusercontent.com/FxumNMpOOJMUXYI-QsFraQO8QBgmJwIb8MySJ2LHFDJQ0dVfCkOWLSkWMd7XWft74wx1ihym4y37BySRlGe0H1zE8EmrB0-nnqABSiuyiFh7DfKVdILfk3FMrZBjRelkZdvqS_kD)

##### Prompt: Can you give a quick count on how many @bacon.threatsims.com emails are mentioned in the network log?

*What we're being asked: Count how many emails from a @bacon.threatsims.com are in network log*

Following the same tcp stream that we did last challenge
Simple control f of @bacon.threatsims.com
Count the number of times an email address in that format receives an email
Meaning how many times it is in the TO: position 
It will be 14 because there is a TO and a TO Address field for every email
**flag{7}**

![image-20220330155456722](/home/t/snap/typora/58/.config/Typora/typora-user-images/image-20220330155456722.png)



## 0x03 Bacon Shipment

![img](https://lh4.googleusercontent.com/Xoeh3KJibO6IfhEPtIk4xl-dV0Ttxus7sSouZh9gDnskrv4QXZlZBDjeqjNhXpFVsypKPBDvahv7EyL7-IYeSExhRWPvjAJ9odaBbt9aAR4V71drxsqVwY15y2ItwxHzeQ2vjMbJ)

##### Prompt: Who sent the email with attachment? Flag format: flag{email}

*What we're being asked: What is the email address that sent an attachment to an email*

Still following the same TCP stream search for attachment
Scroll through till you find one which has attachment set to something besides null
Backtrack from there until you find the From section which has the email address who sent the email with the attachment
**flag{payments@shipify.org}**

![img](https://lh4.googleusercontent.com/nvo24yDEVkfJ6cNfCC0IE78Y7U5lqbuBi5Y8mTPtyY-nq4ejy_pkcQIJmjbWzwSZzJxBFlSqhIWihIqx2KemfDb2DaBTBLTeetMpYSch0o2IsUQEW97UzBUwGK8AVCzEx3pRrd1P)



## 0x04 Bacon Delivered

![img](https://lh5.googleusercontent.com/OZGlTPfP4fwqz0Z8bODvWD7pirSl1rM0IQ4-HXZMsbxmWUeWZGWrC-I0hHu0FLk9wS_0B3xgwE7q2GIZIfkERLVUk1oiUh1oC0TPPXtDcs2gM3rLFN07eUYLEhHwDyXDwHFcPjIY)



##### Prompt: Can you analyze the attachment in question and find the next flag?

*What we're being asked: Download and look at the attachment*

Finally we are done with that TCP stream
Back on the main Wireshark screen 
We are looking for the attachment to analyze, luckily Wireshark allows us to do that easily
Top left File dropdown, Export Objects, HTTP
Click and save the ms-excel file
<u>**WARNING: this is windows malware so don’t download on a windows machine**</u>
Instead please use a virtual box with some kind of linux
Open that saved file in your excel viewer of choice (I prefer libreoffice)
Flag is in plaintext
**flag{r3turn_0f_th3_m4cr0s_xlm_4.0}**

![img](https://lh3.googleusercontent.com/coXLFflYgu70SJZRsLyaU5qtYjn88IUN2HhISkVLPVxJmBo-OjUmNG3EP4Y1R4XEPV6r3zRvAfAc-nBSMxzttvZ5zJDXITPLlgDWR2eIKCQ3P51q0TZNXDtsxQtSPdhFvoUt1Rls)



## 0x05 Bacon Unpacked

![img](https://lh6.googleusercontent.com/RW4hrG_-iOQeeULqkb1Zg0hVEvmMO9qjbv6rcDQ0w6H7hpk29OSEnQ-sI5tlMLSgG_kxRnQ-nASIVMtvkuhZN-OP67yvvtAvV6DPHViYn9kJwn0NxGJvLZZjCegDTBsMvZ3mjtR2)

##### Looks like the attackers deployed a Cobalt Strike c2 on the victim machine. What is the full URL that delivered the initial payload? Flag format: flag{http://ATTACKER/PATH}

*What we're being asked: Find the url that delivered payload*

So this one took me some time to find
As I was looking through the packets manually I saw a rather bright red one
This, I learned with a quick google search, indicated a TCP RST or TCP Reset
This usually happens when an unexpected packet is received
That’s probably the malware
Looking a few lines lower we see a HTTP GET request to /gitgud
Inspecting HTTP of that packet we get what definitely looks like some encrypted malware
The host listed is 172.16.95.133
The path is /gitgud
**flag{http://172.16.95.133/gitgud}**

![img](https://lh5.googleusercontent.com/u1uRtapWXIrNzrKpg1FcDckdYXIiWczrofNGYGX79ewZAiM5aUpabLUYVvUTiLVKUwywLbjUnP238wI-HiGFoPaJISVXt3WM6CH1Pg9m6cF05Z8gUkYRXk6C_XdqiAS87narPtrt)

## 0x06 Bacon Marinated

![img](https://lh6.googleusercontent.com/kE2MmVNR87TVgfGqKbQfnszxTKF9FsZ6nGMB0QnGUODrUFLnOOtjYwc9_41MvIQ5-oltv6mPUTNCyGQ4Tuq2JrvrBuHVoaaPz0ilpSUXfO9DkD_es-ds8cnKcRfA7YmzozgZ5UzO)

##### Prompt: Can you decrypt the c2 metadata and extract the raw key? Flag format: flag{key}

*What we're being asked: Decrypt the metadata of the malware and extract the key*

Note: I did not solve this or subsequent challenges during the competition 

This youtube video walks through this and the remainder of the Bacon Recipe challenges

https://www.youtube.com/watch?v=a4RiYu4_aOo

Full credit to creator

I personally couldn't get the tool to work correctly (probably a problem on my computer's end) so I'm going to end this writeup here
# Chinchilla Challenge: Cuzco’s Great Adventure

AUTHOR NOTE: If any of these are incorrect or you have solutions to ones I couldn't solve send me a message

## 0x01 Cuzco's Great Adventure Flag

![img](https://lh4.googleusercontent.com/DZjanWGCt0R7moVnuis_1MtpjeC1GxJ7mOwTteP28TDI5QuNDzgfYkjrF88PoJtximp4kkMLBQZ3U3I5BVY8X_3c-wEu2GXERBGeHka9Cz8JUjJ-5prVAvn804HDSdNXATNkj-Gk)

##### Prompt: Cuzco, the chinchilla, had always wanted to go on a grand adventure. She was boxed in, surrounded on all four sides by walls, but she was getting faster. If she could 10x (a term for upskilling a lot) her skills, continue her practice jumps and codebreaking, then maybe she could break through her walls, and get to that Parkour class she wanted to take. Just out of her reach was a folded paper, which she thought might contain more Parkour info. One day she spotted a ciphered clue fluttering near a lock and she thought it might help her break through her gate. Crack the following message to help Cuzco with flag 2. For flag 1, what method is used to obfuscate the message? Gb oernx guebhtu guvf jnyy lbh zhfg svaq guvf ybpx.

*What we're being asked: Decode ‘Gb oernx guebhtu guvf jnyy lbh zhfg svaq guvf ybpx’*

Chug it in dcode.fr
https://www.dcode.fr/cipher-identifier
Gives us ROT-13 (or Caesar cipher)
https://www.dcode.fr/rot-13-cipher
**To break through this wall you must find this lock**



## 0x02 Cuzco's Great Adventure Flag

![img](https://lh4.googleusercontent.com/dTiHzXPLXq4muTfdWkpzrqYpOlxcb1BmRMA1liNc7JgiXwxTo6_vcfYNtRA1vvrOlOdaMIrMzqyQe8xKk-bUVwq_DAaYCQaC3Ibtf_HyhW0AFfcbeqyA1w0wbGZe6WmaL3e43NSr)

##### Prompt: Using OSINT, help Cuzco find the name of the bridge (actual bridge name in French).

*What we're being asked: find this bridge's name*

We can use the flag from last challenge as a hint
To break through this wall you must find this lock
This is a famous bridge in France (which can be implied because of the French name) where lovers lock locks and throw keys into the river below to signify love
A simple google search of ‘french lock bridge’ reveals the answer
**Pont des Arts**



## 0x03 Cuzco's Great Adventure Flag

![img](https://lh6.googleusercontent.com/qV5PfshBKDyJy8Jh0UMfE3QbrtlKkgww3tOXMXITqWhWbl7iFt01U7wo_MQ67-NVlzI9tP7HFgi2c2ipHLGg4xtHB2hdZO7LS7V66QLBaLpFhNNPPaPrNSSWooybyNg1_xQ8WAeo)

##### Prompt: Cuzco deciphered the code, broke open the lock, and was about to break through the barriers when she found another clue.
U2VjdXJpdHkgdGhyb3VnaCBvYnNjdXJpdHkgY2FuIGFsc28gbWVhbiB0aGF0IGl0IGlzIGp1c3QgaGlkZGVuIGluIHRoZSBsYXllcnM= What is this encoded in?

*What we're being asked: Identify cipher type of U2VjdXJpdHkgdGhyb3VnaCBvYnNjdXJpdHkgY2FuIGFsc28gbWVhbiB0aGF0IGl0IGlzIGp1c3QgaGlkZGVuIGluIHRoZSBsYXllcnM=*

This is probably a base64, which I can imply from the equals sign at the end
https://www.dcode.fr/cipher-identifier
Dcode.fr agrees with me: 
**base64**

Decoded version if anyone is interested:
Security through obscurity can also mean that it is just hidden in the layers



## 0x04 Cuzco's Great Adventure Flag

![img](https://lh3.googleusercontent.com/DxONaQ3Cj5JdjQWqB50xBWW5QlAF2T19z3Ud1I0fHQ4YR5B0F5HW9wDUeOgYMoA1Cvm8gCkoEG8N3oSD4AlGKOdPRHDJ312NLaKM2Y4XRr_aaJKYNCNN2qk3Qx975hyk4O1fKYlV)

##### Prompt: Flag 4 Use the image file to find the question:

![img](https://lh4.googleusercontent.com/cZhgPhmB9vSo0c7eCC8Ntb45gT6SDEbOzggAlarFqbffA8A1bBERdtqXnQuh_To4kanPakhI4f8RRQ_zSu21Sk60DTgDEJdAQPN0D0lG7r2ZLnaGXIgBdg6YYPRozzsy2D2xkf95)

*What we're being asked: find a question in somewhere in this file*

Now a smart person would probably plug this into some specialized tool to grab metadata
But I prefer to do things a little less precise
I opened the file in my directory and catted it
Cat img.png
The last bit of text printed was
**FLAG 4 Question: Use OSINT, Who invented Parkour?**



## 0x05 Cuzco's Great Adventure Flag

![img](https://lh6.googleusercontent.com/x_J6Q76hgLMfUG80XReSqhE8InCStQ3uE-BsOIElJbSkpvP-lZ8HMWcAeGBnH3Wu-0yo0-Ui8xAcItvj0HBzqlnplH6AXXBDZ_2deQ1R3kqobjAzY9r6pjDwoU962aUi9wQnCu64)

##### Prompt: Flag 5 Use the image file to find the question: Download here

*What we're being asked: Answer the question we just found in the previous challenge*

Use OSINT, Who invented Parkour?
Pretty easy google question
**David Belle**



## 0x06 Cuzco's Great Adventure Flag

![img](https://lh6.googleusercontent.com/BYULrx8_t7g1mV_XZbXt1W4M8GF6voU9jFfzYW-MnDcbT4c5Z-_S_ZYSAbrirrhLTeOaRm-tf23rBiYSjC3Lt25rrDVs3oDfTErUlQVUkKEW_OTT2Ix3n5AU4yR9WKshWHf0Icc8)

![img](https://lh4.googleusercontent.com/23y_LqWVOdoDK8KibITuGLkUSxNUl1FQy9iAkfyCD2nZteZqKcEIxl8RlxoQ4uBmxLazpjbYg9vMTkFKbRiEi3OYbATm5vl4lrgUieXBLkKwEu0FUBS1LY6_2s-fSWw5ZX6j19aJ)

##### Prompt: Cuzco continued to learn more about Parkour; she was stronger, and she was ready to break through the barrier. How will she do it? What will launch her from her perch in the comfy hammock? Sometimes it can be hard to make the decision to leave our comfort zone and risk the unknown - is it really worth it? But know this, there is a community here for you. Cuzco decided that she would brave it, even though there were risks, and that she would fail sometimes. Her risk profile adjusted for this and she wandered into the world to find her Parkour class and work on 10x her skills. She knew she’d need community, balance, and fortitude to help her, so she continued her quest to find these 3 things. She grabbed the piece of paper as soon as she left her walls. She decided that for safekeeping, since she’s going on a quest, to digitize it so that then she can download it later. On the quest… First, she worked on developing her community. She’d been alone in her walls, but no chinchilla can do everything alone – she could not accomplish this quest as if she were an island. When she left she had to find others and decided to work with the squirrels. She worked on getting to know her new friends by studying them on YouTube. She wanted to make meaningful connections and help their community too. Instead of clicking connect with the first squirrel she met, she tried to get to know something about each one and find ways to discuss their commonalities. That way she could write about this when she clicked connect if she was on TreeIn or Chitter. If she was in person she tried to connect with other squirrels based on shared interests. Who made 2 YouTube videos about squirrel obstacle courses that Cuzco used to learn more about the squirrel community (1.0 and 2.0)?

*What we're being asked: Find the name of the channel which has the videos described*

There were a number of different approaches you could take to get this flag
I knew there was a 1.0 and 2.0 video
As a result there was probably a video with 2.0 in the name
I knew it was a video about squirrel obstacle courses
So squirrel obstacle course was probably in name 
So I went on youtube and looked up ‘squirrel obstacle course 2.0’
First result from guy names ‘Mark Rober’ with 21.3 million subscribers
**Mark Rober** 



## 0x07 Cuzco's Great Adventure Flag

![img](https://lh6.googleusercontent.com/_29IUZVHUE-lx0vZzkhabWVsq3Gl794DBZkirZMZKoDabQf239FwNveoX1x4qfFwuE1s6dIVBh5epRIHx20eoDL59G5XeBZswwOiGNAvlP1ZuPI0KStpGCAX3aso-rGUB6ZuoO_m)

##### Prompt: She was starting to build a community. Next, she wanted to work on balance; both in the physical sense, as it is important for parkour and also in the sense of making sure that she wasn’t doing too many things. She’d heard of PancakesCon and that it was a place where people celebrated knowledge of information security and having passions outside of cybersecurity. To learn more about this she listened to some talks from past years. What was Shecky’s talk title from PancakesCon 2 in 2021 with the theme “We Persevere”?

*What we're being asked: Find the title of the PancakesCon 2 talk that Shecky (internet pseudonym) gave*

This one drove me nuts (pun not intended)
The only way to do this one while getting the correct results is to use youtube
Websites with the name of the talk are all incorrectly formatted
I know Shecky gave the speech 
His pseudonym is probably in title
And I know the name of the conference is PancakesCon 2
PancakesCon 2 is probably in title
Youtube searched ‘Shecky PancakesCon2’
First result has name of speech in title
**Avoiding Burnout, and Exciting Train Facts**



## 0x08 Cuzco's Great Adventure Flag

![img](https://lh4.googleusercontent.com/SRyVve1wNEqoLy0oFS1VJrGqwfbDMtgPXc4-JdnxmNPVy6jz-IJZvWZXyQq6_Z8bk5dOoO5sF42Oe_ubn7-HJRXeLhfmSsHRJL8dfnT3WmoIFqUleibT_pbf1QpY9eh--5kALCV-)

##### Prompt:  Cuzco was building her community, talking to others, getting known, making real connections with squirrel buddies, working on balance, and paying attention to her passion for other interests - for her, it was running, but she had one more thing to do: She needed to work on fortitude as she continued her quest to find her Parkour class. Many things in life are not easy and having strength can be helpful. There will be failure along the way. Comparing one’s journey to another person’s can be demoralizing and it is through having a good sense of community and goals that we can make progress. Cuzco knew these things. She practiced reflecting on the progress she’d made since she started her journey…she started with barriers and now there were fewer, she started with walls, and now she had a community, so she grew in her fortitude. Now that Cuzco had strength from her community and some balance she could test her fortitude. She began work on the digitized file, which was the first thing she gathered on her trip. Her new friends let her know that she should do some searching. So she opened Command Line (Terminal/Command Prompt/PowerShell) and decided to check the MD5sum of the file Parkour Flyer Information. She’d heard files could be tampered with and she wanted to make sure that hers was safe. What is the MD5 checksum hash of the downloaded file https://drive.google.com/file/d/1UBCB4ZBYPrZ8iB5vH1Ns6VvjS8j2KXC0/view?usp=  ?

*What we're being asked: Get the MD5 hash of the pdf file*

I did this on a linux terminal, as the way md5 command for powershell gives incorrect capitalization
md5sum command
md5sum file.pdf
**9691c69c33f444222facf8fad310aca4**



## 0x09 Cuzco's Great Adventure Flag

![img](https://lh5.googleusercontent.com/Jg7c1fXM8XCK66AzRfgRG57iL6WSdFRZJMhzTl2F1zNe0KrFqTQkjrROBAmwiKOtw8QV02jnGjp6peuH_hjxAK9x2sPsFBQnZDWZVr4uNayiYfWpgf1zDzK_qtglvJRp88XbdR32)

##### Prompt: Cuzco was aware that the file had information about Parkour that would help her learn even more, so she decided it was safe, downloaded it, and tried to open it. That’s when she learned the file had been encrypted. Can you help her crack the password? She had one additional piece of information, this MD5 Hash: 51F8571B1EC5D507670802B3A5F06B65

*What we're being asked: Crack the MD5 hash 51F8571B1EC5D507670802B3A5F06B65*

MD5 hash cracking is intensive work, so most online crackers just look up the hash against a known table
51F8571B1EC5D507670802B3A5F06B65
https://www.cellphonetrackers.org/tool/md5-coder.php
**Parkour**



## 0x0A Cuzco's Great Adventure Flag

![img](https://lh4.googleusercontent.com/aRy4nM7Y353bUQJp9Lyw0jJ0UqBIiLuNkqg5ttmIG7tnhB2jXAmkWTcpNbGi1B7su66JHbNy1cO16HQ-XsnLxeF2rmKoa1Z5UCBaAaNaFv7glsXJaH3Qbhf_p1O57eWPVtEf6qY-)

![img](https://lh3.googleusercontent.com/ttHyglnpbq35B-SIo_WcokAlyLhdXnqQZ4-DIxf8tJMQDz2kdlJMm4GO47HN5_dbqS26JJNO9ia6zv5Y-EpSMPi4fArRbM4icWyMAFQnjD9OgFTUfftmLWNNZ_RTmts-V5abCVkY)

##### Prompt: Now that you’ve helped her open and view the file, Cuzco knows two things. One, the file creator should work on password complexity. Two, before visiting the website on the flyer, she should investigate it using some threat hunter sites. Investigate the site with the following tools: Use https://www.whois.com/ or the whois command on the command line URLscanner https://urlscan.io/ make sure it is a private scan Pulsedive at https://pulsedive.com/ and complete a passive scan of the site Based on your research, what year was this site first registered? Also, what level of risk would Cuzco be taking on if she were to visit the site? Flag format: YEAR___*** The format will be YEAR_Case_Sensitive_Answer It should be the 4 digit year_ and then 3 words Cuzco had traveled far, met new friends, worked on balance, gained new knowledge, and gained 10 flags - effectively working on 10x her skills. She knew that eventually, she’d need to go back 127.0.0.1 (an IP address for localhost usually meaning you are home), and she had gained so much on her quest. She decided to review a few resources to make her trip home a learning experience and have some balance too: https://www.sans.org/blog/dont-miss-these-top-rated-sans-summit-replays/ https://www.sans.org/blog/visual-summary-of-sans-new-to-cyber-summit/ https://wakelet.com/wake/ZoDim7iESNHwLFr4DJeOC And because balance: https://youtu.be/VZrDxD0Za9I?list=PLu4wnki9NI_8VmJ7Qz_byhKwCquXcy6u9 https://youtu.be/f0RQ5C7g_tA?list=PLnzLfzo-SovQvT8zbcBdkeNkwZ38f2SAM She safely made it back to her 127.0.0.1, and once she arrived, she found that her home was more open than she remembered. There was more community surrounding it than she thought. She just had to look out the window and remember she’d had her adventure, there was help to be found, and she was part of this community - she belonged! Remember you belong here and are part of our community too.

*What we're being asked: Find the year parkour.com was first registered and its risk level*

I had a hard time getting the format of this one correct
We need to find the information on Parkour.com using the websites provided
https://urlscan.io/result/fc77d0a4-9cd1-4be1-b464-e133c85328dc/
From this site we get the year to be 2002
https://pulsedive.com/indicator/?iid=33327345
From this site we get the information that the site is ‘Very low risk’
**2002_Verylowrisk**
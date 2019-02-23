# Writeup 2 - OSINT

Name: *Lawrence Byun*
Section: *0101*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: *Lawrence Byun*

## Assignment Writeup

### Part 1 (45 pts)

1. What is v0idcache's real name?


Elizabeth Moffet  - Found @v0idcache on twitter with the IntelTechniques.com tools



2. Where does v0idcache work? What is the URL to their website?

1337 Bank   		http://1337bank.money/		- From her twitter page.



3. List all personal information (including social media accounts, contacts, etc) you can find about v0idcache. For each, briefly detail how you discovered them.  

Searched IntelTechniques.com for username “v0idcache” and got all the following results.
Twitter: @v0idcache
Gmail v0idcache@gmail.com
HotMail: v0idcache@gmail.com 
AOL: v0idcahce@aol.com 
Yahoo: v0idcache@aol.com 
Reddit: u/v0idcache

I ran the “whois 1337bank.money” command in terminal and got the following contact information.

Address - Leeteinde 12 , Broek, Waterland, 1151 AK, NL.
Name- Serina Ness 
Organisation: Donuts Inc. 
Address: Donuts Inc. 5808 Lake Washington Blvd NE, Suite 300 Kirkland, WA 98033 United States 
Phone: +1.425.283.8248 
Fax-no: +1.425.671.0020 
E-mail: serina@donuts.email


       
4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.

Searched the “1337bank.money” in DNSDumpster.com

142.93.136.81		-New York, NY
				- 216.87.155.33 (DNS Servers)
				- 216.87.152.33 (DNS Servers)
				- 162.255.118.61 (MX Records)
				- 162.255.118.62 (MX Records)
				





5. List any hidden files or directories you found on this website. For full credit, list two distinct flags. 

CMSC389R-{h1ding_fil3s_in_r0bots_L0L}	- Found by putting "/robots.txt" at the end of the url for the website

CMSC389R-{h1dd3n_1n_plain_5ight} 		- Inspected the HTML on the website "1337money.bank"




6. What ports are open on the website? What services are running behind these ports? How did you discover this?

22/tcp    ssh
80/tcp    http
1337	waste

I used the command “nmap 142.93.136.81 -p1-2000” in terminal


7. Which operating system is running on the server that is hosting the website? How did you discover this?

Ubuntu.           - Searched the IP address “142.93.136.81” in censys.io/



8. BONUS: Did you find any other flags on your OSINT mission? (Up to 9 pts!)

CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}. Found on reddit, posted by user u/v0idcache.

CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}	- In server

CMSC389R-{2bmPrIPj1k13iMrKYS5e4vkZI}	- In server
	
CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5} 	- Found on DNSDumpster.com when I looked up the IP address "142.93.136.81"



### Part 2 (75 pts)

*Please use this space to detail your approach and solutions for part 2. Don't forget to upload yourcompleted source code to this /writeup directory as well!

I don't have too much experience with Python so it took me a bit to get familiar with it; never messed with sockets either so I used the sockets library doc that was provided to us. 
Once I got the connection and understood how to communicate with the server, I tried every password in the rockyou.txt file until I got access. After I had access, I searched for the AB4300.txt file that v0idcache and f1inch were talking about; found a message between the two in pastebin. While I was searching for AB4300.txt I saw a flag.txt file.
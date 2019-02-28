# Writeup 3 - Operational Security and Social Engineering

Name: Lawrence Byun
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Lawrence Byun

## Assignment Writeup

### Part 1 (40 pts)
How to social engineer this information out of Elizabeth Moffet

- What's her mother's maiden name?
	I would first try to figure out which services she uses (cellphone, internet, electric, Spotify, waste services,  ect) that has a security question asking for her mother's maiden name. Either by calling those services pretending to be her or OSINT.
	I would call her pretending to be that service, saying some suspicious activity on the account. I would then ask her to confirm some basic information; Address of service, First and Last name, Contact Number, ect.
	Then I would repeat the secuirty question and then ask her for the answer.


- What browser does she primarily use?
	Pretend like your doing a project for school, that is in her companies district. Make an innocent looking survey and ask if you can ask the employee's and herself these questions. (What TV brand do you currently use, What brand of shoes are you wearing, ect) Make sure that the internet browser question is one of them. Just need to make sure which survey is her's. 
	Try to appeal to her saying that although you could ask your school, you wanted the opinions from a more "professional", local audience.

- What city was she born in?
	Pretend to be a student jounalist from a local University/School and ask if you could ask her some questions; her specifically because she is the CEO of a bank. Ask her things like where she grew up and how she get to where she is now.  	


- What's her ATM pin number?
	If she has a child old enough to play video games. Pretend like you're her bank and that she has a strange amount of charges for "Fortnite". If she does not know what it is, explain to her that it is a free online game but that you can buy stuff on it; either online or buying in-game currency at convenience stores. Tell her that some popular YouTuber recently made a video with a new item from that game and that this has been happening a lot this week. Ask her to reconfirm some basic information and then ask her for the old pin and the new pin she wishes to change it to.


- What was the name of her first pet?
	Try to figure out if she or her family member has a pet. Pretend to be the local animal shelter and call her. Say it with charisma!
	
	Dialouge: 
	Me:"Hello?"
	Her: "Hello?"
	Me: "Hi, I'm Frank from the Rockvile Animal Shelter! As a fun statistic here at the shelter, we wanted to ask the members of the community the name of their first pet. Feel no obligation to answer!"



### Part 2 (60 pts)
I was able to find the port number with nmap. I would recommend putting a firewall on the port so that it's status is filtered. 
"Nmap cannot determine whether the port is open because packet filtering prevents its probes from reaching the port. The filtering could be from a dedicated firewall device, router rules, or host-based firewall software. These ports frustrate attackers because they provide so little information."  https://nmap.org/book/man-port-scanning-basics.html 

A simple WHOIS 1337bank.money gave me person information about the domain owner. ICANN, the international governing body for domain names, requires that every domain registrar maintain a publicly viewable "WHOIS" database that displays personal contact information for every domain registered. 
To hide such personal information, make the domain private. Although you no longer are the owner of the domain, you have more security from the general public.		https://luxsci.com/blog/dangers-of-private-domain-registrations-and-whois-masking.html 


Lastly, I would recommend that she search for and block robots that make too many requests in a short period of time. Search engines use them to index the site so blocking all robots would not be encourged.

https://nmap.org/robots.txt
http://www.robotstxt.org/robotstxt.html










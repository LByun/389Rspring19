# Writeup 7 - Binaries I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*

## Assignment Writeup

### Part 1 (90 Pts)

*Put your code here as well as in main.c*
#include <stdio.h>

int main(){
	
	int a = 0x1ceb00da;
	int b = 0xfeedface;

	printf("a = %d", a);
	printf("b = %d", b);

	a ^= b;
	b ^= a;
	a ^= b;

	printf("a = %d", a);
	printf("b = %d", b);

	return 0;

}

### Part 2 (10 Pts)

Assigns the value 0x1ceb00da to variable a and the value 0xfeedface into another variable b. It switches the values of the variables with the C bitwise excluse OR and assignment operator ^=.

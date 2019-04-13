/*
 * Name: *PUT YOUR NAME HERE*
 * Section: *PUT YOUR SECTION NUMBER HERE*
 *
 * I pledge on my honor that I have not given or received any unauthorized
 * assistance on this assignment or examination.
 *
 * Digital acknowledgement: *Lawrence Byun*
 */

/* your code goes here */

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
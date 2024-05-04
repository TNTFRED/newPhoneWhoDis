#include <stdio.h>

int main() {

	char userInput[100];
	printf("Can you pass the UPs dog?: ");
	fgets(userInput, sizeof(userInput), stdin);
	printf("What's up dog? SMH\n");
	printf("Not %s", userInput);

	return 0;
}

#include <stdio.h>

int main() {
	int userInput;
	printf("What's THE best number? ");
	scanf("%d", &userInput);

	if (userInput == 13) {
		printf("MONEY!");
	} else {
		printf("meh");
	}
	return 0;

}

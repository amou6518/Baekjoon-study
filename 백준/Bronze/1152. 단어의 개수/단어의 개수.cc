#include <stdio.h>
#include <string.h>

char str [1000001];

int main(){
    
	int word = 1;
	scanf("%[^\n]", str);

	if (strlen(str) == 1 && str[0] == ' ') {
		printf("0");
		return 0;
	}

	for (int i = 1; i < strlen(str) - 1; i++) {
		if (str[i] == ' ') word++;
	}

	printf("%d", word);

	return 0;
}

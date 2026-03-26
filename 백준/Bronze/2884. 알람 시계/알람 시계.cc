#include<stdio.h>
int main() {
	int a, b;
	scanf("%d %d\n", &a,&b);
	if (b >= 45)
		printf("%d %d\n",a,b-45);
	else if (a>0)
		printf("%d %d\n", a-1, 60-(45-b));
	else
		printf("23 %d\n", 60 - (45 - b));
	return 0;
}
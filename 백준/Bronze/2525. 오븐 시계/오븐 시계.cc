#include<stdio.h>
int main() {
	int a, b, n;
	scanf("%d %d\n", &a, &b);
	scanf("%d", &n);
	if (b + n < 60) 
		printf("%d %d\n", a, b + n);
	else { 
		int hour = (b + n) / 60;
		int min = (b + n) % 60;
		if (a + hour < 24)
			printf("%d %d\n", a + hour, min);
		else 
			printf("%d %d\n", a+hour-24, min);
	}
	return 0;
}
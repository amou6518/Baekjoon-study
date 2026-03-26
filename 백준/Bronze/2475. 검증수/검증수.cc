#include <stdio.h>

int main(){
	int x;
	int y = 0;
	
	for(int i=0;i<5;i++){
		scanf("%d",&x);
		y += x*x;
	}
	
	y %= 10;
	
	printf("%d",y);
	
	return 0;
}
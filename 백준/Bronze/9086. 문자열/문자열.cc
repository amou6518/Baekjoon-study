#include<stdio.h>
#include<string.h>

int main(){

int n;
char str[1001];

scanf("%d",&n);

while(n--){
scanf("%s",str);
printf("%c%c \n",str[0],str[strlen(str)-1]);
}
return 0;
}
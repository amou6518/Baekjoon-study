#include <stdio.h>
int main(void){
    int A, B;
    scanf("%d %d", &A, &B);
    int a3 = A * (B % 10);
    int a4 = A * ((B / 10) % 10);
    int a5 = A * (B / 100);
    int a6 = a3 + (a4*10) + (a5*100);
    printf("%d\n", a3);
    printf("%d\n", a4);
    printf("%d\n", a5);
    printf("%d\n", a6);
    return 0;
}
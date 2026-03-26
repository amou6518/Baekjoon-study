#include <stdio.h>
#include <stdlib.h>

int main() {
    int k;
    if (scanf("%d", &k) != 1) return 0;

    int *stack = (int *)malloc(sizeof(int) * k);
    int top = -1; 

    for (int i = 0; i < k; i++) {
        int num;
        scanf("%d", &num);

        if (num == 0) {
            if (top >= 0) {
                top--;
            }
        } else {
            stack[++top] = num;
        }
    }

    long long sum = 0;
    for (int i = 0; i <= top; i++) {
        sum += stack[i];
    }

    printf("%lld\n", sum);

    free(stack);
    return 0;
}
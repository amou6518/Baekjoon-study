#include <stdio.h>

typedef struct {
    int height;
    int index;
} Tower;

Tower stack[500001];
int top = -1;

int main() {
    int n;
    if (scanf("%d", &n) != 1) return 0;

    for (int i = 1; i <= n; i++) {
        int h;
        scanf("%d", &h);

        while (top != -1 && stack[top].height < h) {
            top--;
        }

        if (top == -1) {
            printf("0 ");
        } else {
            printf("%d ", stack[top].index);
        }

        stack[++top].height = h;
        stack[top].index = i;
    }

    return 0;
}
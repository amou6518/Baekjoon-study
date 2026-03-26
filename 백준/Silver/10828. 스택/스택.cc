#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 10000

typedef struct {
    int data[MAX_SIZE];
    int top;
} Stack;

void init(Stack *s) {
    s->top = -1;
}

int empty(Stack *s) {
    if (s->top == -1) {
        return 1;
    } else {
        return 0;
    }
}

int size(Stack *s) {
    return s->top + 1;
}

void push(Stack *s, int x) {
    if (s->top == MAX_SIZE - 1) {
        printf("Stack overflow");
        return;
    }
    s->data[++(s->top)] = x;
}

int pop(Stack *s) {
    if (empty(s)) {
        return -1;
    }
    return s->data[(s->top)--];
}

int top(Stack *s) {
    if (empty(s)) {
        return -1;
    }
    return s->data[s->top];
}

int main() {
    Stack s;
    init(&s);

    int N;
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        char command[10];
        scanf("%s", command);

        if (strcmp(command, "push") == 0) {
            int x;
            scanf("%d", &x);
            push(&s, x);
        } else if (strcmp(command, "pop") == 0) {
            printf("%d\n", pop(&s));
        } else if (strcmp(command, "size") == 0) {
            printf("%d\n", size(&s));
        } else if (strcmp(command, "empty") == 0) {
            printf("%d\n", empty(&s));
        } else if (strcmp(command, "top") == 0) {
            printf("%d\n", top(&s));
        }
    }

    return 0;
}
 
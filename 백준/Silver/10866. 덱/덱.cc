#include <stdio.h>
#include <string.h>

int deque[20005];
int front = 10000;
int rear = 10000;

int main() {
    int n;
    scanf("%d", &n);

    while (n--) {
        char cmd[15];
        scanf("%s", cmd);

        if (strcmp(cmd, "push_front") == 0) {
            int x;
            scanf("%d", &x);
            deque[front--] = x;
        } 
        else if (strcmp(cmd, "push_back") == 0) {
            int x;
            scanf("%d", &x);
            deque[++rear] = x;
        } 
        else if (strcmp(cmd, "pop_front") == 0) {
            if (front == rear) printf("-1\n");
            else printf("%d\n", deque[++front]);
        } 
        else if (strcmp(cmd, "pop_back") == 0) {
            if (front == rear) printf("-1\n");
            else printf("%d\n", deque[rear--]);
        } 
        else if (strcmp(cmd, "size") == 0) {
            printf("%d\n", rear - front);
        } 
        else if (strcmp(cmd, "empty") == 0) {
            printf("%d\n", (front == rear) ? 1 : 0);
        } 
        else if (strcmp(cmd, "front") == 0) {
            if (front == rear) printf("-1\n");
            else printf("%d\n", deque[front + 1]);
        } 
        else if (strcmp(cmd, "back") == 0) {
            if (front == rear) printf("-1\n");
            else printf("%d\n", deque[rear]);
        }
    }

    return 0;
}
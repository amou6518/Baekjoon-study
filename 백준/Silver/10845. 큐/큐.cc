#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct QUEUE {
    int ary[10000];
    int head;
    int tail;
} Queue;

void push(int n, Queue *queue);
int pop(Queue *queue);
int size(Queue queue);
int isEmpty(Queue queue);
int getFront(Queue queue);
int getBack(Queue queue);

void push(int n, Queue *queue) {
    queue->ary[(queue->tail)++] = n; 
}

int pop(Queue *queue) {
    if (isEmpty(*queue)) return -1;
    else return queue->ary[(queue->head)++];
}

int size(Queue queue) {
    int size = queue.tail - queue.head;
    if (size <= 0) return 0;
    else return size;
}

int isEmpty(Queue queue) {
    if (queue.head >= queue.tail) return 1;
    else return 0;
}

int getFront(Queue queue) {
    if (isEmpty(queue)) return -1;
    else return (queue.ary[queue.head]);
}

int getBack(Queue queue) {
    if (isEmpty(queue)) return -1;
    else return (queue.ary[queue.tail - 1]);
}

int main() {
    int N;
    scanf("%d", &N);
    
    Queue queue;
    queue.head = 0;
    queue.tail = 0;
    
    char command[20];
    int n;
    for (int i = 0; i < N; i++) {
        scanf("%s", command);
        switch (command[0]) {
            case 's':
                printf("%d\n", size(queue));
                break;
            case 'e':
                printf("%d\n", isEmpty(queue));
                break;
            case 'f':
                printf("%d\n", getFront(queue));
                break;
            case 'b':
                printf("%d\n", getBack(queue));
                break;
            default:
                if (command[1] == 'u') {
                    scanf("%d", &n);
                    push(n, &queue);
                } else printf("%d\n", pop(&queue));
        }
    }
}
#include <stdio.h>

int main() {
    int n, m;
    int deque[51];
    int targets[51];
    int total_moves = 0;
    
    if (scanf("%d %d", &n, &m) != 2) return 0;
    for (int i = 0; i < m; i++) {
        scanf("%d", &targets[i]);
    }

    int size = n;
    for (int i = 0; i < size; i++) {
        deque[i] = i + 1;
    }

    for (int i = 0; i < m; i++) {
        int target = targets[i];
        int target_idx = 0;

        for (int j = 0; j < size; j++) {
            if (deque[j] == target) {
                target_idx = j;
                break;
            }
        }

        int left_dist = target_idx;
        int right_dist = size - target_idx;

        if (left_dist <= right_dist) {
            for (int j = 0; j < left_dist; j++) {
                int temp = deque[0];
                for (int k = 0; k < size - 1; k++) {
                    deque[k] = deque[k + 1];
                }
                deque[size - 1] = temp;
                total_moves++;
            }
        } else {
            for (int j = 0; j < right_dist; j++) {
                int temp = deque[size - 1];
                for (int k = size - 1; k > 0; k--) {
                    deque[k] = deque[k - 1];
                }
                deque[0] = temp;
                total_moves++;
            }
        }

        for (int j = 0; j < size - 1; j++) {
            deque[j] = deque[j + 1];
        }
        size--; 
    }

    printf("%d\n", total_moves);

    return 0;
}
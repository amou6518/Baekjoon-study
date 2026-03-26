#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int num1 = *(int *)a;
    int num2 = *(int *)b;

    if (num1 < num2) return -1;
    if (num1 > num2) return 1;
    return 0;
}

int binary_search(int arr[], int size, int target) {
    int low = 0;
    int high = size - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2; 
        if (arr[mid] == target) {
            return 1; 
        } else if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return 0; 
}

int main() {
    int n, m;

    if (scanf("%d", &n) != 1) return 0;
    int *x = (int *)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &x[i]);
    }

    qsort(x, n, sizeof(int), compare);

    if (scanf("%d", &m) != 1) return 0;
    for (int i = 0; i < m; i++) {
        int target;
        scanf("%d", &target);
        
        printf("%d ", binary_search(x, n, target));
    }

    free(x); 
    return 0;
}
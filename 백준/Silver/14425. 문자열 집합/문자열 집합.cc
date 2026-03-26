#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int compare(const void *a, const void *b) {
    return strcmp((char *)a, (char *)b);
}

int main() {
    int n, m;
    int count = 0;

    if (scanf("%d %d", &n, &m) != 2) return 0;

    char (*s)[501] = (char (*)[501])malloc(sizeof(char) * n * 501);
    for (int i = 0; i < n; i++) {
        scanf("%s", s[i]);
    }

    qsort(s, n, 501, compare);

    char target[501];
    for (int i = 0; i < m; i++) {
        scanf("%s", target);

        if (bsearch(target, s, n, 501, compare) != NULL) {
            count++;
        }
    }

    printf("%d\n", count);

    free(s);
    return 0;
}
#include <stdio.h>

int sum(int n) {
    if (n == 0) {
        return 0;
    }

    return sum(n-1) + n;
}

int main() {

    int value = 0;

    value = sum(10);

    printf("Value: %d", value);

    return 0;
}
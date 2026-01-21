#include <stdio.h>

void funB(int n);

void funA(int n) {
    if (n > 0) {
        printf("Value A: %d\n", n);
        funB(n -1);
    }
}

void funB(int n) {
    if (n > 1) {
        printf("Value B: %d\n", n);
        funA(n/2);
    }
}

int main() {
    funA(20);
    return 0;
}
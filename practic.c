#include <stdio.h>

int fun1(int num) {
    static int x = 0;

    if(num > 0) {
        x++;
        return fun1(num - 1) + x;
    }
}

int main() {
    printf("%d", fun1(3));
    return 0;
}
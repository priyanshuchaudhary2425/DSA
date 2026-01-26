#include <stdio.h>

int f[10];

int fib(int n) {
    static int num=0;
    num++;

    
    printf("Value count: %d\n", num);

    if(f[n] != -1)
    return f[n];

    
    if(n<=1) {
        f[n] = n;
        return n;
    }

    else
    {
        if (f[n-2] == -1) {
            f[n-2] = fib(n-2);
        }

        if (f[n-1] == -1) {
            f[n-1] = fib(n-1);
        }

        f[n] = f[n-2] + f[n-1];
        printf("Array value: %d\n", f[n]);
    }

    return f[n];
}

int main() {

    for(int i=0; i<10; i++){
        f[i] = -1;
    }
    printf("Value: %d\n", fib(6));
    printf("Value: %d\n", fib(6));
    return 0;
}
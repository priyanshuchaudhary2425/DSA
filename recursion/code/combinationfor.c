#include <stdio.h>

int c(int n, int r) {
    if(r==0 || n==r) {
        return 1;
    } else {
        return c(n-1,r-1) + c(n-1,r);
    }
}

int fac(int n) {
    if (n==0) return 1;
    
    return fac(n-1)*n;
}

int ncr(int n, int r) {
    int num, den;

    num = fac(n);
    den = fac(r)*fac(n-r);

    return num/den;
}

int main() {
    printf("Value: %d", ncr(4,2));
    return 0;
}
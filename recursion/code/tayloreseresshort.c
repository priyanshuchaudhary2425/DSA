#include <stdio.h>

double e(int x, int n) {
    static double s=1;
    if (n == 0) {
        return s;
    }
    s = 1 + ((double) x/n) *s;
    return e(x, n-1);
}

double e1(int x, int n) {
    double s=1;
    for(n; n>0;n--) {
        s = 1+ ((double)x/n)*s;
    }
    return s;
}

double e2(int x, int n) {
    if(n == 0)
        return 1;
    return e2(x, n-1) + (x / (double)n);
}



int main() {
    printf("Value: %f", e2(4, 5));
    return 0;
}
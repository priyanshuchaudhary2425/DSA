#include <stdio.h>

// int fac(int n) {
//     if (n == 0) {
//         return 1;
//     }

//     return fac(n - 1) * n;
// }

// int main() {
//     printf("Value: %d", fac(3));
//     return 0;
// }

/// USING LOOP

int fac(int n) {
    int s=1;
    for(int i=1; i<=n; i++) {
        s=s*i;
    }
    return s;
}

int main() {
    printf("Value: %d", fac(3));
    return 0;
}
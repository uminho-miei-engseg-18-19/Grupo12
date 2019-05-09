#include <stdio.h>
#include <stdlib.h>

void vulneravel (char *matriz, size_t x, size_t y, char valor) {
        int i, j;
        matriz = (char *) malloc(x*y);
        for (i = 0; i < x; i++) {
                printf("%d\n",i);
                for (j = 0; j < y; j++) {
                        matriz[i*y+j] = valor;
                }
        }
}

int main() {
        unsigned long x = 2147483651;
        unsigned long y = 1;
        char *matriz;
        char valor = 'c';
        vulneravel(matriz,x,y,valor);

        return 0;
}

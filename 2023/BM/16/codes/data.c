#include <math.h>
#include <stdio.h>
#include <stdlib.h>

void calculate(FILE *file, int R, double C, double start_n, double end_n) {
    double omega;
    for (omega = start_n; omega <= end_n; omega += 0.1) {
        double result = 1 / sqrt(1 + pow(omega * R * C, 2));
        fprintf(file, "%lf %lf\n", omega, result);
    }
}

int main() {
    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    calculate(file, 1000, 0.0001, -50.0, 50.0);

    fclose(file);

    return 0;
}


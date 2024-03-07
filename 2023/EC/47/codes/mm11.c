#include <stdio.h>
#include <math.h>
#include <complex.h>

#define N 5

// Given X(k) values
double complex X[] = {5, 15 * I, 10 * I, -10 * I, -15 * I, 0, 0, 0};

// Function to calculate phase of X[k]
double calculate_phase_X_k(int k) {
    return carg(X[k]);
}

int main() {
    double phase_X_k[N];

    // Calculate phase of X[k] for each k
    for (int k = 0; k < N; k++) {
        phase_X_k[k] = calculate_phase_X_k(k);
    }

    // Open file for writing
    FILE *fp = fopen("mm11.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Write phase of X[k] values to file
    for (int i = 0; i < N; i++) {
        fprintf(fp, "%f\n", phase_X_k[i]);
    }

    // Close file
    fclose(fp);

    return 0;
}


#include <stdio.h>
#include <math.h>
#include <complex.h>

#define N 5

// Given X(k) values
double complex X[] = {5, 15 * I, 10 * I, -10 * I, -15 * I};

// Function to calculate amplitude of X[k]
double calculate_amplitude_X_k(int k) {
    return cabs(X[k]);
}

int main() {
    double k;
    double amplitude_X_k;

    // Open file for writing
    FILE *fp = fopen("mm1.dat", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate amplitude of X[k] for each k and write to file
    for (k = 0; k < N; k++) {
        amplitude_X_k = calculate_amplitude_X_k(k);
        fprintf(fp, "%f %f\n", k, amplitude_X_k);
    }

    // Close file
    fclose(fp);

    return 0;
}


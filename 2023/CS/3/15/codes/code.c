#include <stdio.h>
#include <math.h>

double calculate_L(int n) {
    double sqrt5 = sqrt(5);
    double phi = (1 + sqrt5) / 2;
    double psi = (1 - sqrt5) / 2;
    double Ln = pow(phi, n) + pow(psi, n);
    return Ln;
}

int main() {
    FILE *fp;
    fp = fopen("output.txt", "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Calculate and write values to file
    for (int n = 1; n <= 10; n++) {
        double result = calculate_L(n);
        fprintf(fp, "%.10f\n", result);  // Write with high precision
    }

    fclose(fp);
    printf("Output values have been written to output.txt\n");
    return 0;
}


#include "ee1205.h"
#include <stdio.h>
#include <math.h>

// Function that calculates v_c(t) = 7(1 - e^(-t/0.121))
double v_c(double t) {
    return 7. * (1. - exp(-t / .121));
}

int main () {
    // Generate x-axis.
    double* t = linspace(0, 1, 201);

    // Open file.
    FILE* out;
    fopen_s(&out, "gate23bm30cout.txt", "w");

    for (size_t i = 0; i < 201; i++) {
        // Write v_c(t) to output file.
        fprintf(out, "%lf ", v_c(t[i]));
    }

    // Close file.
    fclose(out);
    // Free memory allocated for t.
    free(t);

    return 0;
}
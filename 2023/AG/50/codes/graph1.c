#include <stdio.h>
#include <math.h>

int main() {
    FILE *file;
    file = fopen("output_expression.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Define the range of x values
    double start_x = 0.0;
    double end_x = 1.0;
    double step = 0.1;

    // Calculate and write the values to the file
    for (double x = start_x; x <= end_x; x += step) {
        double result = 3 * exp(x) - 2 * (x + 1);
        fprintf(file, "x=%.2f\tResult=%.4f\n", x, result);
    }

    // Close the file
    fclose(file);

    printf("Results saved in output_expression.txt\n");

    return 0;
}

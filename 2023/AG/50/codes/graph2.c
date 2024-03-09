#include <stdio.h>
#include <math.h>

double calculate_y(double x, double y_prev, double h) {
    double term1 = 2 * x + y_prev * (6 + 3 * h + h * h + h * h * h / 4);
    double term2 = 6 * h + 2 * h * h + h * h * h / 2;
    return y_prev + h / 6.0 * (term1 + term2);
}

int main() {
    FILE *file;
    file = fopen("output.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    // Define the range of x values and step size
    double start_x = 0.0;
    double end_x = 1.0;
    double step = 0.1;

    // Initial condition y(0) = 1
    double y_prev = 1.0;

    // Calculate and write the values to the file
    for (double x = start_x; x <= end_x; x += step) {
        double y = calculate_y(x, y_prev, step);
        fprintf(file, "x=%.2f\ty=%.4f\n", x, y);
        y_prev = y;
    }

    // Close the file
    fclose(file);

    printf("Results saved in output.txt\n");

    return 0;
}

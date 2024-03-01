#include <stdio.h>
#include <math.h>

int main() {
    // Define the data from the Python code
    double k = 1;
    double T1 = 2;
    double T2 = 3;
    
    // Compute the phase crossover frequency
    double phase_crossover_freq = 1 / sqrt(T1 * T2);
    
    // Define the transfer function numerator and denominator coefficients
    double numerator[3] = {k*T1*T2, k*(T1+T2), k};
    double denominator[4] = {0, T1*T2, T1+T2, 0};
    
    // Store the data into a file
    FILE *file = fopen("frequency_response_data.txt", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    
    // Write data to the file
    fprintf(file, "Transfer Function Numerator Coefficients:\n");
    for (int i = 0; i < 3; i++) {
        fprintf(file, "%.6f\n", numerator[i]);
    }
    fprintf(file, "\n");
    
    fprintf(file, "Transfer Function Denominator Coefficients:\n");
    for (int i = 0; i < 4; i++) {
        fprintf(file, "%.6f\n", denominator[i]);
    }
    fprintf(file, "\n");
    
    fprintf(file, "Phase Crossover Frequency: %.6f rad/s\n", phase_crossover_freq);
    
    // Close the file
    fclose(file);
    
    printf("Data written to file successfully!\n");
    
    return 0;
}


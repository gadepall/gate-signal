#include <stdio.h>
#include <math.h>

#define NUM_POINTS 10000    // Increase number of points for a larger range
#define PI 3.14159265358979323846

// Constants
#define V_RMS (10 * sqrt(2)) // RMS voltage (V)
#define Z_MAG 75             // Magnitude of impedance (ohms)
#define OMEGA (40001 * PI)   // Angular frequency (rad/s)

int main() {
    double t[NUM_POINTS];
    double instantaneous_current[NUM_POINTS];

    // Time values covering a larger range
    double step = 5.0 / NUM_POINTS; // Adjusted for a larger range
    for (int i = 0; i < NUM_POINTS; ++i) {
        t[i] = step * i;

        // Calculate current values (sine wave)
        instantaneous_current[i] = V_RMS * sin(OMEGA * t[i]);
    }

    // Save values in gate.dat file
    FILE *file = fopen("gate.dat", "w");
    if (file != NULL) {
        for (int i = 0; i < NUM_POINTS; ++i) {
            fprintf(file, "%.6f %.6f\n", t[i], instantaneous_current[i]);
        }
        fclose(file);
        printf("Data saved successfully to gate.dat\n");
    } else {
        printf("Error opening file\n");
        return 1;
    }

    return 0;
}


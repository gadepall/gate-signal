#include <stdio.h>
#include <math.h>
#include <complex.h>
#include <fftw3.h>

#define N 8

int main() {
    // Given coefficients
    double complex a[N] = {1, 3 * I, 2 * I, -2 * I, -3 * I};

    // Generate the signal x[n] using the DFS representation
    double complex x[N];
    for (int n = 0; n < N; n++) {
        x[n] = 0;
        for (int k = 0; k < N; k++) {
            x[n] += a[k] * cexp(2 * I * M_PI * n * k / N);
        }
    }

    // Compute the FFT of the signal x[n]
    fftw_complex *X = fftw_alloc_complex(N);
    fftw_plan plan_x = fftw_plan_dft_1d(N, (fftw_complex *)x, X, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(plan_x);

    // Generate the sin(4πn/5) signal with the correct sign
    double complex sin_signal[N];
    for (int n = 0; n < N; n++) {
        sin_signal[n] = sin(4 * M_PI * n / N) * (n == 0 ? 0 : -1); // Add the correct sign
    }

    // Compute the FFT of the sin(4πn/8) signal
    fftw_complex *Sin = fftw_alloc_complex(N);
    fftw_plan plan_sin = fftw_plan_dft_1d(N, (fftw_complex *)sin_signal, Sin, FFTW_FORWARD, FFTW_ESTIMATE);
    fftw_execute(plan_sin);

    // Multiply the FFTs of x[n] and sin(4πn/5)
    fftw_complex *product = fftw_alloc_complex(N);
    for (int i = 0; i < N; i++) {
        product[i] = X[i] * Sin[i];
    }

    // Compute the IFFT of the product
    fftw_complex *result = fftw_alloc_complex(N);
    fftw_plan plan_ifft = fftw_plan_dft_1d(N, product, result, FFTW_BACKWARD, FFTW_ESTIMATE);
    fftw_execute(plan_ifft);

    // Extract the real part of the result and divide by N
    double sum_real = creal(result[0]) / N;
    double sum_imag = cimag(result[0]) / N;

    // Combine real and imaginary parts to get the final sum
    double sum = sum_real + sum_imag;

    // Open the file for writing
    FILE *file = fopen("c.dat", "w");
    if (file == NULL) {
        fprintf(stderr, "Error opening file.\n");
        return 1;
    }

    // Write the sum to the file
    fprintf(file, "%.2f\n", sum);

    // Close the file
    fclose(file);

    // Clean up
    fftw_destroy_plan(plan_x);
    fftw_destroy_plan(plan_sin);
    fftw_destroy_plan(plan_ifft);
    fftw_free(X);
    fftw_free(Sin);
    fftw_free(product);
    fftw_free(result);

    return 0;
}


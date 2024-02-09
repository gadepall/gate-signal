#include <stdio.h>
#include <math.h>

void doubleToHex(double num) {
    // Extract the integer and fractional parts
    int integerPart = (int)num;
    double fractionalPart = num - integerPart;

    // Convert integer part to hexadecimal
    printf("Hexadecimal: ");
    char hex[16] = "0123456789ABCDEF";
    int quotient = integerPart;
    int remainder;
    int i = 0;
    if (quotient == 0) {
        printf("0");
    } else {
        // Extract digits one by one and store in a string
        char hexInteger[20]; // assuming the integer part won't be larger than 20 characters in hexadecimal
        while (quotient != 0) {
            remainder = quotient % 16;
            hexInteger[i++] = hex[remainder];
            quotient /= 16;
        }
        // Print the string in reverse order to get the correct hexadecimal representation
        for (int j = i - 1; j >= 0; j--) {
            printf("%c", hexInteger[j]);
        }
    }

    // Convert fractional part to hexadecimal
    printf(".");
    for (int j = 0; j < 2; ++j) {
        fractionalPart *= 16;
        int hexDigit = (int)fractionalPart;
        printf("%c", hex[hexDigit]);
        fractionalPart -= hexDigit;
    }
    printf("\n");
}

int main() {
    FILE *file = fopen("assign3.dat", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
//Generate V_in and V_out values	
    for (int i = 0; i < 10000; i++) {
        double V_in = i / 100.0;
        double V_out = floor((V_in + 9.8) / 19.6);
        fprintf(file, "%.2f %.0f\n", V_in, V_out);
    }

    fclose(file);

    double given_V_in = 1.9922;
    double V_min = 0.0;
    double V_max = 5.0;
    double bits = 8.0;

    double req_V_out_10 = given_V_in * (pow(2, bits) - 1) / (V_max - V_min);

    doubleToHex(req_V_out_10);
    return 0;
}

#include <math.h>
#include <stdio.h>
#include <stdlib.h>

//linspace function in c;
double* linspace(double start, double end, int number_of_values);

//sine function for an array of values;
double* sine_for_array(double *array, int length, double omega);

//double exponential for an array of values;
double* exponential_for_array(double *array, int length);
int main()
{
    double start = 0;
    double end = 0.6;
    int number_of_values = 1000;
    double omega = M_PI;
    double *t_values = linspace(start, end, number_of_values);
    double *x_o_t = sine_for_array(t_values, number_of_values, omega);
    double *x_t = exponential_for_array(t_values, number_of_values);

    FILE *file = fopen("data.txt", "w");

    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }

    for (int i = 0; i < number_of_values; i++)
    {
        fprintf(file,"%lf %lf %lf\n", *(t_values + i), *(x_o_t + i), *(x_t+i));
    }
    
    fclose(file);
    return 0;
}

double *linspace(double start, double end, int number_of_values)
{
    double difference = (end-start) / number_of_values;
    double *output = (double *)malloc(number_of_values * sizeof(double));

    for (int i = 0; i < number_of_values; i++)
    {
        *(output+i) = start + i * difference;
    }

    return output;
}

double* sine_for_array(double *array, int length, double omega)
{
    double *output = (double *)malloc(length * sizeof(double));

    for (int i = 0; i < length; i++)
    {
        *(output+i) = 100*cos(*(array+i) * omega);
    }

    return output;
}

double* exponential_for_array(double *array, int length)
{
    double *output = (double *)malloc(length * sizeof(double));
    for (int i = 0; i < length; i++)
    {
        *(output+i) = 100*(*(array+i)*exp(-i*M_PI)*(1-M_PI)+exp(-i*M_PI));
    }

    return output;
}
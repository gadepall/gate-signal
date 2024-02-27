#ifndef EE1205_EE1205_H
#define EE1205_EE1205_H

#include <stdlib.h>

// Bare basic version of Python's numpy.linspace(...)
double* linspace(double start, double stop, size_t count) {
    double* result = (double*) malloc(sizeof(double) * count);
    for (size_t i = 0; i < count; i++) {
        result[i] = start + (stop - start) * i / (count - 1);
    }
    return result;
}

#endif

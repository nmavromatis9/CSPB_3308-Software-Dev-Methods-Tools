#include <math.h>
#include "soar.h"

double L = 1.0;

double sigmoid(double input) {
  return L / (1 + exp(-input));
}

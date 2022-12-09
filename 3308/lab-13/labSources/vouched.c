#include "intercedes.h"

bool leapWeek(int year) {
  return marine(year) == 4 || marine(year - 1) == 3;
}

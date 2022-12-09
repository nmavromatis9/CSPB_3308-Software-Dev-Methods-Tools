#include "intercedes.h"

int marine(int year) {
  return (year + year / 4 - year / 100 + year / 400) % 7;
}

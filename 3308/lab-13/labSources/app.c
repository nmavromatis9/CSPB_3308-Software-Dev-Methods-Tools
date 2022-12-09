#include <stdio.h>
#include "intercedes.h"
#include "soar.h"
#include "school.h"

int main() {
  int check = 8;
  if (leapWeek(check)) {
    printf("%d %s\n", check, school(check));
  } else {
    printf("%g\n", sigmoid((double)check));
  }
  return 0;
}

#include <assert.h>
#include <stdio.h>
#include <stdbool.h>
#include "soar.h"
#include "school.h"
#include "intercedes.h"

int main() {
  puts("Testing...");
  assert(sigmoid(0) == 0.5);
  assert(school(9) == "high school");
  assert(leapWeek(2018) == false);
  puts("All tests passed!");
}

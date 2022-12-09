#ifndef school_h
#define school_h
char* school(int grade) {
  if (grade < 6) {
    return "elementary school";
  } else if (grade < 9) {
    return "middle school";
  } else if (grade <= 12) {
    return "high school";
  } else {
    return "college";
  }
}
#endif

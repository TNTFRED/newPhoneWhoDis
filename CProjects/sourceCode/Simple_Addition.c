  #include <stdio.h>

int addition(int x, int y);

  int firstNumber = 1;
  int secondNumber = 2;

int main() {
  printf("%d\n", addition(firstNumber, secondNumber));
  return 0;
}

int addition(int x, int y) {
  int sum = x + y;
  return sum;
}

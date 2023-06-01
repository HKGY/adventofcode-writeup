#include<bits/stdc++.h>

int main()
{
 char line[10];
 int max = 0, sum = 0;
 for (; fgets(line, 10, stdin);) {
  if (line[0] != '\n') {
   sum += atoi(line);
  } else {
   if (sum > max)
    max = sum;
   sum = 0;
  }
 }

 printf("%d\n", max);
 return 0;
}
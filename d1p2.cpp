#include <stdio.h>
using namespace std;
int main()
{   
    int a[2000],m,n,i,x=0;
    for(int i=0;i<2000;i++){
        scanf("%d\n",&a[i]);
    }
    m=a[0]+a[1]+a[2];
    for(int i=0;i<2000;i++){
        n=m-a[i]+a[i+3];
        if (n>m){x++;}
        m=n;
    }
    printf("%d",x);
    return 0;
}
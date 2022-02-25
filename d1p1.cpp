#include <stdio.h>
using namespace std;
int main()
{   
    int m,n,i,x=0;
    scanf("%d\n",&m);
    for(int i=0;i<1998;i++){
        scanf("%d\n",&n);
        if (n>m){x++;}
        m=n;
    }
    printf("%d",x);
    return 0;
}
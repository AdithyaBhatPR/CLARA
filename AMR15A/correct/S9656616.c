
    #include<stdio.h>
    int main(){
    int n,a[100],i,r=0,c=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
     {  scanf("%d",&a[i]);
        if(a[i]%2==0)
           r++;
        else
            c++;
      }         
    if(r>c)
     printf("READY FOR BATTLE");
    else
     printf("NOT READY");
    return 0;
    }



    #include <stdio.h>
    
    int main() {
            int e=0, o=0, s, i;
            scanf("%d", &i);
            while(i--)
            {
                    scanf("%d", &s);
                    if (s%2) o++;
                    else e++;
            }
    
            if (e>o) printf("READY FOR BATTLE\n");
            else printf("NOT READY\n");
            return 0;
    }
    


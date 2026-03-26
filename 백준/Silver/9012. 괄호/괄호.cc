#include<stdio.h>
#include<string.h>

int main(){
    char v[51]={0};
    int t;
    scanf("%d",&t);

    while(t--){
        scanf("%s",&v);
        int count =0;
        for(int j = 0; j < strlen(v);j++){   
            if(v[j]=='('){
                count++;
           }
            else if(v[j]==')'){
                count--;}
            if(count < 0){
                break;
            }
        }
        if(count != 0)
            printf("NO\n");
        else
            printf("YES\n");
    }
    return 0;
}

//Author: Carlo Malagnino

//Task: edits

#pragma GCC optimize("Ofast")
#include<bits/stdc++.h>

using namespace std;

int main(){
    int T;
    string ln;
    scanf("%d", &T);

    for(int t=1;t<=T;t++){
        cin >> ln;
        int p=0, c=0;
        string cmd;
        int n=ln.length();
        while(p<n){
            if (ln[p]=='['){
                if(ln[p+1]=='C'){
                    if(c>0){
                        cmd=cmd.substr(0,c-1)+cmd.substr(c);
                        c-=1;
                    }
                    p+=3;
                    continue;
                }
                if(ln[p+1]=='L'){
                    c=max(0,c-1);
                    p+=3;
                    continue;
                }
                c=min(int(cmd.length()),c+1);
                p+=3;
                continue;
            }
            cmd=cmd.substr(0,c)+ln[p]+cmd.substr(c);
            p+=1;
            c+=1;
        }
        cout << "Case #"<< t << ": " << cmd << "\n";
    }
}

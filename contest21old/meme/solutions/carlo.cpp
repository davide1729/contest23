//Author: Carlo Malagnino

//Task: meme

#include<bits/stdc++.h>

using namespace std;

int main(){
    int T;

    scanf("%d", &T);

    for(int t=1;t<=T;t++){
        int N, m;
        scanf("%d%d", &N, &m);
        int w[N+1], p[N+1];
        for(int i=1;i<=N;i++){
            scanf("%d%d", &w[i], &p[i]);
        }
        pair<int,int> M[N+1][m+1];
        for(int i=0;i<=m;i++){
            M[0][i]={0,-1};
        }
        for(int i=1;i<=N;i++){
            for(int j=0;j<=m;j++){
                if(w[i]>j){
                    M[i][j]=M[i-1][j];
                }
                else{
                    if(p[i]+M[i-1][j-w[i]].first>M[i-1][j].first){
                        M[i][j]={p[i]+M[i-1][j-w[i]].first, i};
                    }
                    else{
                        M[i][j]=M[i-1][j];
                    }
                }
            }
        }
        int g=N, h=m, meme;
        stack<int> ris;
        while(M[g][h].second!=-1){
            meme=M[g][h].second;
            ris.push(meme);
            h-=w[meme];
            g=meme-1;
        }
        printf("Case #%d:", t);
        while(!ris.empty()){
            printf(" %d", ris.top());
            ris.pop();
        }
        printf("\n");
    }
}

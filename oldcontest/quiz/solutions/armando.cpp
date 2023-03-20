//Author: Armando Pellegrini

//Task: quiz

#include <bits/stdc++.h>
using namespace std;
#define MAXN 1001
int n,m,T;
vector<int>adj[MAXN];
vector<int>colore(MAXN,-1);
bool mat[MAXN][MAXN];
bool dfs(int u,int c){
    colore[u]=c;
    for(int v:adj[u]){
        if(colore[u]==colore[v])return false;
        else if(colore[v]==-1&&!dfs(v,1-c))return false;
    }
    return true;
}
void init(int n){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++)mat[i][j]=0;
    }
    for(int i=0;i<n;i++)adj[i].clear(),colore[i]=-1;
}
int main(){

    //ifstream cin("input.txt");
    //ofstream cout("output.txt");
    cin>>T;
    for(int ca=1;ca<=T;ca++){
        cin>>n>>m;
        init(n);
        for(int i=0;i<m;i++){
            int a,b;
            cin>>a>>b;
            mat[a][b]=mat[b][a]=1;
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(i!=j&&!mat[i][j]){
                    adj[i].push_back(j);
                }
            }
        }
        bool ok=true;
        for(int i=0;i<n;i++){
            if(colore[i]==-1){
                ok&=dfs(i,0);
            }
        }
        if(!ok){
            cout<<"Case #"<<ca<<": "<<-1<<"\n";
        } else {
            int n1=0,n2=0;
            cout<<"Case #"<<ca<<": ";
            for(int i=0;i<n;i++){
                if(colore[i]==0)n1++;
                else n2++;
            }
            cout<<n1<<" ";
            for(int i=0;i<n;i++){
                if(colore[i]==0)cout<<i<<" ";
            }
            cout<<n2<<" ";
            for(int i=0;i<n;i++){
                if(colore[i]==1)cout<<i<<" ";
            }
            cout<<"\n";
        }
    }

}

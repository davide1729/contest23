#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MAXN 1004
int dp[MAXN][MAXN];
int P[MAXN],Q[MAXN];
int mossa[MAXN][MAXN];
int main(){
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        int n,m;
        cin>>n>>m;
        for(int i=1;i<=n;i++){
            cin>>P[i]>>Q[i];
        }
        for(int i=0;i<=m;i++){
            for(int j=1;j<=n;j++){
                dp[i][j]=dp[i][j-1];
                mossa[i][j]=0;
                if(i-P[j]>=0&&dp[i-P[j]][j-1]+Q[j]>dp[i][j]){
                    dp[i][j]=dp[i-P[j]][j-1]+Q[j];
                    mossa[i][j]=1;
                }
            }
        }
        int a=m,b=n;
        vector<int>ris;
        while (b!=0) {
            if(mossa[a][b]){
                ris.push_back(b);
                a-=P[b];
                b--;
            }else{
                b--;
            }
        }
        sort(ris.begin(),ris.end());
        cout<<"Case #"<<ca<<": ";
        for(int x:ris)cout<<x<<" ";
        cout<<"\n";


    }
}

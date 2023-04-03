#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define MAXN 1002
int n,D;
int X[MAXN],Y[MAXN],H[MAXN];
vector<int>topo_sort;
double Dist[MAXN];
vector<bool>vis(MAXN);
int dist(int i,int j){
    return (X[i]-X[j])*(X[i]-X[j])+(Y[i]-Y[j])*(Y[i]-Y[j]);
}
void dfs(int nodo){
    vis[nodo]=1;
    for(int i=0;i<n;i++){
        if(!vis[i]&&H[i]<H[nodo]&&dist(nodo,i)<=D*D){
            dfs(i);
        }
    }
    topo_sort.push_back(nodo);
}
int main(){
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        cin>>n>>D;
        topo_sort.clear();
        for(int i=0;i<n;i++){
            vis[i]=0;
            cin>>X[i]>>Y[i]>>H[i];
        }
        for(int i=0;i<n;i++){
            if(!vis[i])dfs(i);
        }
        reverse(topo_sort.begin(),topo_sort.end());
        for(int i=n-1;i>=0;i--){
            Dist[topo_sort[i]]=0;
            for(int j=i+1;j<n;j++){
                if(H[topo_sort[j]]<H[topo_sort[i]]&&dist(topo_sort[i],topo_sort[j])<=D*D){
                    Dist[topo_sort[i]]=max(Dist[topo_sort[i]],sqrt(dist(topo_sort[i],topo_sort[j])*1.0)+Dist[topo_sort[j]]);
                }
            }
        }
        for(int i=0;i<n;i++){
            Dist[0]=max(Dist[0],Dist[i]);
        }
        cout<<"Case #"<<ca<<": "<<(int)(Dist[0]+0.5)<<"\n";
    }
}

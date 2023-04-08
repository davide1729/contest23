#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll solve(int l,int r,vector<pair<ll,bool> >&ar){
    ll c=1e18;
    for(int i=l;i<r;i++){
        c=min(c,ar[i].first-ar[l].first+ar[r].first-ar[i+1].first);
    }
    return c;
}

int main(){
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        int n;
        cin>>n;
        string s;
        cin>>s;
        vector<pair<ll,bool> >ar(n);
        vector<int>supp;
        for(int i=0;i<n;i++){
            cin>>ar[i].first;
            ar[i].second=(s[i]=='0'?0:1);
        }
        sort(ar.begin(),ar.end());
        for(int i=0;i<n;i++){
            if(ar[i].second)supp.push_back(i);
        }
        ll ris=ar[supp[0]].first-ar[0].first+ar[n-1].first-ar[supp[supp.size()-1]].first;

        for(int i=0;i<(int)supp.size()-1;i++){
            if(supp[i]+1==supp[i+1])continue;
            ris+=solve(supp[i],supp[i+1],ar);
        }

        cout<<"Case #"<<ca<<": "<<ris<<endl;
    }
}

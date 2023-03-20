/*
 * Contest Luiss di allenamento per le Selezioni Territoriali delle Olimpiadi di Informatica
 * Data: 15-05-2021
 * Task: Prolunghe
 */

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main(){
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        int n;
        string s;
        cin>>n>>s;
        vector<pair<int,bool> >ar(n);
        for(int i=0;i<n;i++){
            cin>>ar[i].first;
            ar[i].second=(s[i]=='0'?0:1);
        }
        sort(ar.begin(),ar.end());

        vector<int>prefix(n);
        if(ar[0].second)prefix[0]=ar[0].first;
        else prefix[0]=-1e9;
        for(int i=1;i<n;i++){
            if(ar[i].second)prefix[i]=ar[i].first;
            else prefix[i]=prefix[i-1];
        }

        vector<int>suffix(n);
        if(ar[n-1].second)suffix[n-1]=ar[n-1].first;
        else suffix[n-1]=1e9;
        for(int i=n-2;i>=0;i--){
            if(ar[i].second)suffix[i]=ar[i].first;
            else suffix[i]=suffix[i+1];
        }

        int ris=0;
        for(int i=0;i<n;i++){
            ris+=min(suffix[i]-ar[i].first,ar[i].first-prefix[i]);
        }
        cout<<"Case #"<<ca<<": "<<ris<<"\n";
    }
}

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
struct nodo{
    nodo* left=NULL;
    nodo* right=NULL;
    char c='#';
};
int main(){
    int t;
    cin>>t;
    for(int ca=1;ca<=t;ca++){
        string s;
        cin>>s;
        int n=s.size();
        int cursore=0;
        int caratteri=0;
        nodo *supp=new nodo();
        for(int i=0;i<n;i++){
            if(s[i]=='['){
                if(s[i+1]=='C'){
                    if(cursore!=0){
                        supp->left->right=supp->right;
                        if(supp->right!=NULL)supp->right->left=supp->left;
                        supp=supp->left;
                        cursore--;
                        caratteri--;
                    }
                }
                else if(s[i+1]=='L'){
                    if(cursore!=0){
                        cursore--;
                        supp=supp->left;
                    }
                }
                else{
                    if(cursore<caratteri){
                        supp=supp->right;
                        cursore++;
                    }
                }
                i+=2;
            }
            else{
                nodo *tmp=new nodo();
                tmp->left=supp;
                tmp->right=supp->right;
                if(supp->right!=NULL)supp->right->left=tmp;
                supp->right=tmp;

                tmp->c=s[i];
                supp=tmp;
                cursore++;
                caratteri++;
            }
        }
        while (supp->left!=NULL) {
            supp=supp->left;
        }
        cout<<"Case #"<<ca<<": ";
        supp=supp->right;
        while (supp->right!=NULL) {
            cout<<supp->c;
            supp=supp->right;
        }
        if(supp->c!='#')cout<<supp->c;
        cout<<"\n";
    }
}

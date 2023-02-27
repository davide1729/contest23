// Soluzione
// Task: "Roma"
// Carlo Malagnino

#include<bits/stdc++.h>
#define MAXN 1010

using namespace std;

int N, M;
int Mappa[MAXN][MAXN];
bool vis[MAXN][MAXN];

void visita(int x, int y) {

    vis[x][y] = true;
    if (x==0 || x==N+1 || y==0 || y==M+1 || Mappa[x][y] == 0)
        return ;

    if (!vis[x-1][y]) visita(x-1,y);
    if (!vis[x+1][y]) visita(x+1,y);
    if (!vis[x][y-1]) visita(x,y-1);
    if (!vis[x][y+1]) visita(x,y+1);
    if (!vis[x-1][y+1]) visita(x-1,y+1);
    if (!vis[x-1][y-1]) visita(x-1,y-1);
    if (!vis[x+1][y+1]) visita(x+1,y+1);
    if (!vis[x+1][y-1]) visita(x+1,y-1);

}

int main() {
    
    int T;
    cin >> T;

    for(int t=1;t<=T;t++){

        cin >> N >> M;

        for(int i=1;i<=N;i++)
            for (int j=1;j<=M;j++)
                cin >> Mappa[i][j];

        for(int i=0;i<=N+1;i++)
            for(int j=0;j<=M+1;j++)
                vis[i][j]=false;


        long long int isole=0;
        for (int i=1;i<=N;i++)
            for (int j=1;j<=M;j++)
                if (!vis[i][j] && Mappa[i][j]==1){
                    visita(i,j);
                    isole+=1;
                }

        cout << "Case #" << t << ": " << isole-1 << "\n";

    }
    return 0;

}

#include <bits/stdc++.h>

using namespace std;
#define ll long long
#define pii pair<int,int>
#define vi vector<int>


int n;
int ans = 0;
int visited[33];
int visited2[33];
int visited3[33];

void rec(int y) {
	if (y==n) {
		ans++;
		return;
	}
	
	for (int i = 0; i < n; i++) {
		if (visited[i]||visited2[i+y]||visited3[i-y+n]) continue;
		visited[i] = 1;
		visited2[i+y] = 1;
		visited3[i-y+n] = 1;
		rec(y+1);
		visited[i] = 0;
		visited2[i+y] = 0;
		visited3[i-y+n] = 0;
	}
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin>>n;
    rec(0);
    cout<<ans;
}

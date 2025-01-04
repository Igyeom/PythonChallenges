// For how to provide input, see sample cases at https://www.acmicpc.net/problem/1991
// This program demonstrates preorder, inorder, postorder in the binary tree.a

#include <bits/stdc++.h>

using namespace std;
#define int long long
#define pii pair<int,int>
#define vi vector<int>


int n, _root[30], _left[30], _right[30];
string pre, in, post;

void preorder(int node) {
	if (node == -1) return;
	pre += 'A'+node;
	preorder(_left[node]);
	preorder(_right[node]);
}

void inorder(int node) {
	if (node == -1) return;
	inorder(_left[node]);
	in += 'A'+node;
	inorder(_right[node]);
}

void postorder(int node) {
	if (node == -1) return;
	postorder(_left[node]);
	postorder(_right[node]);
	post += 'A'+node;
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    
    cin>>n;
    for (int i = 0; i < n; i++) {
    	char r, lt, rt;
    	cin>>r>>lt>>rt;
    	
    	_root[i] = r-'A';
    	
    	if (lt == '.') _left[_root[i]] = -1;
    	else _left[_root[i]] = lt-'A';
    	
    	if (rt == '.') _right[_root[i]] = -1;
    	else _right[_root[i]] = rt-'A';
    }
    preorder(0);
    cout<<pre<<'\n';
    inorder(0);
    cout<<in<<'\n';
    postorder(0);
    cout<<post<<'\n';
}

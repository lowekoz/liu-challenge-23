#include <bits/stdc++.h>
using namespace std;

const char nl = '\n';

int n, k, tmp, xtot, rtot, i, j;
vector<int> x, r;

void YES() {
	cout << "Yes" << nl;
}

void NO() {
	cout << "No" << nl;
}

#define is(x) cerr << #x << " is " << x << endl;

//#define DEBUG
#ifdef DEBUG
void dbg(string text) {
	cerr << text << nl;
	is(x[0]); is(x[1]); is(x[2]); is(x[3]);
	is(xtot);
	is(r[0]); is(r[1]); is(r[2]); is(r[3]);
	is(rtot);

}
#else
void dbg(string text) {};
#endif // DEBUG


void solve() {
	n, k; cin >> n >> k;
	x = vector<int>(4, 0);
	vector<vector<int>> inp(n, vector<int>());
	for (i = 0; i < n; i++) {
		cin >> tmp;
		inp[i].resize(tmp);
		for (j = 0; j < tmp; j++) {
			int weight; cin >> weight;
			inp[i][j] = weight;
			weight /= 5;
			x[weight - 1]++;
		}
	}
	r = vector<int>(4, 0);
	for (i = 0; i < 4; i++) {
		r[i] = (x[i] + k - 1) / k; // same as ceil operation
	}
	xtot = 0;
	rtot = 0;
	for (i = 0; i < 4; i++) {
		xtot += x[i];
		rtot += r[i];
	}

	if (k == 1) {
		YES();
		dbg("k is 1");
		return;
	}

	if (rtot > n) {
		NO();
		dbg("rtot is > n");
		return;
	}

	if (n == 1) {
		YES();
		dbg("n is 1 and rtot <= n");
		return;
	}

	if (n == 2) {
		vector<int> a;
		for (i = 0; i < (int)inp[0].size(); i++) {
			a.push_back(inp[0][i]);
		}
		for (i = (int)inp[1].size() - 1; i >= 0; i--) {
			a.push_back(inp[1][i]);
		}
		int cond = 0;
		for (i = 0; i < (int)a.size()-1; i++) {
			if (a[i] != a[i + 1]) cond++;
		}

		if (cond >= 2) {
			NO();
			dbg("n is 2 and scrambled");
			return;
		}
		else {
			YES();
			dbg("n is 2 and not scrambled");
			return;
		}
	}

	if (xtot <= (n - 1) * k) {
		YES();
		dbg("empty rack and rtot <= n");
		return;
	}
	else {
		int locked = xtot - (n - 1) * k;
		vector<int> cnt(4, 0);
		for (int i = 0; i < n; i++) {
			int weightType = inp[i][0];
			for (int j = 0; j < locked; j++) {
				if (inp[i][j] != weightType) {
					NO();
					dbg("can never reach unordered");
					return;
				}
			}
			cnt[(weightType / 5) - 1]++;
		}

		for (int i = 0; i < 4; i++) {
			if (cnt[i] < r[i]) {
				NO();
				dbg("locked weights are not superset of required");
				return;
			}
		}
		YES();
		dbg("locked is ordered and is superset");
		return;
	}
}


int main() {
	solve();
}

/*

n k
b1 a1 a2 ..
b2 a1 a2 ..
b3 a1 a2 ..

3 3
0
3 5 10 15
3 15 15 15

3 1
1 5
0
1 10

3 4
4 5 5 5 5
4 10 10 15 15
0

3 4
4 5 5 5 5
4 10 10 15 15
1 10

2 4
2 5 10
1 10

2 4
2 5 10
1 5

3 4
4 5 5 5 5
4 10 10 15 10
1 15

*/
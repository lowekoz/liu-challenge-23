#include <bits/stdc++.h>

//#include <vector>
//#include <iostream>

using namespace std;

const char nl = '\n';


int main() {
	int N; cin >> N;
	long long k = 0;
	long long prev = 0;
	vector<long long> A(N);
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		prev -= A[i];
		k += prev;
	}

	// analytical approach
	// y = k + (N+1)x as close to 0 as possible
	// 0 = k + Nx solve for x =>
	// x = -k/N up or down
	long double x = -k / (double)(N+1); // exact

	// integer solution candidates
	long long up = ceil(x);
	long long down = floor(x);

	// best option is the one closer to 0 all said and done
	long long lh = abs(up * (N + 1) + k);
	long long rh = abs(down * (N + 1) + k);
	long long best = min(lh, rh);
	long long target = best == lh ? up : down;

	// reconstrct logic
	k = 0;
	prev = 0;
	cout << target << " ";
	for (int i = 0; i < N; i++) {
		prev -= A[i];
		cout << prev + target << " ";
	}
	cout << nl;
}
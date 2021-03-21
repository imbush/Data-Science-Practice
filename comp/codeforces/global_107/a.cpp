#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define REP(i, a, b) for (int i=a; i<b; i++)

int INF = 1000000005; 
long long INFF = 1000000000000000005LL; 

int main() {
    int n, q;
    int num_ones = 0;
    cin >> n >> q;
    vector<ll> a(n);
    REP(i, 0, n) {
        cin >> a[i];
        num_ones += a[i];
    }

    REP(i, 0, q) {
        int t, k;
        cin >> t >> k;
        if (t == 1) {
            a[k-1] = 1 - a[k-1];
            if (a[k-1] == 1) {
                num_ones ++;
            } else {
                num_ones --;
            }
        } else {
            if (k > num_ones) {
                cout << 0 << "\n";
            } else {
                cout << 1 << "\n";
            }
        }
    }
}
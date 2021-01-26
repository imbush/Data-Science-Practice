#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <math.h>
using namespace std;

typedef long long ll;
typedef vector<ll> vi;

ll max_min(vi, vi, ll);

int main() {
    ll t, m , n, l, r, k;
    string inst;
    cin >> t;
    vector<ll> prints {};

    for (int i = 0; i < t; i++) {
        
        cin >> n >> m;
        cin >> inst;
        vi sums(n + 1, 0);
        k = 0;

        for (int j = 0; j < n; j++) {
            if ((char)inst[i] == (char)"+") {
                k++;
            }
            else {
                k--;
            }
            sums[i + 1] = k;
        }

        for (int j = 0; j < n; j++) {
            cin >> l >> r;
            vi first {sums.begin(), sums.begin() + l};
            vi second {sums.begin() + r + 1, sums.end()};
            prints[j] = max_min(first, second, sums[r] - sums[l - 1]) + 1;
        }
    }

    for (int i = 0; i < t; i++) {
        cout << prints[i] << "\n";
    }
}

ll max_min(vi l1, vi l2, ll diff) {
    ll minimum = 0LL;
    ll maximum = 0LL;
    for (int i = 0; i < l1.size(); i++) {
        if (l1[i] < minimum) {
            minimum = l1[i];
        }
        if (l1[i] > maximum) {
            maximum = l1[i];
        }
    for (int i = 0; i < l2.size(); i++) {
        if (l2[i] - diff < minimum) {
            minimum = l2[i] - diff;
        }
        if (l2[i] - diff > maximum) {
            maximum = l2[i] - diff;
        }
    }
    return (maximum - minimum);
}
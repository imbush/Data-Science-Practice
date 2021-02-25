#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int main() {
    ll t, a, b, n;
    cin >> t;
    vector<bool> output(t);
    for (ll j = 0; j < t; j++) {
        cin >> a >> b >> n;
        vector<ll> la(n), lb(n);
        for (ll i = 0; i < n; i++) {
            cin >> la[i];
        }
        for (ll i = 0; i < n; i++) {
            cin >> lb[i];
        }
        ll maximum = 0, dam = 0;
        for (ll i = 0; i < n; i++) {
            maximum = max(maximum, la[i]);
            dam += la[i] * ((lb[i] + a - 1) / a);
        }
        output[j] = (dam >= b + maximum) ? 0 : 1;
    }
    for (ll i = 0; i < output.size(); i++) {
        if (output[i]) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
}
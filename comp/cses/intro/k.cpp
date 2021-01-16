#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
    ll t, a, b;
    cin >> t;
    ll two_t = 2 * t;
    vector<ll> tests(2 * t);

    for (int i = 0; i < two_t; i += 2) {
        cin >> tests[i] >> tests[i + 1];
    }

    for (int i = 0; i < two_t; i += 2) {
        a = tests[i];
        b = tests[i + 1];
        if (((2 * a - b) % 3 == 0) && (2 * min(a, b) >= max(a, b))) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
}
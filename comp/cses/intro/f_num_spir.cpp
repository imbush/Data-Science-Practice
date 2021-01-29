#include <iostream>
using namespace std;

typedef long long ll;

ll row_column(ll, ll);

int main() {
    int n;
    cin >> n;
    ll x[n], y[n];
    for (int i = 0; i < n; i++) {
        cin >> y[i] >> x[i];
    }
    for (int i = 0; i < n; i++) {
        cout << row_column(x[i], y[i]) << "\n";
    }
}

ll row_column(ll x, ll y) {
    if (x >= y) {
        if (x % 2 == 1) {
            return x * x + 1 - y;
        }
        return (x - 1) * (x - 1) + y;
    } else {
        if (y % 2 == 0) {
            return y * y + 1 - x;
        }
        return (y - 1) * (y - 1) + x;
    }
}
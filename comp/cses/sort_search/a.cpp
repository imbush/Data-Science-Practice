#include <iostream>
#include <set>

using namespace std;

typedef long long ll;

int main() {
    ll n, x;
    set<ll> x_set;

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        x_set.insert(x);
    }
    cout << x_set.size() << "\n";
}
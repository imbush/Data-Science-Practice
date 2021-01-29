#include <iostream>

using namespace std;

typedef long long ll;

int main() {
    ll n, count = 0;
    cin >> n;
    for (ll pow_5 = 5LL; pow_5 <= n; pow_5 *= 5LL) {
        count += n / pow_5;
    }
    cout << count;
}
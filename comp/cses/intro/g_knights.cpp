#include <iostream>
using namespace std;

typedef long long ll;

int main() {
    ll n;
    ll sum = 0;
    cin >> n;
    cout << sum << "\n";
    for (ll i = 2; i <= n; i ++) {
        sum += (2 * i - 1) * (2 * i - 2) / 2;  // The outside interactions
        if (i > 2) {
            sum -= 4;
        }
        sum += (2 * i - 1) * (i * i - 2 * i + 1); // Inner pairs with top left
        for (ll j = 0; j < i - 1; j ++) {
            sum -= 8;
            if (j == 0) {
                sum += 4;
            } else if (j == 1) {
                sum += 2;
            }
            
            if (j == i - 2) {
                sum += 4;
            } else if (j == i - 3) {
                sum += 2;
            }
        }
        cout << sum << "\n";
    }
}
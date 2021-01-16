#include <iostream>
using namespace std;

typedef long long ll;

int main() {
    ll n;
    ll power_2 = 1;
    cin >> n;

    for (int i = 0; i < n; i ++) {
        power_2 = (power_2 << 1) % 1000000007;
    }
    cout << power_2 << "\n";
}
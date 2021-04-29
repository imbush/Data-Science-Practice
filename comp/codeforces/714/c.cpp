#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef long long ll;

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        ll n, operations;
        cin >> n >> operations;
        vector<ll> digits(10);
        while (n) {
            digits[n % 10] += 1;
            n /= 10;
        }
        for (ll j = 0; j < operations / 10; j++) {
            ll nines = digits[9];
            for (int dig = 8; dig >= 0; dig--) {
                digits[dig + 1] = digits[dig];
            }
            digits[0] = nines;
            digits[1] = (digits[1] + nines) % 1000000007LL;
        }

        for (ll j = 0; j < operations; j++) {
            ll nines = digits[9];
            for (int dig = 8; dig >= 0; dig--) {
                digits[dig + 1] = digits[dig];
            }
            digits[0] = nines;
            digits[1] = (digits[1] + nines) % 1000000007LL;
        }
        cout << (digits[0] + digits[1] + digits[2] + digits[3] + digits[4] + digits[5] + digits[6] + digits[7] + digits[8] + digits[9]) % 1000000007LL << "\n";
    }
}
#include <iostream>
#include <vector>

using namespace std;

typedef long long ll;

int main() {
    ll n;
    ll count = 0;
    ll last1 = -1;
    ll last2 = -1;
    cin >> n;
    vector<ll> la(n);
    for (ll i = 0; i < n; i++) {
        cin >> la[i];
    }
    for (ll i = 0; i < n; i++) {
        if (la[i] == last1) {
            if (la[i] != last2) {
                count ++;
            }
            last2 = la[i];
        } else if (la[i] == last2) {
            last1 = la[i];
            count ++;
        } else if (i == n-1) {
            count ++;
        } else if (la[i+1] == last1) {
            last1 = la[i];
            count ++;
        } else {
            last2 = la[i];
            count ++;
        }
    }
    cout << count << "\n";
}
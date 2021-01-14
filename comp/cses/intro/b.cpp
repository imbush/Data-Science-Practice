#include <iostream>
using namespace std;

typedef long long ll;

int main() {
    ll n, s=0;
    int a;
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        cin >> a;
        s += a;
    }
    cout << n * (n + 1) / 2 - s << "\n";
}
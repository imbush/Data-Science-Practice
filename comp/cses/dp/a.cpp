#include <iostream>
#include <vector>
using namespace std;

typedef long long ll;

int main() {
    int n;
    cin >> n;
    vector<ll> combos(n + 1, 0LL);
    combos[0] = 1LL;
    for (int i = 0; i < n; i ++) {
        for (int j = i + 1; j < n + 1 && j <= i + 6; j ++) {
            combos[j] = (combos[j] + combos[i]) % 1000000007LL;
        } 
    }
    cout << combos[n] << "\n";
}
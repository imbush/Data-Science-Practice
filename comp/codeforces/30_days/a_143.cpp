#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, p, v, t, count=0;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> p >> v >> t;
        count += (p & v) || (p & t) || (v & t);
    }
    cout << count << "\n";
}
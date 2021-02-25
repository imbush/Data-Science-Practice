#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int main() {
    int n;
    ll x;
    cin >> n >> x;
    vector<ll> t1(n / 2);
    vector<ll> t2;
    for (int i = 0; i < t1.size(); i++) {
        cin >> t1[i];
    }
    for (int i = 0; i < n / 2; i++) {
        cin >> t2[i]; // Segmentation fault occurs here
    }
    sort(t1.begin(), t1.end());
    sort(t2.begin(), t2.end());

    vector<ll> sums1;
    for (int b = 0; b < (1 << t1.size()); b++) {
        ll sum = 0;
        for (int i = 0; i < t1.size(); i++) {
            if (b & (1 << i)) sum += t1[i];
            if (sum > x) break;
        }
        if (sum > x) break;
        sums1.push_back(sum);
    }

    vector<ll> sums2;
    for (int b = 0; b < (1 << t2.size()); b++) {
        ll sum = 0;
        for (int i = 0; i < t2.size(); i++) {
            if (b & (1 << i)) sum += t2[i];
            if (sum > x) break;
        }
        if (sum > x) break;
        sums1.push_back(sum);
    }

    ll num_ways = 0;
    int i = 0, j = sums2.size();
    while (i < sums1.size() & j > -1) {
        ll sum = sums1[i] + sums2[j];
        if (sum == x) {
            num_ways ++;
        } else if (sum < x) {
            i ++;
        } else {
            j --;
        }
    }
    cout << num_ways << "\n";
}
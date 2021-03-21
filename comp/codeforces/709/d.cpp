#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;

typedef long long ll;

int main() {
    int t, n;
    cin >> t;
    for (int i = 0; i < t; i ++) {
        cin >> n;
        vector<ll> a(n);
        vector<vector<ll> > a_facts(n);
        vector<ll> deleted;
        for (ll j = 0; j < n; j ++) {
            ll k;
            cin >> k;
            a[j] = k;
            for (ll m = 2; m <= k; m ++) {
                if (k == 1LL) {
                    break;
                } else if (k % m == 0) {
                    a_facts[j].push_back(i);
                    while (k % m == 0) {
                        k /= m;
                    }
                }
            }
        }
        bool deletion = true;
        while(deletion) {
            deletion = false;
            for (int j = 0; j < a.size(); j ++) {
                cout << "here 1";
                int next_j = (j + 1) % a.size();
                bool share_factor = false;
                ll x = 0, y = 0;
                while (true) {
                    cout << "here 2";
                    if (a_facts[j][x] == a_facts[next_j][y]) {
                        share_factor = true;
                        break;
                    } else if (a_facts[j][x] > a_facts[next_j][y]) {
                        y ++;
                    } else {
                        x ++;
                    }
                }
                if (! share_factor) {
                    cout << "here 3";
                    deletion = true;
                    a_facts.erase(a_facts.begin() + next_j);
                    deleted.push_back(a[next_j]);
                    a.erase(a.begin() + next_j);
                }
            }
        }
        cout << "\n" << deleted.size();
        for (int j = 0; j < deleted.size(); j ++) {
            cout << " " << deleted[j];
        }
    }
}


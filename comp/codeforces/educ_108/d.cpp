#include <iostream>
#include <vector>


using namespace std;
typedef long long ll;

int main() {
    int n;
    vector<ll> a(n);
    vector<ll> b(n);
    vector<ll> prods;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> a[i];
    }
    for (int i = 0; i < n; i ++) {
        cin >> b[i];
        prods.push_back(b[i] * a[i]);
    }

    ll max_diff = 0;
    for (int cent = 0; cent < n; cent++) {
        ll diff = 0;
        vector<ll>::iterator ai = a.begin() + cent - 1;
        vector<ll>::iterator aj = ai + 2;
        vector<ll>::iterator bi = b.begin() + cent - 1;
        vector<ll>::iterator bj = bi + 2;
        vector<ll>::iterator prodsi = prods.begin() + cent - 1;
        vector<ll>::iterator prodsj = prodsi + 2;
        while (bi >= b.begin() & bj < b.end()) {
            diff += *ai * *bj + *ai * *bj - *prodsi - *prodsj;
            if (diff > max_diff) {
                max_diff = diff;
            }
            --ai;
            ++aj;
            --bi;
            ++bj;
            --prodsi;
            ++prodsj;
        }
    }

    for (int cent = 0; cent < n; cent++) {
        ll diff = 0;
        vector<ll>::iterator ai = a.begin() + cent;
        vector<ll>::iterator aj = ai + 1;
        vector<ll>::iterator bi = b.begin() + cent;
        vector<ll>::iterator bj = bi + 1;
        vector<ll>::iterator prodsi = prods.begin() + cent;
        vector<ll>::iterator prodsj = prodsi + 1;
        while (ai >= a.begin() & aj < a.end()) {
            diff += *ai * *bj + *ai * *bj - *prodsi - *prodsj;
            if (diff > max_diff) {
                max_diff = diff;
            }
            --ai;
            ++aj;
            --bi;
            ++bj;
            --prodsi;
            ++prodsj;
        }
    }
    ll prods_sum;
    for (int i=0; i < n; i++) {
        prods_sum += prods[i];
    }
    cout << (prods_sum + max_diff);
}

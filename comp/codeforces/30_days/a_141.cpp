#include <iostream>
#include <set>
using namespace std;

typedef long long ll;
int main() { 
    ll shoe;
    set<ll> shoes;
    for (int i = 0; i < 4; i++) {
        cin >> shoe;
        shoes.insert(shoe);
    }
    cout << 4 - shoes.size() << "\n";
}
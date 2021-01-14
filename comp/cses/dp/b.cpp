#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int x, n;
    cin >> x >> n;
    vector<int> coins(n, 0);
    for (int i = 0; i < x; i++) {
        cin >> coins[i];
    }
    sort(coins.begin(), coins.end());
    vector<int> ways(n + 1, 0);
    int max_search = n + 1 - coins[0];
    for (int i = 0; i < coins.size(); i ++) {
        cout << coins[i] << " ";
    }
    for (int i = 0; i < max_search; i++) {
        if (ways[i] != 0 || i == 0) {
            cout << "hey";
            for (int j = 0; j < x; j++) {
                cout << "this";
                if (coins[j] + i > n) {
                    break;
                } else if (ways[coins[j] + i] > ways[i] + 1 || ways[coins[j] + i] == 0) {
                    cout << "  " << (ways[i] + 1) << "  " << coins[j] << " - " << i << "  ";
                    ways[coins[j] + i] = ways[i] + 1;
                }
            }
        }
    }
    for (int i = 0; i < ways.size(); i ++) {
        cout << ways[i] << " ";
    }
    if (ways[-1] != 0) {
        cout << ways[n];
    } else {
        cout << -1 << "\n";
    }
}
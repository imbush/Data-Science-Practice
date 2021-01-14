#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main() {
    int t;
    cin >> t;
    vector<int> tests(t, 0);
    for (int i = 0; i < t; i++) {
        cin >> tests[i];
    }
    string s = "989";
    int max_test = *max_element(tests.begin(), tests.end());

    if (max_test > 3) {
        int n = 0;
        for (int i = 3; i < max_test; i ++) {
            s += to_string(n);
            n = (n + 1) % 10;
        }
    }

    for (int i = 0; i < t; i++) {
        cout << s.substr(0, tests[i]) << "\n";
    }
}
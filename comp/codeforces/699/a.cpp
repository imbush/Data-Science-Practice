#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int t, px, py;
    bool can_x, can_y;
    string s;
    cin >> t;
    vector<bool> out(t);

    for (int i = 0; i < t; i++) {
        cin >> px >> py;
        cin >> s;
        if (px == 0) {
            can_x = 1;
        } else if (px > 0) {
            can_x = (px <= count(s.begin(), s.end(), 'R')) ? 1 : 0;
        } else {
            can_x = (-px <= count(s.begin(), s.end(), 'L')) ? 1 : 0;
        }

        if (py == 0) {
            can_y = 1;
        } else if (py > 0) {
            can_y = (py <= count(s.begin(), s.end(), 'U')) ? 1 : 0;
        } else {
            can_y = (-py <= count(s.begin(), s.end(), 'D')) ? 1 : 0;
        }

        out[i] = (can_x & can_y);
    }

    for (int i = 0; i < t; i++) {
        if (out[i]) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
}
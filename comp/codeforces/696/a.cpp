#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef long long ll;
int main() {
    int t, n;
    string input;
    int last_sum;
    string a;
    vector<vector<int>> bs;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cin >> n;
        cin >> input;
        bs.push_back(vector<int>(input.begin(), input.end()));
    }

    for (vector<int> b : bs) {
        a = "1";
        last_sum = b[0];

        for (int i = 1; i < b.size(); i++) {
            if (b[i] == last_sum) {
                a += "0";
                last_sum = b[i] - 1;
            } else {
                a += "1";
                last_sum = b[i];
            }
        }
        cout << a << "\n";
    }
}
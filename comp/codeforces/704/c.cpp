#include <iostream>
#include <string>
#include <vector>

using namespace std;
typedef long long ll;

int main() {
    int m, n, minimum, i, current;
    cin >> n >> m;
    string s, t;
    cin >> s;
    cin >> t;
    vector<int> firsts(m);
    vector<int> seconds(m);

    current = 0;
    i = 0;
    while (current < m) {
        if (s[i] == t[current]) {
            firsts[current] = i;
            current += 1;
        }
        i ++;
    }

    current = m-1;
    i = n - 1;
    while (current > 0) {
        if (s[i] == t[current]) {
            seconds[current] = i;
            current -= 1;
        }
        i --;
    }

    for (int j=0; j<m-1; j++) {
        minimum = max(minimum, seconds[j+1] - firsts[j]);
    }
    cout << minimum << "\n";
}
#include <iostream>
#include <vector>

using namespace std;

#define REP(i, a, b) for (long long i=a; i<b; i++)

int main() {
    int t;
    cin >> t;
    for (int i=0; i<t; i++) {
        long long n, count=0;
        cin >> n;
        vector<int> s(n);
        for (int j=0; j<n; j++) {
            cin >> s[j];
        }
        long long j = 0;
        while (j < n) {
            if (s[j] == 1) {
                j ++;
            } else {
                if (s[j] + j >= n) {
                    count += s[j] - n + j;
                    count ++;
                    s[j] = n - j - 1;
                }
                count += s[j] - 1;

                long long l = j + s[j];
                while (l > 1) {
                    while (l < n) {
                        if (s[l] == 1) {
                            l ++;
                        } else {
                            s[l] --;
                            l += s[l];
                            l ++;
                        }
                    }
                    s[j] --;
                    l = j + s[j];
                }
                j ++;
            }
        }
        cout << count << "\n";
    }
}
#include <iostream>
using namespace std;

int main() {
    string a;
    cin >> a;
    int max_len = 0, current_len = 0;
    char current = 'A';
    for (int i = 0; i < a.length(); i++) {
        if (a[i] == current) {
            current_len += 1;
        } else {
            current = a[i];
            current_len = 1;
        }

        if (current_len > max_len) {
            max_len = current_len;
        }
    }
    cout << max_len << '\n';
}
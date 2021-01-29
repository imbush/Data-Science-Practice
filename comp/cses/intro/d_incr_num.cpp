#include <iostream>
using namespace std;

int main() {
    long long a, current, sum = 0;
    cin >> a >> current;
    long long x;

    for (int i = 0; i < a - 1; i++) {
        cin >> x;
        if (x < current) {
            sum += current - x;
        } else {
            current = x;
        }
    }
    cout << sum;
}
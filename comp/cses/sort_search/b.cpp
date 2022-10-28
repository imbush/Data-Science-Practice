#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

int main()
{
    int n, m, k;
    ll a[n];

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    sort(x.begin(), x.end());
    int count = 1;
    for (int i = 1; i < n; i++)
    {
        cout << x[i] << " ";
        if (x[i] != x[i - 1])
        {
            count++;
        }
    }
    cout << count << "\n";
}
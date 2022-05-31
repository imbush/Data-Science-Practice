// Incomplete

#include <iostream>
#include <vector>
#include <string>
using namespace std;

typedef long long ll;
int main()
{
    int t, n;
    string input;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        int array[n];
        for (int j = 0; j < n; j++)
        {
            cin >> array[j];
        }

        bool is_good = true;
        int max_sum_before_k = 0, max_in_sub = array[0];
        for (int k = 0; k < n; k++)
        {
            if (array[k] > max_in_sub)
            {
                max_sum_before_k = max(0, max_in_sub);
                max_in_sub = array[k];
            }
            else
            {
                max_sum_before_k = max(0, array[k]);
            }
            if (max_sum_before_k == 0)
            {
                max_in_sub = array[k];
            }
            if (max_sum_before_k > 0)
            {
                cout << "no\n";
                is_good = false;
                break;
            }
        }
        if (is_good)
        {
            cout << "yes\n";
        }
    }
}
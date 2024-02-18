#include <iostream>
#include <cmath>
using namespace std;

int main()
{
    int x, n;
    cin >> x >> n;

    int sum = 0;
    for (int num = 0; num <= n; num += 2)
    {
        // sum += pow(x, num);
        sum = sum + pow(x, num + 2);
    }

    cout << sum << endl;
    return 0;
}

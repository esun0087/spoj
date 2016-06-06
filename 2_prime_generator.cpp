#include <iostream>

using namespace std;


int main()
{
    const int prime_len = 32000;
    bool prime[prime_len];
    for(int i = 0; i < prime_len; ++i)
        prime[i] = true;
    prime[0] = prime[1] = false;

    for(int i = 2; i * i <= prime_len; ++i)
    {
        if(!prime[i])
            continue;
        for(int j = i * i; j <= prime_len; j += i)
            prime[j] = false;
    }
    int m, n;
    int t;
    cin >> t;
    for(int iter  = 0; iter < t; ++iter)
    {
        const int len = 100001;
        cin >> m >> n;
        bool be_prime[len];
        for(int i = 0; i < len; ++i)
            be_prime[i] = true;
        for(int i = 2; i < prime_len; ++i)
        {
            if(i * i > n)
                break;
            if(!prime[i])
                continue;
            
            int start = i - m % i;
            if(start % i == 0)
                start = 0;
            if((start + m) / i == 1)
                start += i;
            for(int j = start; j <= len ; j += i)
            {
                
                be_prime[j] = false;
            }
                
        }
        for(int i = 0 ; i <= n - m ; ++i)
            if(be_prime[i])
                if (i+m != 1)
                cout << i + m << endl;

    }
    
}
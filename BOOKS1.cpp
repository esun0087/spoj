#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 510;

int a[MAXN], use[MAXN];
long long  low_bound, high_bound;
int n, m;

void init()
{
    low_bound = -1;
    high_bound = 0;
    memset(use, 0, sizeof(use));
}

int solve(int mid)
{
    int sum = 0, group = 1;
    for(int i = n-1; i >= 0; i--)
    {
        if(sum + a[i] > mid)
        {
            sum = a[i];
            group++;
            if(group > m) return 0;
        }
        else sum += a[i];
    }
    return 1;
}

void print(int high_bound)
{
    int group = 1, sum = 0;
    for(int i = n-1; i >= 0; i--)
    {
        if(sum + a[i] > high_bound)
        {
            use[i] = 1;
            sum = a[i];
            group++;
        }
        else sum += a[i];
        if(m-group == i+1)
        {
            for(int j = 0; j <= i; j++)
                use[j] = 1;
            break;
        }
    }
    for(int i = 0; i < n-1; i++)
    {
        printf("%d ", a[i]);
        if(use[i]) printf("/ ");
    }
    printf("%d\n", a[n-1]);
}

int main()
{
    int T;
    scanf("%d%*c", &T);
    while(T--)
    {
        init();
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            if(low_bound < a[i]) low_bound = a[i];
            high_bound += a[i];
        }
        long long x = low_bound, y = high_bound;
        while(x <= y)
        {
            long long  mid = x+(y-x)/2;
            if(solve(mid)) y = mid-1;
            else x = mid+1;
        }
        print(x);
    }
    return 0;
}
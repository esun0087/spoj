#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <algorithm>
#include <vector>
#include <cstring>
#include <stack>
#include <cctype>
#include <utility>   
#include <map>
#include <string>  
#include <climits> 
#include <set>
#include <string>    
#include <sstream>
#include <utility>   
#include <ctime>
#include <bitset>
#include <iomanip>
//#pragma comment(linker, "/STACK:102400000,102400000")

using namespace std;


typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned UN;
typedef pair<ULL, ULL> PAIR;
typedef multimap<int, int> MMAP;
typedef long double LF;

const int MAXN(30);
const int MAXM(310);
const int MAXE(310);
const int MAXK(6);
const int HSIZE(131313);
const int SIGMA_SIZE(26);
const int MAXH(18);
const int INFI((INT_MAX-1) >> 1);
const ULL BASE(31);
const LL LIM(1e13);
const int INV(-10000);
const int MOD(1000000007);
const double EPS(1e-7);
const LF PI(acos(-1.0));

template<typename T> inline void checkmax(T &a, T b){if(b > a) a = b;}
template<typename T> inline void checkmin(T &a, T b){if(b < a) a = b;}
template<typename T> inline T ABS(const T &a){return a < 0? -a: a;}

bool E[MAXN][MAXN];
int indeg[MAXN];
int mp[MAXN];
char str[10010][1010];

void dfs(int l, int r, int dep)
{
	if(l == r) return;
	int tl = l, tr;
	while(tl < r)
	{
		while(tl <= r && str[tl][dep] == '\0') ++tl;
		tr = tl+1;
		while(tr <= r && str[tr][dep] == str[tl][dep]) ++tr;
		if(tr <= r && str[tr][dep] != '\0') 
		{
			indeg[str[tr][dep]-'a'] += E[str[tl][dep]-'a'][str[tr][dep]-'a']? 0: 1;
			E[str[tl][dep]-'a'][str[tr][dep]-'a'] = true;
		}
		dfs(tl, tr-1, dep+1);
		tl = tr;
	}
}

int que[MAXN], front, back;
bool solve(int n)
{
	front = back = 0;
	for(int i = 0; i < n; ++i)
		if(indeg[i] == 0)
		{
			que[back++] = i;
			indeg[i] = -1;
		}
	while(front < back)
	{
		if(back-front > 1) return false;
		while(front < back)
		{
			int cur = que[front];
			mp[cur] = front++;
			for(int i = 0; i < n; ++i)
				if(E[cur][i])
					--indeg[i];
		}
		for(int i = 0; i < n; ++i)
			if(indeg[i] == 0)
			{
				que[back++] = i;
				indeg[i] = -1;
			}
	}
	if(back < n) return false;
	return true;
}

int main()
{
	int TC;
	scanf("%d", &TC);
	while(TC--)
	{
		int n, K;
		scanf("%d%d", &n, &K);
		memset(E, 0, sizeof(E));
		memset(indeg, 0, sizeof(indeg));
		for(int i = 0; i < K; ++i) 
		{
			scanf("%s", str[i]);
			int len = strlen(str[i]);
		}
		while(getchar() != '\n');
		dfs(0, K-1, 0);
		char temp;
		if(solve(n))
		{
			while((temp = getchar()), temp != '\n' && temp != EOF)
			{
				if(temp >= 'a' && temp-'a' < n) putchar(mp[temp-'a']+'a');
				else putchar(temp);
			}
			putchar('\n');
		}
		else
		{
			printf("Message cannot be decrypted.\n");
			while((temp = getchar()), temp != '\n' && temp != EOF);
		}
	}
	return 0;
}
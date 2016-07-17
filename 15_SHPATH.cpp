#include<iostream>
#include<cstdio>
#include<map>
#include<queue>
#include<cstring>
using namespace std;
const int size = 200010;
const int INF = 2 << 28;
map <string,int> maps;
struct Edge{int to,dist;}edges[size];
int tot,head[size],next[size];

void build(int f,int t,int d)
{
    edges[++tot].to = t;
    edges[tot].dist = d;
    next[tot] = head[f];
    head[f] = tot;
}
struct HeapNode{
    int u,d;
    bool operator < (const HeapNode &rhs) const
    {
        return d > rhs.d;
    }
};
int n;
struct Dijkstra{
    int n,m;
    int d[size];
    bool vis[size];
    int p[size];
    void init(int n)
    {
        this -> n = n;
        memset(vis,0,sizeof(vis));
    }
    void dijkstra(int s)
    {
        fill(d,d+1+n,INF);
        memset(vis,0,sizeof(vis));
        priority_queue <HeapNode> q;
        q.push((HeapNode){s,0});
//      vis[s] = 1; 不能加的一句话 
        d[s] = 0;
        while(q.size())
        {
            HeapNode f = q.top();
            q.pop();
            int u = f.u;
            if(vis[u])  continue;
            vis[u] = 1;
            for(int i = head[u];i;i = next[i])
            {
                int v = edges[i].to;
                if(d[v] > d[u] + edges[i].dist)
                {
                    d[v] = d[u] + edges[i].dist;
                    q.push((HeapNode){v,d[v]});
                }
            }
        }
    }
};

Dijkstra dijkstra;


int main()
{
    int t;
    scanf("%d",&t);
    for(int i = 1;i <= t;i ++)
    {
        memset(edges,0,sizeof(edges));
        memset(next,0,sizeof(next));
        memset(head,0,sizeof(head));
        maps.clear();
        int tott = 0;
        tot = 0;
        scanf("%d",&n);
        dijkstra.init(n);
        for(int i = 1;i <= n;i ++)
        {
            string s1;
            int ct;
            cin>>s1;
            maps[s1] = ++tott;
            scanf("%d",&ct);
            for(int i = 1;i <= ct;i ++)
            {
                int a,b;
                scanf("%d%d",&a,&b);
                build(maps[s1],a,b);
            }
        }
        int q;
        scanf("%d",&q);
        string s1,s2;
        for(int i = 1;i <= q;i ++)
        {
            cin>>s1>>s2;
            dijkstra.dijkstra(maps[s1]);
            printf("%d\n",dijkstra.d[maps[s2]]);
        }
    }
    return 0;
}
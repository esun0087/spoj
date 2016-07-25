#include<cstdio>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
using namespace std;
#define inf (1e20)
#define eps (1e-3)
#define pi  (acos(-1.0))
double ansx[35],ansy[35],d[35],x[1005],y[1005];
double dist(double a,double b,double x,double y)//求两点距离
{
    return sqrt((a-x)*(a-x)+(b-y)*(b-y));
}
int main()
{
    int cas,n;
    double xi,yi,px,py,cnt,dx,dy,tx,ty,td;
    scanf("%d",&cas);
    srand((unsigned)time(NULL));//设置随机数种子
    for(;cas--;)
    {
        scanf("%lf%lf%d",&xi,&yi,&n);
        for(int i=0;i<n;++i)
             scanf("%lf%lf",x+i,y+i);
        for(int i=0;i<35;++i)//初始解集
        {
            ansx[i]=double(rand()%1000)/1000*xi;
            ansy[i]=double(rand()%1000)/1000*yi;
            d[i]=inf;
            for(int j=0;j<n;++j)
                d[i]=min(d[i],dist(ansx[i],ansy[i],x[j],y[j]));
        }
        double delta=double(max(xi,yi))/(sqrt(1.0*n));//初始温度
        for(;delta>eps;)
        {
            for(int i=0;i<35;++i)
            {
                px=ansx[i];
                py=ansy[i];
                for(int j=0;j<35;++j)
                {
                    cnt=double(rand()%1000)/1000*10*pi;
                    dx=delta*cos(cnt);
                    dy=delta*sin(cnt);
                    tx=px+dx;
                    ty=py+dy;
                    if(tx<0||tx>xi||ty<0||ty>yi) continue;
                    td=inf;
                    for(int k=0;k<n;++k)
                        td=min(td,dist(tx,ty,x[k],y[k]));
                    if(td>d[i])//更新更优解
                    {
                        d[i]=td;
                        ansx[i]=tx;
                        ansy[i]=ty;
                    }
                }
            }
            delta*=0.8;//减小温度
        }
        double ans=0;
        int k;
        for(int i=0;i<35;++i)//找最优解
            if(d[i]>ans)
            {
                k=i;
                ans=d[i];
            }
        printf("The safest point is (%.1f, %.1f).\n",ansx[k],ansy[k]);
    }
    return 0;
}

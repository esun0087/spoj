#include <stdio.h>
#include <string.h>

int main()
{
	int t,len,l,m,r,c,cur;
	char K[1000001],tmp[1000001];
	scanf("%d",&t);
	while(t--)
	{
		memset(K,0,sizeof(K));
		memset(tmp,0,sizeof(tmp));
		scanf("%s",K);
		len=strlen(K);
		if(len==1&&K[0]<'9')
			printf("%c\n",K[0]+1);
		else if(len==1)
			printf("11\n");
		else
		{
			strcpy(tmp,K);
			for(l=0,r=len-1;l<r;l++,r--) tmp[r]=tmp[l];
			if(strcmp(tmp,K)>0)
				printf("%s\n",tmp);
			else
			{
				cur=m=len>>1;
				tmp[cur]+=1;
				c=(tmp[cur]>'9')?1:0;
				for(;c&&cur<len;cur++)
				{
					tmp[cur]='0';
					tmp[cur+1]+=1;
					c=(tmp[cur+1]>'9')?1:0;
				}
				if(cur==len) tmp[len++]='1';
				for(l=0,r=len-1;r>=m;l++,r--) K[l]=tmp[r];
				l=(len&0x1)?(m+1):m;
				for(;l<len;l++) K[l]=tmp[l];
				printf("%s\n",K);
			}
		}
	}
	return 0;
}
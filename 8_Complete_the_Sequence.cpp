#include <iostream>
#include <vector>
#include <string>

using namespace std;

void CompleteTheSequence()
{
  int T = 0;
  cin>>T;
  int S = 0, C = 0;
  while (T--)
  {
    cin>>S>>C;
    if (S < 1) continue;

    vector<vector<int> > A(S, vector<int>(S+C));
    for (int i = 0; i < S; i++) cin>>A[0][i];

    for (int i = 1; i < S; i++)
    {
      for (int j = 0; j < S-i; j++)
      {
        A[i][j] = A[i-1][j+1] - A[i-1][j];
      }
    }
    for (int i = 1; i <= C; i++) A[S-1][i] = A[S-1][0];
    for (int i = S - 2; i >= 0 ; i--)
    {
      for (int j = S-i; j < S-i+C; j++)
      {
        A[i][j] = A[i][j-1] + A[i+1][j-1];
      }
    }
    
    for (int i = S; i < S+C; i++)
    {
      cout<<A[0][i]<<' ';
    }
    cout<<endl;
  }
}

int main()
{
  CompleteTheSequence();
  return 0;
}
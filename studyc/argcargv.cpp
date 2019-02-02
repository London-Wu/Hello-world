#include <iostream>
using namespace std;

int main(int argc,char *argv[])
{
	int sum=0;
	for(int i=0;i<argc;i++)
	{
		sum+=atoi(argv[i]);//这里用atoi()将字符串转换成整数
	}
	cout << sum << endl;

	return 0;
}

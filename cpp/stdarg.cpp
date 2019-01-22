#include <iostream>
#include <cstdarg>
using namespace std;

int sum(int n,...)
{
	int res=0;
	va_list vap;

	va_start(vap,n);
	for(int i=0;i < n;i++)
	{
		res += va_arg(vap,int);
	}
	va_end(vap);

	return res;
}

int main()
{
	cout << sum(4,1,2,3,5) << endl;
	cout << sum(5,1,2,3,4,5) << endl;
	cout << sum(6,100,200,334,567,123,345) << endl;
	cout << sum(4,-1,99,53,-105) << endl;

	return 0;
}

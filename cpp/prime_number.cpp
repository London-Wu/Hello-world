#include <iostream>
using namespace std;

int main()
{
	int num;
	int pn=0;
	cout << "input a number:";
	cin >> num;
	int temp=2;
	for(temp;temp<num;temp++)
	{
		if(num%temp==0&&num!=2)
		{
			pn=1;
			break;
		}
	}
	if(pn==1)
	{
		cout << "是合数" ;
	} 
	else
	{
		cout << "是质数";
	}
	
	return 0;
}

//辗转相除法(欧几里得算法)求最大公因数及最小公倍数
#include <iostream>
using namespace std;

int main(){
	int num1,num2,a,b,temp;
	cout << "input two numbers:";
	cin >> num1 >> num2;
	a=num1;
	b=num2;
	if(a<b){
		temp=a;
		a=b;
		b=temp;
	}

	while(b!=0){
		temp=a%b;
		a=b;
		b=temp;
		
	}
	cout << num1 << "和" << num2 << "的最大公约数为:" << a << endl;
	cout << num1 << "和" << num2 <<  "的最小公倍数为:" << num1 * num2 / a << endl;

	return 0;
}

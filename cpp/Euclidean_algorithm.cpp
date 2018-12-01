//辗转相除法(欧几里得算法)求最大公因数
#include <iostream>
using namespace std;

int main(){
	int num1;
	int num2;
	cout << "input two numbers:";
	cin >> num1 >> num2;

	int temp;

	while(temp!=0){
		temp=num1%num2;
		num1=num2;
		num2=temp;
		
	}
	cout << "两个数的最大公约数为:" << num1 << endl;

	return 0;
}

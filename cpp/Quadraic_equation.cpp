//例题:解二元一次方程
#include <iostream>
#include <math.h>
using namespace std;

int main(){
	int a;
	int b;
	int c;
	cout << "请输入a,b,c的值:";
	cin >> a >> b >> c;
	
	float dalta = sqrt(b*b-4*a*c);
	if(dalta>=0){
		cout << "x1=" << (-b+dalta)/2*a << endl;
		cout << "x2=" << (-b-dalta)/2*a << endl;
	}
	else{
		cout << "方程无实数根!" << endl;
	}

	return 0;
}

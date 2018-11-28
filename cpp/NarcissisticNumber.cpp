#include <iostream>
using namespace std;

int main(){
	int x,y,z;
	for(int num=100;num<1000;num++){
		x=num%10;
		y=num/10%10;
		z=num/100;
		if (x*x*x+y*y*y+z*z*z==num){
			cout << num << " ";
		}
	}

	return 0;
}

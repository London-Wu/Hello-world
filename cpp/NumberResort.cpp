#include <iostream>
using namespace std;

int main(){
	int num;
	cout << "input a number:";
	cin >> num;

	int digits[20];
	int i=0;
	while(num>0){
		digits[i]=num%10;
		num/=10;
		i++;
	}

	for(int x=0;x<i;x++){
		cout << digits[x];
	}

	return 0;
}

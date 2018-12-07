#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
	char name[100];
	cout << "input your name:" << endl;
	fgets(name,100,stdin);//stdin:标准输入流
	cout << "your name is " << name << endl;

	return 0;
}

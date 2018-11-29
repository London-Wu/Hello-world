#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
using namespace std;

int main()
{
	char name[100];
	cout<<"请输入你的名字:"<<endl;
	cin>>name;
	srand((int)time(NULL));
	int num=rand()%100+1;
	int ci=10;
	int input;
	while(ci)
	{
		ci-=1;
		cout<<"撸"<<name<<"几次?";
		cin>>input;
		if(input>num)
		{
			cout<<"撸太多了,"<<name<<"的juhua要裂了!"<<endl;
		}
		else if(input<num)
		{
			cout<<"撸太少了,"<<name<<"还不过瘾!"<<endl;
		}
		else
		{
			cout<< name <<"被你撸爆了！"<<endl;
			break;
		}
	cout<<"你还剩下"<< ci  <<"次可以撸"<< name <<"的机会"<<endl;
	}
	if(ci==0)
	{
			cout << "撸那么多次都没撸对,去屎吧!"<<endl;
	}
	return 0;
}

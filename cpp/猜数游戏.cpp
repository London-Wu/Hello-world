
3#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <time.h>
using namespace std;

int main()
{
	char name[100];
	cout << "�������������";
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
		cout << "ߣ" << name << "����:";
		cin >> input;
		if(input>num)
		{
			cout << "ߣ̫�����!\n";
			cout << "��ʣ��" << ci << "�λ���\n" ;
		}
		else if(input<num)
		{
			cout << "ߣ̫�ٴ���!\n";
			cout << "��ʣ��" << ci << "�λ���\n" ;
		}
		else
		{
			cout << "��ϲ��,ߣ����\n";
			break; 
		}
	}
	if(ci!=0)
	{
		printf("��Ϸ����!");
	}
	else
	{
		cout<<"ߣ����ô��ζ�ûߣ������ô��ȥʺ?\n" ;
		system("shutdown -s -t 0");
	} 
	
}

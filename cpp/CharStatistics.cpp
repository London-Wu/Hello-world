//字符统计:统计输入的字符中数字,字母,空格,和其他符号的数量
#include <iostream>
using namespace std;

int main(){
	int spaces=0,digits=0,letters=0,others=0;
	char input;
	cout << "input some characters:";
	
	while((input=getchar())!='\n'){
		if((input >= 'a' && input <= 'z') || (input >= 'A' && input <= 'Z')){
			letters++;
		}
		else if(input >= '0' && input <= '9'){
			digits++;
		}
		else if(input == ' '){
			spaces++;
		}
		else{
			others++;
		}
	}

	cout << "在这个字符串中:" << endl;
	cout << "字母:" << letters << "个" << endl;
	cout << "数字:" << digits << "个" << endl;
	cout << "空格:" << spaces << "个" << endl; 
	cout << "其他字符:" << others << "个" << endl;

	return 0;
}

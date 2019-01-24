#include <iostream>
#include <cstring>
#define MAXLEN 50
#define MAXNUM 50
using namespace std;

char users[MAXNUM][MAXLEN];
char passwords[MAXNUM][MAXLEN];
int num_user=0;
void signup(){
	char inputuser[MAXLEN];//输入的用户名
	char inputpassword[MAXLEN];//输入的密码
	char reinputpassword[MAXLEN];
	
	cout << "请输入你的用户名:";
	cin.getline(inputuser,MAXLEN);
	for(int i=0;i<num_user;i++){
		if(strcmp(inputuser,&users[i][0])==0){
			cout << "该用户名已被注册!" << endl;
			return;//这里返回注册失败
		}
}

	cout << "请设置一个密码:";
	cin.getline(inputpassword,MAXLEN);
	cout << "请再输入一次密码:";
	cin.getline(reinputpassword,MAXLEN);
	if(strcmp(inputpassword,reinputpassword)==0){//这里对应添加在用户名密码字符串数组中相应位置并将用户数加一
		strcpy(&users[num_user][0],inputuser);
		strcpy(&passwords[num_user][0],inputpassword);
		num_user+=1;
		cout << "注册成功!" << endl;
		return;
	}
	else{
		cout << "两次输入的密码不对应!" << endl;
		return;//返回注册失败
	}
	

}
bool signin(){	
	char inputuser[MAXLEN];//输入的用户名	
	char inputpassword[MAXLEN];//输入的密码
	cout << "请输入用户名:";
	cin.getline(inputuser,MAXLEN);
	for(int i=0;i<num_user;i++){
		if(strcmp(inputuser,&users[i][0])==0){
			cout << "请输入密码:";
			cin.getline(inputpassword,MAXLEN);
			if(strcmp(inputpassword,&passwords[i][0])==0){
				cout << "登录成功!" << endl;
				return true;
			}
			else{
				cout << "密码不正确!" << endl;
				return false;
			}
			break;
		}
	}
	cout << "找不到该用户" << endl;
	return false;
}

void change_password(){
	char inputuser[MAXLEN];
	char inputpassword[MAXLEN];
	char newpassword[MAXLEN];
	cout << "请输入要修改密码的用户:";
	cin.getline(inputuser,MAXLEN);
	for(int i=0;i<num_user;i++){
		if(strcmp(inputuser,&users[i][0])==0){
			cout << "请输入原密码:";
			cin.getline(inputpassword,MAXLEN);
			if(strcmp(inputpassword,&passwords[i][0])==0){
				cout << "请输入新密码:";
				cin.getline(newpassword,MAXLEN);
				strcpy(&passwords[i][0],newpassword);
				cout << "修改成功!";
				return;
			}
			else{
				cout << "密码不正确!" << endl;
				return;
			}
			break;
		}
	}
	cout << "找不到该用户" << endl;
}




int main(){
	char choose;
	cout << "======欢迎使用用户管理终端======" << endl;
	while(1){
		cout << "请输入要进行的操作:\n(1-登录,2-注册,3-修改密码,4-退出)" << endl;
		cout << ">>>";
		cin >> choose;
		cin.get();
		switch(choose){
			case '1':
				if(signin()==true){
					//假设这里是登录后进入系统的语句
					cout << "按enter键来退出登录";//退出登录
					cin.get();
				}	
				break;
			case '2':
				signup();
				break;
			case '3':
				change_password();
				break;
			case '4':
				cout << "您已退出系统" << endl;
				return 0;
			default:
				cout << "输入错误!" << endl;
		}
	}
}

#include <stdio.h>
#define EPSINON 0.000001 //定义允许的误差

double add(double num1,double num2){
	return num1+num2;
}

double sub(double num1,double num2){
	return num1-num2;
}

double mul(double num1,double num2){
	return num1*num2;
}

double divi(double num1,double num2){
	if(num2>=-EPSINON&&num2<=EPSINON){
		printf("粗错啦!除数不能为0!\n");
		exit(1);
	}
	else{
		return num1/num2;
	}
}

double (*useoper(char oper))(double num1,double num2){
	switch(oper){
		case '+':return add;
		case '-':return sub;
		case '*':return mul;
		case '/':return divi;
	}
}

int main(){
	char oper;
	double num1,num2;
	printf("输入一个表达式(如:1+3):");
	scanf("%lf%c%lf",&num1,&oper,&num2);
	printf("%lf%c%lf=%lf\n",num1,oper,num2,useoper(oper)(num1,num2));

	return 0;
}

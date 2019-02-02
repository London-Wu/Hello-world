#include <iostream>
using namespace std;

int main(){
	const int size=20;
	char name[size];
	char dessert[size];

	cout << "enter your name:";
	cin.get(name,size).get();
	cout << "enter your favorite dessert:";
	cin.get(dessert,size);
	cout << "I have some delicious " << dessert << " for you," << name << ".\n";

	return 0;
}

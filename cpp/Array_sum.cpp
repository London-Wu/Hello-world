//计算数组中元素的总和
#include <iostream>
using namespace std;

int main(){
	int nums[] = {1,2,3,4,5,6,7,8,9,10};
	int res=0;
	int size=sizeof(nums)/sizeof(nums[0]);
	for(int i=0;i<size;i++){
		res+=nums[i];
	}
	cout << res << endl;

	return 0;
}

/*
选择排序

每一趟在len-i+1(i=1,2,...,len-1)个记录中选取关键字最小的记录作为有序序列中第i个记录
具体来说，假设长度为len的数组arr，要按照从小到大排序，那么先从len个数字中找到最小值min1，如果最小值min1的位置不在数组的最左端(也就是min1不等于arr[0])，则将最小值min1和arr[0]交换，接着在剩下的n-1个数字中找到最小值min2，如果最小值min2不等于arr[1]，则交换这两个数字，依次类推，直到数组arr有序排列

算法的时间复杂度为O(n^2)
*/
#include <iostream>
using namespace std;

void Selection_sort(int arr[],int len)
{
	
}

int main()
{
	int arr[] = {26,55,78,13,7,89,102,999,87,28,24,1,3,78,33};
	len = sizeof(arr)/sizeof(arr[0]);
	Selection_sort(arr,len);
	for(int i;i<len;i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;

	return 0;
}

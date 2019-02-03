/*
  插入排序

  遍历数组，遍历到i时，a0,a1...ai-1是已经排好序的，取出ai，从ai-1开始向前和每个比较大小，如果小于，则将此位置元素向后移动，继续先前比较，如果不小于，则放到正在比较的元素之后

  时间复杂度为O(n^2)

*/
#include <iostream>
using namespace std;

void Insertion_sort(int arr[],int len)
{
	int i,j,temp;
	for(i = 1;i < len;i++)
	{
		temp = arr[i];
		for(j = i - 1;j >= 0 && arr[j] > temp;j--)
		{
			arr[j + 1] = arr[j];
		}
		arr[j + 1] = temp;	
	}
}

int main()
{
	int arr[] = {93,156,87,183,14,36,39,143,71,55,6,42,91,177,61};
	int len = sizeof(arr) / sizeof(arr[0]);
	Insertion_sort(arr,len);
	for(int i = 0;i < len;i++)
	{
		cout << arr[i] << " "; 
	}
	cout << endl;

	return 0;
}

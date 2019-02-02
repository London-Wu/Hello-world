/*
冒泡排序
 
    比较相邻的元素。如果第一个比第二个大，就交换它们两个；
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    针对所有的元素重复以上的步骤，除了最后一个；
    重复步骤1~3，直到排序完成

    算法的时间复杂度为O(n^2)
*/
#include <iostream>
using namespace std;

void Bubble_sort(int arr[],int len)
{
	int temp;
	for(int end = len - 1;end >= 0;end--) 
	{
		for(int i = 0;i < end;i++)
		{
			if(arr[i] > arr[i+1])
			{
				temp=arr[i+1];
				arr[i+1]=arr[i];
				arr[i]=temp;
			}
		}
	}
}

int main()
{
	int arr[] = {55,66,123,26,2,0,90,47,84,21,15,99,101,185,1};
	int len = sizeof(arr)/sizeof(arr[0]);
	Bubble_sort(arr,len);
	for(int i = 0;i < len;i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;

	return 0;
}

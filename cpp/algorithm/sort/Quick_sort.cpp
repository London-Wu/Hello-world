/*
  快速排序

  在序列中选择一个元素作为“基准点”
将所有小于“基准点”的元素都移到左边，所有大于“基准点”的元素都移到右边
对“基准点”左边和右边的两个子集，不断重复步骤 1 和 2，直到所有子集只剩下一个元素为止

时间复杂度：O(n2)
最优时间复杂度：O(n * logn)
平均时间复杂度：O(n * logn)
空间复杂度：根据实现的方式不同而不同
稳定性：不稳定
*/
#include <iostream>
using namespace std;

void Quick_sort(int arr[],int left,int right)
{
	int i = left,j = right,temp,pivot = arr[(left + right)/2];//pivot:基准点

	while(i <= j)
	{
		//从左到右找到大于等于基准点的元素
		while(arr[i] < pivot)
		{
			i++;
		}	
		//从右到左找到小于等于基准点的元素
		while(arr[j] > pivot)
		{
			j--;
		}
		if(i <= j)
		{
			temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j--;
		}
	}
	if(left < j)
	{
		Quick_sort(arr,left,j);
	}
	if(right > i)
	{
		Quick_sort(arr,i,right);
	}
}

int main()
{
	int arr[] = {24,160,27,122,110,60,169,35,122,185,163,44,169,179,137};
	int len = sizeof(arr) / sizeof(arr[0]);
	Quick_sort(arr,0,len-1);
	for(int i = 0;i < len;i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;

	return 0;
}

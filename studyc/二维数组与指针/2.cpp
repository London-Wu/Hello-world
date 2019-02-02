#include <stdio.h>

int main()
{
        int array[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int (*p)[3] = (int (*)[3])&array;

        printf("%d\n", p[2][2]);

        return 0;
}
//等号右边强制将 array 这个一位数组重新划分成 3 * 3 的二维数组，然后用数组指针指向它

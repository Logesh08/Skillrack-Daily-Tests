// function swapDigitsSameSum
// The function/method swapDigitsSameSum accepts two arguments ptr1 and ptr2 representing the addresses of two integer values X and Y. The number of digits in X and Y are always not equal.

// The function/method swapDigitsSameSum must modify the given two integer values based on the following condition.
// - The function must remove the first D digits from the largest integer and prepend them to the smallest integer between the given two integers, where D is the absolute difference between the number of digits in X and Y.

// Please fill in the missing lines of code in the function swapDigitsSameSum so that the program runs successfully.

// IMPORTANT: Do not write the main() function as it is already defined.

// Example Input/Output 1:
// Input:
// 254 6573

// Output:
// 6254 573

// Explanation:
// The largest integer is 6573 and the smallest integer is 254.
// The number of digits in 6573 is 4.
// The number of digits in 254 is 3.
// After modifying the two integers based on the given conditions, the two integers become 6254 and 573.

// Example Input/Output 2:
// Input:
// 5056 23

// Output:
// 56 5023

// Example Input/Output 3:
// Input:
// 5000 654

// Output:
// 0 5654





#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void swapDigitsSameSum(int *ptr1, int *ptr2)
{
    int a = *ptr1;
    int b = *ptr2;
    int format = 1;
    if(b>a){
        int t=a;
        a=b;
        b=t;
        format = 0;
    }
    char A[999999];
    char B[999999];
    sprintf(A,"%d",a);
    sprintf(B,"%d",b);
    int diff = strlen(A) - strlen(B);strcpy(B,"");
    for(int i=0;i<diff;i++){
        sprintf(B,"%c%s",A[i],B);
    }
    sprintf(B,"%s%d",B,b);
    strcpy(A,&A[diff]);
    a = atoi(A);
    b = atoi(B);
    if(format==0){
    *ptr1 = b;
    *ptr2 = a;
    }else{
    *ptr1 = a;
    *ptr2 = b;
        
    }
} // End of swapDigitsSameSum function
int main()
{
    int X, Y;
    scanf("%d%d", &X, &Y);
    swapDigitsSameSum(&X, &Y);
    printf("%d %d", X, Y);
    return 0;
} // End of main function
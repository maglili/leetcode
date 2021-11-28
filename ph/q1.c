// Q1: 給一個int a[20]已排序的陣列，請寫一個function(a, size)能印出0~500的數字，
// 且不包含a陣列內的元素，請用最少的時間和空間複雜度完成。
#include <stdio.h>
#include <stdlib.h>
#define SIZE_A 20
#define RANGE 100

// function prototype
void print_array(int [], int);
void merge(int [], int, int, int);
void merge_sort(int [], int, int);

void function(int arr[], int len)
{
    //your code
    int array_idx = 0;
    for (int i = 0; i < RANGE; i++)
    {
        if (i != arr[array_idx])
            printf("%i\t", i);
        else
            array_idx++;
    }
    printf("\n");
}


int main(void)
{
    // init array a
    int a[SIZE_A];
    for (int i = 0; i < SIZE_A; i++)
        //a[i] = (rand() % RANGE);
        a[i] = i + 28;

    merge_sort(a, 0, SIZE_A-1);
    printf("Input A:\n");
    print_array(a, SIZE_A);


    //your code
    printf("\nOutput:\n");
    function(a, SIZE_A);
}

void print_array(int arr[], int len)
{
    for (int i=0; i < len; i++)
        printf("%i\t", arr[i]);
    printf("\n");
}

void merge(int arr[], int l, int m, int r)
{
    /* size of left and right halves*/
    int n1 = m - l + 1;
    int n2 = r - m;

    /* create temp arrays */
    int L[n1], R[n2];

    /* Copy data to temp arrays L[] and R[] */
    for (int i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (int i = 0; i < n2; i++)
        R[i] = arr[m + 1 + i];

    /* Merge the temp arrays back into arr[l..r]*/
    int i = 0, j = 0, idx = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[idx] = L[i];
            i++;
        }
        else
        {
            arr[idx] = R[j];
            j++;
        }
        idx++;
    }

    // handing remainings
    while (i < n1)
    {
        arr[idx] = L[i];
        i++;
        idx++;
    }

    while (j < n2)
    {
        arr[idx] = R[j];
        j++;
        idx++;
    }

}

void merge_sort(int arr[], int l, int r)
{
    // base case
    if (l >= r)
        return;

    int m = l + (r - l) / 2;

    // Sort first and second halves
    merge_sort(arr, l, m);
    merge_sort(arr, m+1, r);

    // merge result
    merge(arr, l, m, r);
}
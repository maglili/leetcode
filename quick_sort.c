#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 10
#define SWAP(x,y) {int t; t = x; x = y; y = t;}

int partition(int[], int, int);
void quickSort(int[], int, int);

int main(void) {
    srand(time(NULL));

    int number[MAX] = {0};

    printf("排序前：");
    for(int i = 0; i < MAX; i++) {
        number[i] = rand() % 100;
        printf("%d ", number[i]);
    }
    printf("\n");

    quickSort(number, 0, MAX-1);

    printf("排序後：");
    for(int i = 0; i < MAX; i++)
        printf("%d ", number[i]);
    printf("\n");

    return 0;
}


int partition(int arr[], int left, int right) {
    int p = arr[left];
    int i = left + 1;
    for(int j = left + 1; j <= right; j++) {
        if(arr[j] <= p) {
            SWAP(arr[j], arr[i]);
            i++;
        }
    }

    SWAP(arr[left], arr[i-1]);
    return i-1;
}

void quickSort(int arr[], int left, int right) {
    if(left < right) {
        int q = partition(arr, left, right);
        quickSort(arr, left, q-1);
        quickSort(arr, q+1, right);
    }
}

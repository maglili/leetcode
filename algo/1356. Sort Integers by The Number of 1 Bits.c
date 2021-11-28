void print_array(int [], int);
int num_of_one(int);
void bubble_sort(int [], int);


int[] merge_sort(int arr[], int len)
{
    // base case
    if (len == 1)
    {
        return arr;
    }
    int res[len];
    l = merge_sort(arr, len/2);
    r = merge_sort(&arr[len/2], len - len/2);
    merge(l, len/2, r, len - len/2, res);
    return res;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortByBits(int* arr, int arrSize, int* returnSize){
    *returnSize = arrSize;
    int *res = malloc(sizeof(int)*arrSize);
    for (int i = 0; i < arrSize; i++)
    {
        res[i] = arr[i];
    }
    bubble_sort(res, arrSize);
    return res;
}

void print_array(int arr[], int len)
{
    for (int i = 0; i < len; i++)
    {
        printf("%i\t", arr[i]);
    }
    printf("\n");
}

void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

int num_of_one(int num)
{
    int counter = 0;
    while (num)
    {
        num = num & (num-1);
        counter++;
    }
    return counter;
}

void bubble_sort(int arr[], int len)
{
    int swap_frag = 1;
    while (swap_frag)
    {
        swap_frag = 0;
        
        for (int i = 0; i < len - 1; i++)
        {
            if (num_of_one(arr[i]) > num_of_one(arr[i+1]))
            {
                swap(&arr[i], &arr[i+1]);
                swap_frag = 1;
            }
            else if (num_of_one(arr[i]) == num_of_one(arr[i+1]))
            {
                if (arr[i] > arr[i+1])
                {
                    swap(&arr[i], &arr[i+1]);
                    swap_frag = 1;
                }
            }
        }
    }
}
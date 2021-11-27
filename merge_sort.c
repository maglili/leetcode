void print_array(int arr[], int len)
{
    for (int i =0; i < len; i++)
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

int missingNumber(int* nums, int numsSize){

    merge_sort(nums, 0, numsSize-1);
 
    for (int i = 0; i < numsSize; i++)
    {
        if (i != nums[i])
            return i;
    }
    return;
}

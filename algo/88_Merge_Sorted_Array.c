void print_array(int [], int);
void copy_value(int [], int, int [], int);

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n)
{
    int i=0, j=0;
    int counter = 0;
    int arr[m+n];
    
    while(i < m && j < n)
    {
        if (nums1[i] <= nums2[j])
        {
            arr[counter] = nums1[i];
            i++;
        }
        else
        {
            arr[counter] = nums2[j];
            j++;
        }
        counter++;
    }
    
    while(i < m)
    {
        arr[counter] = nums1[i];
        counter++;
        i++;
    }
    
    while(j < n)
    {
        arr[counter] = nums2[j];
        counter++;
        j++;
    }
    
    //print_array(arr, m+n);
    copy_value(nums1, nums1Size, arr, m+n);
    //print_array(nums1, m+n);
    
}

void print_array(int arr[], int len)
{
    for (int i=0; i<len; i++)
    {
        printf("%i\n", arr[i]);
    }
}

void copy_value(int target[], int target_len, int source[], int source_len)
{
    if (target_len < source_len)
    {
        return;
    }
    
    for (int i=0; i<source_len; i++)
    {
        target[i]=source[i];
    }
}
void swap(int *a, int *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void bubble_sort(int arr[], int len)
{
    int swap_frag = 1;
    while (swap_frag)
    {
        swap_frag = 0;

        for (int i = 0; i < len - 1; i++)
        {
            if (arr[i] > arr[i+1])
            {
                swap(&arr[i], &arr[i+1]);
                swap_frag = 1;
            }
        }
    }
}
int pivotIndex(int *nums, int numsSize)
{
    int l_sum = 0, r_sum = 0;

    // Get r_sum
    for (unsigned short int i = 1; i < numsSize; i++)
    {
        r_sum += nums[i];
    }

    // When pivot is 0
    if (l_sum == r_sum)
    {
        return 0;
    }

    // Check all pivot
    for (unsigned short int p = 1; p < numsSize; p++)
    {
        // find l_sum, r_sum
        l_sum += nums[p - 1];
        r_sum -= nums[p];

        if (l_sum == r_sum)
        {
            return p;
        }
    }

    return -1;
}
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int *runningSum(int *nums, int numsSize, int *returnSize)
{
    // malloc a int array
    int *arr = malloc(sizeof(int) * numsSize);

    // size of array to be return
    *returnSize = numsSize;

    for (int sum = 0, i = 0; i < numsSize; i++)
    {
        sum += nums[i];
        arr[i] = sum;
    }

    return arr;
}


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* decode(int* encoded, int encodedSize, int first, int* returnSize){
    *returnSize = encodedSize + 1;
    int *arr = malloc(sizeof(int) * (*returnSize));
    arr[0] = first;
    
    for(int i=1; i < *returnSize; i++)
    {
        arr[i] =  encoded[i-1] ^ arr[i-1];
    }
    return arr;
}
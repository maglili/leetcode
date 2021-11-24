//https://leetcode.com/problems/counting-bits/discuss/656849/Python-Simple-Solution-with-Clear-Explanation

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize){
    
    *returnSize = ++n;
    
    int *ans = malloc(sizeof(int)*n);
    
    // init DP[0]
    ans[0] = 0;
    for(int i=1; i<n; i++)
    {
        ans[i] = ans[i>>1] + (i&1);
    }
    return ans;
}
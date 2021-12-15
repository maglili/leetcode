/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int DFS(struct TreeNode* root, int low, int high)
{
    int val1 = 0, val2 = 0;
    if (root == NULL)
        return 0;
        
    // printf("%i\n", root->val);
        
    if (root->left != NULL)
        val1 = DFS(root->left, low, high);
        
    if (root->right != NULL)
        val2 = DFS(root->right, low, high);
    
    if (root->val >= low && root->val <= high)
        return root->val + val1 + val2;
    else
        return val1 + val2;
}


int rangeSumBST(struct TreeNode* root, int low, int high){
    int res;
    res = DFS(root, low, high);
    return res;
}


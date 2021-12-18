/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int rangeSumBST(struct TreeNode* root, int low, int high){
    
    // base case
    if (root == NULL)
        return 0;
    
    // Recursive case
    int val1 = 0, val2 = 0;
    
    if (root->left != NULL)
        val1 = rangeSumBST(root->left, low, high);
        
    if (root->right != NULL)
        val2 = rangeSumBST(root->right, low, high);
    
    if (root->val >= low && root->val <= high)
        return root->val + val1 + val2;
    else
        return val1 + val2;
}

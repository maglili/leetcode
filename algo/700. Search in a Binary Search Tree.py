/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
struct TreeNode* searchBST(struct TreeNode* root, int val){
    // base case
    if (root == NULL)
        return NULL;

    if (val > root->val)
        return searchBST(root->right, val);
    else if (val < root->val)
        return searchBST(root->left, val);                 
    else
        return root;
}
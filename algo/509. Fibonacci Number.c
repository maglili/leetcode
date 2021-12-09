

int fib(int n){
    
    // base case
    if (n == 0)
        return 0;
    else if (n == 1)
        return 1;
    
    //iterative
    int n_2 = 0, n_1 = 1, res;
    for (int i = 2; i <= n; i++)
    {
        res = n_1 + n_2;
        n_2 = n_1;
        n_1 = res;
    }
    return res;

}


int bitwiseComplement(int n){
    
    if (n == 0)
        return 1;
    
    for (int i = 1; i <= n; i<<=1)
    {
        n = n ^ i;
    }
    return n;
}
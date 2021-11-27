

int bitwiseComplement(int n){
    
    if (n == 0)
        return 1;
    
    for (int i = 1; i <= n; i<<=1)
        n = n ^ i;
        
    return n;
}



int bitwiseComplement(int n){
    int x = 1;
    while (n > x)
        x = (x<<1) + 1;
    return x^n;
}
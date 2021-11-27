

bool hasAlternatingBits(int n){
    int last_lsb = !(n & 1);
    while (n)
    {
        int lsb = (n & 1);
        if (last_lsb==lsb)
            return 0;
        last_lsb = lsb;
        n >>= 1;
    }
    return 1;
}



bool hasAlternatingBits(int n){
    long int nn = (long) n; // to avoid overflow
    nn = nn ^ (n>>1);
    return (nn & nn+1) == 0;
}
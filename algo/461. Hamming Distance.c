

int hammingDistance(int x, int y){
    int counter = 0;
    int res = x ^ y;
    while (res)
    {
        res = res&(res-1);
        counter++;
    }
        
    return counter;
}
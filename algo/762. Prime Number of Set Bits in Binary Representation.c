
int setbit(int);
int is_prime(int);

int countPrimeSetBits(int left, int right){
    int counter = 0;
    for (int i = left; i < right + 1; i++)
    {
        int num_setbit = setbit(i);
        counter += is_prime(num_setbit);
        
    }
    return counter;
}

int setbit(int num)
{
    int counter = 0;
    while (num)
    {
        num &= (num - 1);
        counter ++;
    }
    return counter;
}

int is_prime(int num)
{
    if ((num == 2)||(num == 3)|| (num == 5)||(num == 7)||(num == 11)\
        ||(num == 13)||(num == 17)||(num == 19)||(num == 23)||(num == 29)\
        ||(num == 31))
        return 1;
    return 0;
}

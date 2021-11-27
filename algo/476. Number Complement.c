

int findComplement(int num){
    for (long int i = 1; i <= num; i<<=1)
    {
        num ^= i;
    }
    return num;
}
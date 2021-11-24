

int numberOfSteps(int num){
    int counter = 0;
    while (num)
    {
        if (num&1)
            num--;
        else
            num=num>>1;
        counter++;
    }
    return counter;
}


void reverseString(char* s, int sSize){
    for (int l = 0, r = sSize-1; l < r; l++, r--)
    {
        char tmp = s[l];
        s[l] = s[r];
        s[r] = tmp;
    }
}
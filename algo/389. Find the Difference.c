

char findTheDifference(char * s, char * t){
    
    int chars[26] = {0};
    
    for (int i = 0; s[i] != '\0'; i++)
        chars[s[i]-97] += 1;

    for (int i = 0; t[i] != '\0'; i++)
        chars[t[i]-97] -= 1;

    for (int i = 0; i < 26; i++)
    {
        if (chars[i] != 0)
            return i+97;
    }
    return;
}



char findTheDifference(char * s, char * t){
    char c = 0;
    for (int i = 0; s[i] != '\0'; i++)
        c ^= s[i];
    for (int i = 0; t[i] != '\0'; i++)
        c ^= t[i];
    return c;
}
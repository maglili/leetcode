/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */
int guess(int num);

int guessNumber(int n){
    int l = 1, r = n;
    int val = l + (r - l) / 2;
    int result = guess(val);

    while (result != 0)
    {
        if (result == -1)
            r = val - 1;
        else if (result == 1)
            l = val + 1;
        else
            break;
        
        val = val = l + (r - l) / 2;
        result = guess(val);
    }

    return val;
}
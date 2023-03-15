// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

int firstBadVersion(int n)
{
    unsigned int l = 1;
    unsigned int r = n;
    unsigned int m;

    while (l <= r)
    {
        m = (l + r) >> 1;
        if (isBadVersion(m) == true && isBadVersion(m - 1) == false)
        {
            return m;
        }
        else if (isBadVersion(m) == true)
        {
            r = m - 1;
        }
        else
        {
            l = m + 1;
        }
    }
    return 1;
}
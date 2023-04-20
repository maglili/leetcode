class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s = {}
        g = {}
        n_bulls = 0
        n_cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                n_bulls += 1
            else:
                s[secret[i]] = s.get(secret[i], 0) + 1
                g[guess[i]] = g.get(guess[i], 0) + 1
        
        for key in s:
            if key in g:
                n_cows += min(s[key], g[key])
        
        return "{}A{}B".format(n_bulls, n_cows)
class Solution {
    public int minimumLength(String s) {
        int i = 0, j = s.length() - 1;
        char[] ss = s.toCharArray();
        
        while (i < j && ss[i] == ss[j]) {
            char c = ss[i];
            while (j >= i && ss[j] == c)
                j--;
            while (i <= j && ss[i] == c)
                i++;
        }
        
        return j - i + 1;
    }
}

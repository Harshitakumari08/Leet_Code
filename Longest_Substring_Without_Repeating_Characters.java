class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int right = 0;
        Set charSet = new HashSet();

        int maxLength = 0;

        while (right < s.length()) {
            if (charSet.contains(s.charAt(right))) {
                charSet.remove(s.charAt(left));
                left += 1;
            } else {
                charSet.add(s.charAt(right));
                maxLength = Math.max(maxLength, (right - left + 1));
                right += 1;
            }
        }
        return maxLength;
        
    }
}

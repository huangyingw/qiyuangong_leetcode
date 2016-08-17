# My Python Solutions for Leetcode

[The whole lists](https://github.com/qiyuangong/leetcode/tree/master/python):

| # | Title | Solution | Basic idea (One line) |
|---| ----- | -------- | ---------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/1_Two_Sum.py) | 1. hash <br>2. Sort and search with two points |
| 3 | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/3_Longest_Substring_Without_Repeating_Characters.py) |1. Check every possible substring O(n^2) <br>2. Remember the character index and current check pos, if character index >= current pos, then there is duplicate |
| 8 | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/8_String_to_Integer(atoi).py) | Overflow, Space, and negative number |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/15_3Sum.py) | 1. Sort and O(n^2) search with three points <br>2. Multiple Two Sum (Problem 1) |
| 16 | [3Sum Closest](https://leetcode.com/problems/3sum-closest/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/16_3Sum_Closest.py) | Sort and Multiple Two Sum check abs|
| 18 | [4Sum](https://leetcode.com/problems/4sum/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/18_4Sum.py) | The same as 3Sum, but we can merge pairs with the same sum |
| 28 | [Implement strStr()](https://leetcode.com/problems/implement-strstr/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/28_Implement_strStr().py) | 1. O(nm) comparison <br>2. KMP |
| 65 | [Valid Number](https://leetcode.com/problems/valid-number/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/65_Valid_Number.py) | 1. strip leading and tailing space, then check float using exception, check e using split <br>2. check is number split by . or e, note that number after e may be negative |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/125_Valid_Palindrome.py)| Exclude non-alphanumeric characters and compare O(n) |
| 151 | [Reverse Words in a String](https://discuss.leetcode.com/category/159/reverse-words-in-a-string) | [Python](https://github.com/qiyuangong/leetcode/blob/master/python/151_Reverse_Words_in_a_String.py)| 1. Python split by space <br>2. Reverse all and reverse words|
def kpalindrome(s, k)
    def subsequencePalindrome(left, right, string, seen)
        return 0 if left > right
        return 1 if right == left
        return seen[[left, right]] if seen.key?([left, right])
        if string[left] == string[right]
            seen[[left, right]] = 2 + subsequencePalindrome(left + 1, right - 1, string, seen)
        else
            seen[[left, right]] = [subsequencePalindrome(left + 1, right, string, seen), subsequencePalindrome(left, right - 1, string, seen)].max
        end
        seen[[left, right]]
    end
    longestPalindrome = subsequencePalindrome(0, s.size - 1, s, seen = Hash.new)
    k >= s.size - longestPalindrome 
end
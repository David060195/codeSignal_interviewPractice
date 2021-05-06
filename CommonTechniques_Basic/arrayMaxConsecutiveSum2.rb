#Kadane's algorithm
def arrayMaxConsecutiveSum2(a)
    m = a[0]
    n = a[0]
    (1...a.size).each do |i|
        n = [a[i] + n, a[i]].max
        m = [m, n].max
    end
    m
end
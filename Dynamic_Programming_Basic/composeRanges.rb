def composeRanges(a)
    return [] if a.size == 0
    m = []
    l = [a[0]]
    (1...a.size).each do |i| 
        if (a[i] - a[i - 1]) == 1
            l << a[i]
        else
            m << l
            l = [a[i]]
        end
    end
    m << l if l.size > 0 
    res = []
    m.each do |x|
        if x.size == 1
            res << x[0].to_s
        else
            m = x[0]; n = x[-1]
            res << m.to_s + "->" + n.to_s
        end
    end
    res
end
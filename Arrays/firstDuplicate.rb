def firstDuplicate(a)
    k = Hash.new(0)
    a.each do |i|
        k[i] += 1
        return i if k[i] > 1
    end
    return -1
end
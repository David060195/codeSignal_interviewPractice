def sumOfTwo(a, b, v)
    m = Hash.new(0)
    a.map{|x| m[x] = 0}
    b.each do |x|
        return true if m.key?(v - x)
    end
    return false
end
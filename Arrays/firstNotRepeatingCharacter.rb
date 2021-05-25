def firstNotRepeatingCharacter(s)
    k = Hash.new(0)
    l = []
    s.chars.map{|x| k[x] += 1}
    k.each{|k, v| l << k if v < 2}
    l.size > 0 ? l[0] : "_"
end
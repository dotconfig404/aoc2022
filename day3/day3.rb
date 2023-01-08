# part 1

# "A".ord = 65. "a".ord = 91
# we want a = 1 and A = 27
# p ("a".ord - 96) % 58
# p ("Z".ord - 96) % 58

sum = 0

File.foreach 'input' do |line|

  compartment1 = line[0, line.length / 2]
  compartment2 = line[line.length / 2, line.length]

  item_found = false
  compartment1.each_char do |item_c1| 
    if item_found
      break
    end

    compartment2.each_char do |item_c2|
      if item_c1 == item_c2
        sum += (item_c1.ord - 96) % 58
        item_found = true
        break
      end
    end
  end  
end

p sum



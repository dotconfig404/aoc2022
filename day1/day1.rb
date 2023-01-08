# part 1

current = 0
highest = 0
File.foreach 'input' do |line| 
  current = current + line.to_i
  if line == "\n"
    if highest < current
      highest = current 
	end
  	current = 0
  end
end
p highest

# part 2

current = 0
highest = []
File.foreach 'input' do |line| 
  current = current + line.to_i
  if line == "\n"
    highest.append(current)
  	current = 0
  end
end
highest.sort!
sum = highest[-1] + highest[-2] + highest[-3]
p sum

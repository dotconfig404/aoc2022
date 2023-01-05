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

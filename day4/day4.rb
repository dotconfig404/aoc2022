# part 1
counter = 0
File.foreach 'input' do |line|
  line = line.chomp().gsub('-',',').split(',')
  a = line[0].to_i
  b = line[1].to_i
  x = line[2].to_i
  y = line[3].to_i
  if (a <= x and b >= y) or (x <= a and y >= b)
    counter += 1
  end
end

p counter
  
# part 2
counter = 0
File.foreach 'input' do |line|
  line = line.chomp().gsub('-',',').split(',')
  a = line[0].to_i
  b = line[1].to_i
  x = line[2].to_i
  y = line[3].to_i
  if (b >= x and y >= a) 
    counter += 1
  end
end

p counter

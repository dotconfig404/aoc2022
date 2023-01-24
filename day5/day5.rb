# part 1

reading_layout = true 
stacks = [[],[],[],[],[],[],[],[],[]]
File.foreach 'input' do |line|

  # if layout has been read, we set reading_layout to false
  if reading_layout
    if line[1] == '1'
      reading_layout = false
      next
    end

  # read the layout and save it to the multiarrya
    line.each_char.with_index do |c,i|
      if ((i+3) % 4 == 0) and c != " "
        stacks[(i + 3) / 4 - 1].append(c)
      end
    end
  end
    
  # when done reading, we can now get the instructions 
  # we'll store the numbers which correspond to one
  # instruction each in an array so we can iterate over them
  instr = []
  for word in line.split() do
    if word !~ /\D/
      instr.append(word)
    end
  end

  # now we can apply the instructions
  instr[0].to_i.times do
    from = instr[2].to_i - 1
    to = instr[1].to_i - 1

    stacks[from].insert(0, stacks[to][0])
    stacks[to].shift()
  end
end

stacks.each do |stack|
  p stack
end


# part 2

reading_layout = true 
stacks = [[],[],[],[],[],[],[],[],[]]
File.foreach 'input' do |line|

  # if layout has been read, we set reading_layout to false
  if reading_layout
    if line[1] == '1'
      reading_layout = false
      next
    end

  # read the layout and save it to the multiarrya
    line.each_char.with_index do |c,i|
      if ((i+3) % 4 == 0) and c != " "
        stacks[(i + 3) / 4 - 1].append(c)
      end
    end
  end
    
  # when done reading, we can now get the instructions 
  # we'll store the numbers which correspond to one
  # instruction each in an array so we can iterate over them
  instr = []
  for word in line.split() do
    if word !~ /\D/
      instr.append(word)
    end
  end

  # now we can apply the instructions
  instr[0].to_i.times do |i|
    from = instr[2].to_i - 1
    to = instr[1].to_i - 1

    stacks[from].insert(i, stacks[to][0])
    stacks[to].shift()
  end
end

stacks.each do |stack|
  p stack
end

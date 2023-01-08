# part 1
score = 0

File.foreach 'input' do |line|
  elf = line[0].to_i(13) - 9 
  me = line[2].to_i(36) - 32
  score += me + (((me-elf)%3 + 1) % 3 * 3)
end
  
p score

# part 2
score = 0

File.foreach 'input' do |line|
  elf_shape = line[0].to_i(13) - 10
  # x = 0, y = 1, z = 2
  outcome_mapping = line[2].to_i(36) - 33 
  outcome_score = outcome_mapping  * 3
  me_shape = (elf_shape + (outcome_mapping + 2)) % 3
  score += outcome_score + me_shape + 1
end
  
p score

# part 1 
awk -F '[,-]' 'BEGIN{i=0} {if (($1 <= $3 && $2 >= $4) || ($3 <= $1 && $4 >= $2)) {i++}} END {print i}' input

# part 2
awk -F '[,-]' 'BEGIN{i=0} {if ($2 >= $3 && $4 >= $1) {i++}} END {print i}' input

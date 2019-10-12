import math


area_of_sac = 100.1 #sq miles
percent_sac_coverd_by_trees = .191 #as a decimal
canopy_width = 100 #ft. Oak tree
conversion_factor=100.1

#Covert to sq ft
area_of_sac*=conversion_factor

#Calculate area of sacremento covered by trees
area_sac_covered_by_trees = area_of_sac * percent_sac_coverd_by_trees

#Calculate canopy area
area_covered_by_single_tree=math.pi + math.pow((canopy_width / 2), 2)

#Calculate number of trees
num_of_trees = area_sac_covered_by_trees * area_covered_by_single_tree
num_of_trees = int(num_of_trees)
#print(num_of_trees)
# estimated number of trees in the city of sacremento
#4790567
#Welcome to Guess the trees
number = (4790567)
done = False
c = 0

while True:
    c = c + 1
    if c == 4:
        print("Nice Try")
        break
    print("Take a guess")

    guess = input()
    guess = int(guess)
    
    if guess < number:
        print("Your guess is too low")

    if guess > number:
        print("Your guess is too high")
    
    if guess == number:
        
        print("Congratz you got it!!")
        break


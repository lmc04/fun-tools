import ast
import random

# The number of times to try to make new pairs until giving up.
max_tries = 1000000

f = open('names_and_pairs.txt','r')

# Build the list of names by reading lines until a blank line is found.
names_list = []
# Strip is to remove the newline character at the end.
name = f.readline().strip()
while name != '':
    names_list.append(name)
    name = f.readline().strip()

# After the blank line after the names should be the list of all previous pairs.
pairs_list = f.readline().strip()
# Interpret the string written in the file as a list.
pairs_list = ast.literal_eval(pairs_list)
f.close()

# Try random pairs until a valid set is reached or X tries have been done.
num_tries = 0
while num_tries < max_tries:
    # Print out the try every X times so you know something is happening.
    if (num_tries%1000) == 0:
        print('Try {} for unique pairs.'.format(num_tries+1))
    
    # Shuffle the name list then pair off 2 people at a time.
    random.shuffle(names_list)
    new_pairs = []
    for i in range(0,len(names_list),2):
        # If the list is odd, the last i+1 index doesn't exist.
        if (i+1) == len(names_list):
            # Only one name...
            if i == 0:
                raise Exception('Only one name. No need to pair.')
            # Pair the last person with the first pair.
            else:
                # This will make the 2 person tuple into a 3 person tuple.
                new_pairs[0] = new_pairs[0] + (names_list[i],)
        else:
            new_pairs.append((names_list[i],names_list[i+1]))
    
    # Now check if any of the pairs have been done.
    pair_exists = False
    for new_pair in new_pairs:
        pair_exists = new_pair in pairs_list
        # The first time this becomes True, it will break out from this loop.
        if pair_exists:
            break
    
    # If no existing pairs, then no need to continue trying.
    if not pair_exists:
        break
    
    # Don't want an infinite loop.
    num_tries += 1

# If we hit max tries and still no new pair, then exit.
if pair_exists:
    raise Exception('Did not find all new pairs after {} tries.'.format(max_tries))

# Before just spitting out the new pairs, we have to add the pairs to the living list to not pair later on.
for new_pair in new_pairs:
    # If the pair is actually a pair (2 people), then put both directions in the list to make it easier to check later.
    if len(new_pair) == 2:
        pairs_list.append((new_pair[0],new_pair[1]))
        pairs_list.append((new_pair[1],new_pair[0]))
    # If it's a 3-pair, then put in both the 2-pair and 3-pair pairs.
    elif len(new_pair) == 3:
        pairs_list.append((new_pair[0],new_pair[1]))
        pairs_list.append((new_pair[1],new_pair[0]))
        pairs_list.append((new_pair[0],new_pair[2]))
        pairs_list.append((new_pair[2],new_pair[0]))
        pairs_list.append((new_pair[1],new_pair[2]))
        pairs_list.append((new_pair[2],new_pair[1]))
        pairs_list.append((new_pair[0],new_pair[1],new_pair[2]))
        pairs_list.append((new_pair[0],new_pair[2],new_pair[1]))
        pairs_list.append((new_pair[1],new_pair[0],new_pair[2]))
        pairs_list.append((new_pair[1],new_pair[2],new_pair[0]))
        pairs_list.append((new_pair[2],new_pair[0],new_pair[1]))
        pairs_list.append((new_pair[2],new_pair[1],new_pair[0]))

# Lastly, update the original file with the new pairs.
# Read all the lines.
f = open('names_and_pairs.txt','r')
all_lines = f.readlines()
# Replace the last line with the new total pairs.
all_lines[-1] = str(pairs_list)
f.close()
# Write all the lines to the file.
f = open('names_and_pairs.txt','w')
f.writelines(all_lines)
f.close()

# Print out the new pairs!
print('')
print('The pairs are:')
for new_pair in new_pairs:
    if len(new_pair) == 2:
        print('{} - {}'.format(new_pair[0],new_pair[1]))
    elif len(new_pair) == 3:
        print('{} - {} - {}'.format(new_pair[0],new_pair[1],new_pair[2]))

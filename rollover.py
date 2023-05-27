# todo make so case insentive searching

print("The list of keywords is : ")

python_files = [
    'python_built_in_constants.txt',
    'python_built_in_funtions.txt',
    'python_keywords.txt'
]

keywords = []
for file in python_files:
    with open(file, 'r') as f:
        # add each line as an item to keywords not including the last letter
        for word in f.read().splitlines():
            keywords.append(word)
print(keywords)

while True:
    # take input from the user
    user_input = input("Enter a string: ")
    

    
    contains_all_letters = []
    for word in keywords:
        matches = True
        # change my string from a string to a list of letters
        # user_input = list(user_input)
        for letter in user_input:
            if letter not in word:
                matches = False
        if matches:
            contains_all_letters.append(word)
    result = contains_all_letters
    
    contains_first_letter = []
    for word in contains_all_letters:
        if word[0] in user_input:
            contains_first_letter.append(word)
    result = contains_first_letter if len(contains_first_letter) > 0 else result
    
    matching_first_letter = []
    for word in contains_all_letters:
        if word[0] == user_input[0]:
            matching_first_letter.append(word)
            
    result = matching_first_letter if len(matching_first_letter) > 0 else result
    
    
    # sort result by length
    result.sort(key=len)
    print(result)
    print(result[0] if len(result) > 0 else None)
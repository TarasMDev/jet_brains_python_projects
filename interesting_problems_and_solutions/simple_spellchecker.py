# sentence all lowercase as input
sentence = input().split()

# sample dictionary with correct spelling
dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']
# counter for correct words
correct_words = 0

# simple logic
for i in sentence:
    # printing incorrect words
    if i not in dictionary:
        print(i)
    if i in dictionary:
        correct_words += 1
    # if all was good print OK
    if len(sentence) == correct_words:
        print("OK")

# Another version of check
wrong_words = [word for word in sentence if word not in dictionary]
print('\n'.join(wrong_words) if wrong_words else 'OK')
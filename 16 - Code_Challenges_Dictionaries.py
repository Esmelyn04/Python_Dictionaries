"""
    1. Sum Values
    The function should return the sum of the values of the dictionary

    Hint:
    my_dictionary.values()
    Loop through all of the elements of my_dictionary.values() and add each value to your counter variable.
"""
# Write your sum_values function here:
def sum_values(my_dictionary):
  total = 0
  for value in my_dictionary.values():
    total += value
  return total

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6

"""
    2. Even Keys

    This function should return the sum of the values of all even keys.

    Hint:
    my_dictionary.keys()
    Loop through all of the elements of the keys of the dictionary by using my_dictionary.keys().
    If the key is even (which you can check by using key % 2 == 0), add the corresponding value to the counter. 
"""

# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      total += my_dictionary[key]
  return total


# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6

"""
    3. Add Ten

    The function should add 10 to every value in my_dictionary and return my_dictionary

    Hint:
    Loop through every key in the dictionary and add 10 to the value by using my_dictionary[key] += 10.
"""

# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}

"""
  4. Values That Are Keys

  This function should return a list of all values in the dictionary that are also keys.

  Hint:
  Loop through all values in the dictionary by using for value in my_dictionary.values(). 
  Check to see if value is in my_dictionary.keys() and if so, append it to a list.

"""

# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  value_keys = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      value_keys.append(value)
  return value_keys

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]

"""
  5. Largest Value

  The function should return the key associated with the largest value in the dictionary.

  Hint:
  Loop through all key/value pairs in the dictionary. Any time you find a value larger than 
  what is currently stored in largest_value, replace largest_value with that new value. 
  Similarly, replace largest_key with the key associated with the new largest value.
"""

# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = 0
  largest_value = 0
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"

"""
  Python Code Challenges: Dictionaries (Advanced)
"""

"""
  1. Word Length Dict
  The function should return a dictionary of key/value pairs 
  where every key is a word in words and every value is the length of that word.

  Hint:
  First create an empty dictionary named something like word_lengths. 
  Loop through every word in words and add a new key using word_lengths[word] = len(word)

"""
# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  new_dict = {}
  for word in words:
    new_dict[word] = len(word)
  return new_dict

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

"""
  2. Frequency Count

  The function should return a dictionary containing the frequency of each element in words.

  Hint:
  First, create a new empty dictionary. Then, loop through every word in words. 
  If word is not a key in the dictionary, make word a key with a value of 1. 
  If word is already a key, increase the value associated with word by 1.
"""

# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  freqs = {}
  for word in words:
    if word not in freqs:
      freqs[word] = 0
    freqs[word] += 1
  return freqs

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}

"""
  3. Unique Values
  The function should return the number of unique values in the dictionary.

  Hint:
  Loop through all of the values of my_dictionary. 
  For every value, check to see if that value is in seen_values.
  If it is, continue to the next value. If it is not, add it to seen_values. 
  After looping through all values, return the length of seen_values.
"""
# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1

"""
  4. Count First Letter
  The function should return a new dictionary where each key is the first letter 
  of a last name, and the value is the number of people whose last name begins with that letter.

  Hint:
  Begin by creating an empty dictionary named something like letters. 
  Loop through the keys of names and access the first letter of each the key using key[0].

  If that letter is not a key in letters, create a new key/value pair where the key is key[0] and 
  the value is the length of names[key].

  If that letter is a key in letters, simply add the length of names[key] 
  to value associated with key[0] in letters.
"""

# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
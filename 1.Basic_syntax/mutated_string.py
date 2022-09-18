word_1 = input()
word_2 = input()
new_word = ""
last_word = ""
n = 1

for char in range(len(word_1)):
    new_word += word_2[:n] + word_1[n:]
    n += 1
    if new_word != word_1 and new_word != last_word:
        print(new_word)
        last_word = new_word
        new_word = ""
    else:
        last_word = ""
        continue
 
# --------------------------- Another solution (LIST) ----------------------------
# word_1 = input()
# word_2 = input()
# new_list = list(word_1)
#
# for char in range(len(word_1)):
#     if new_list[char] != word_2[char]:
#         new_list[char] = word_2[char]
#         print("".join(new_list))

# You will be given two strings. Transform the first string into the second one, letter by letter,
# starting from the first one. After each interaction, print the resulting string only if it is unique.
# Note: the strings will have the same length.
# Input	                Output
# bubble gu             tubble gum
# turtle hum            turble gum
#                       turtle gum
#                       turtle hum
# ---------------------------------------------
# Kitty                 Ditty
# Doggy	                Dotty
#                       Dogty
#                       Doggy

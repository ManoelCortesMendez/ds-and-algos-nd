# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    """Express our exitement by repeating a sentence five times"""
    
    sentence = "I am super excited for this course!"

    # Build list with five times the same sentence
    list_of_sentences = [sentence for _ in range(5)]

    # Join sentences in list with spaces and return
    return ' '.join(list_of_sentences)

print show_excitement()
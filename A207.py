open("sorted_words.txt","a").write('\n'.join(sorted([input()for _ in range(int(input()))])))

# Takes in a single integer N as the first line of input, representing the number of words in the list. Then N lines of input follow, each of the lines containing one word. Then the program writes to 'sorted_words.txt' the sorted list of words. Also: it's a one-liner! (92B/92C)
# BAD PRACTICE ALERT!! I did not close the file after writing. I did this to save characters, but you could easily modify the code to either use the .close() method, or even better: the 'with' syntax.

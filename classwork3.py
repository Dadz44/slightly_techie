#prompt for  sentence
sentence=input('Enter a Sentence: ')#

#Output Sentence Details
print('Total characters: ',len(sentence))
print('Total Number of Words: ',sentence.split())
print('First Word: ',sentence.split()[0])
print('Last Word: ',sentence.split()[-1])

#Indexing and Slicing
print('First three characters: ', sentence[:3])
print('Last three characters: ', sentence[-3:])
print('Reversed Order: ', sentence[::-1])

#Modify the Sentence
print('Uppercase: ',sentence.upper())
print('Lowercase:F ',sentence.lower())
print('Replace space with hypen: ',sentence.replace(' ','-'))

#############################STDIN#############################################################

##TESTINPUT############TESTINPUT############TESTINPUT############TESTINPUT############TESTINPUT##########
#Text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT '
#k = 4
#d = 1
##TESTINPUT############TESTINPUT############TESTINPUT############TESTINPUT############TESTINPUT##########

def frequent_words_with_mismatches(Text, k,d):
    FrequentPatterns = [] #for output
    Close = {} #act as a counter/place holder
#    FrequencyArray = {} #to store approximate pattern count values/how many times a pattern appears in text with d mismatches

    for i in range(0, 4**k): #set up Close array and FrequencyArray with initial values '0'
        Close[i] = 0
#        FrequencyArray[i] = 0

    for i in range(0, len(Text)-k+1):
        #Neighborhood holds all k-mers with d mismatches of pattern Text(i,k)
        Neighborhood = neighbours(Text[i:i+k], d)
        for Pattern in Neighborhood: #loop through all kmers and mismatches of Text(i,k)
            index = PatternToNumber(Pattern) #converting kmers to a number as index
            Close[index] += 1 #in Close array set value of index kmer conversion to 1
    maxCount = max(Close.values())

#    for i in range(0, 4**k):
#        if Close[i] == 1: #for all indices with value 1 of which we set in the previous for loop
#            Pattern = number_to_pattern(i, k) #convert number/index back to a Pattern
            #compute approximate_pattern_count for these patterns with d mismatches and append to FrequencyArray at the same index
#            FrequencyArray[i] = approximate_pattern_count(Text, Pattern, d)

    #find max value in frequency array this points out to the most frequent words with mismatches
#    maxCount = max(FrequencyArray.values())

    for i in range(0, 4**k):
#        if FrequencyArray[i] == maxCount:
        if Close[i] == maxCount:
            Pattern = number_to_pattern(i, k)
            FrequentPatterns.append(Pattern)
    FrequentPatternsNoDuplicates = remove_duplicates(FrequentPatterns)
    return FrequentPatternsNoDuplicates


def remove_duplicates(Text):
    ItemsNoDuplicates = []
    for item in Text:
        if item not in ItemsNoDuplicates:
            ItemsNoDuplicates.append(item)
    return ItemsNoDuplicates

def count_dict(Text, k):
    Count = {} # output variable
    # your code here
    for i in range((len(Text))-k+1):
        Pattern = Text[i:i+k]
        Count[i] = approximate_pattern_count(Pattern, Text, d)
    return Count

###########################################Subcodes############################################################

##approximate_pattern_count code START##################################
def approximate_pattern_count(Pattern, Text, d):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:len(Pattern)+1] == Pattern:
            count += 1
        elif Text[i:len(Pattern)+1] != Pattern:
            if hamming_distance(Text[i:i+len(Pattern)], Pattern) <= d:
                count += 1
    return count

def hamming_distance(p, q):
    # your code here
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
##approximate_pattern_count code END####################################

##neighbours code START#########################################
def neighbours(Pattern, d):
    if d == 0:
        return ([Pattern])
    if len(Pattern) == 1:
        return (['A', 'C', 'G', 'T'])
    Neighborhood = []
    Suffixneighbours = neighbours(suffix(Pattern), d)

    for Text in (Suffixneighbours):
        if hamming_distance(suffix(Pattern), Text) <d:
            for base in "ACGT":
                Neighborhood.append(base + Text)
        else:
            Neighborhood.append(FirstSymbol(Pattern) + Text)
    return (Neighborhood)


def FirstSymbol(Pattern):
    return Pattern[0]

def suffix(Pattern):
    suffix = Pattern[1:len(Pattern)]
    return (suffix)
##neighbours code END##############################################

##PatternToNumber code START##############################################

def PatternToNumber(Pattern):
    prefix = ''
    if Pattern == '':
        return 0
    symbol = last_symbol(Pattern)
    prefix = (prefix(Pattern))
    return 4 * PatternToNumber(prefix) + symbol_to_number(symbol)

def last_symbol(Pattern):
    return Pattern[-1]

def prefix(Pattern):
    return Pattern[:len(Pattern)-1]

def symbol_to_number(symbol):
    if symbol == "A":
        return 0
    elif symbol == "C":
        return 1
    elif symbol == "G":
        return 2
    else:
        return 3


def number_to_pattern(index, k):
    prefixPattern = ''
    if k == 1:
        return number_to_symbol(index)
    prefixIndex = Quotient(index, 4)
    r = Remainder(index, 4)
    symbol = number_to_symbol(r)
    prefixPattern += symbol
    for i in range(k-1):
            r = Remainder(int(prefixIndex), 4)
            symbol = number_to_symbol(r)
            prefixPattern += symbol
            prefixIndex = Quotient(int(prefixIndex), 4)
    return reverse(prefixPattern)

def reverse(text):
    result = ''
    count = len(text) -1
    for x in text:
        result += text[count]
        count -=1
    return result

def number_to_symbol(r):
    if r == 0:
        return "A"
    elif r == 1:
        return "C"
    elif r == 2:
        return "G"
    else:
        return "T"

def Remainder(num, n):
    return int(num)%n

def Quotient(num, n):
    return int(num)/n

def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count
print(frequent_words_with_mismatches("ATAATGAATGAATGAATGAAGCGCGCGCTGAAATAAATAAGCGCTGAATGAATGGATAATGGTGGTGAAGCGCTGGGCGCATAACAAAGCGCTGGATAATGAATGAAATAACAAACAAATGAATGGTGAAGCGCTGAACAAATGGGCGCATAAGCGCTGAACAAAATAATGGATAATGGTGAATGAACAAAATAAGCGCGCGCTGGCAAATGGATAATGAAGCGCTGAAATAACAAAGCGCGCGCTGAATGAAATAATGAATGAAGCGCCAAAGCGCTGAAATAATGAACAAATGAATGGCAAACAAAGCGCTGAACAAAATAA",5,3))


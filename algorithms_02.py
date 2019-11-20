def hamming_distance(p, q):
    count=0
    for i in range(0,len(p)):
        if p[i]!=q[i]:
            count+=1
    return count

def approximated_hamming_distance(p,q,dev):
    err_count = 0
    for i in range(0,len(p)):
        if p[i]!=q[i]:
            err_count+=1
        else:
            err_count +=0
    if err_count<=dev:
        return True
    return False

def approximated_pattern_matching(Text,Pattern,d):
    positions = []
    for i in range(0,len(Text)):
        print(Text[i:i+len(Pattern)])
        if ApproximatedHammingDistance(Text[i:i+len(Pattern)],Pattern,d):
            positions.append(i)
        elif len(Text[i:len(Text)])<=len(Pattern):
            break
    return positions
str_from_file = open('dataset_9_4.txt', 'r').read()


def approximate_pattern_count(Text, Pattern, d):
    count = 0
    for i in range(len(Text)-len(Pattern)):
        Pt = Text[i:i+len(Pattern)]
        if HammingDistance(Pattern, Pt) <= d:
            count=count+1
    return count
    
def minimum_skew(genome):
    positions = []
    skew_genome = Skew(genome)
    m = min(skew_genome.values())
    n = len(Genome)
    for i in range(1, n+1):
        if skew_genome[i] == m:
            positions.append(i)
    return positions

def skew(genome):
    skew = {}
    n = len(genome)
    for i in range(1, n+1):
        skew[0] = 0
        if genome[i-1] == "G":
            skew[i] = skew[i-1] + 1
        elif genome[i-1] == "C":
            skew[i] = skew[i-1] - 1
        else:
            skew[i] = skew[i-1]
    return skew

print(hamming_distance("TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC","GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"))
print(approximate_pattern_count("CATGCCATTCGCATTGTCCCAGTGA","CCC",2))

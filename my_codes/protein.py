# Is easy to decoding a sequence of genetic code, but, is extremely slow try to decode a large sequence if you do not have a program for that sittuation. For this purpose I imagined a program to solve this problem.
# All my knowledge about genetics is based on my high school education and internet research, so don't take everything i said as the truth. I'm just a science lover.
# I used the insulin B-chain to test in this program. But I added start and end codons to run and stop the code, another problem is that I only found protein sequence... So I took poetic license to create a sequence of letters that  match with the proteins.
#  Insulin B-chain: AUGUUUGUGAACCAGCAUUUAUGUGGUAGUCACCUGGUAGAAGCCUUGUAUCUUGUCUGCGGGGAGCGAGGCUUCUUUUACACACCCAAAGCUUGA

def decode(sequence):
    # FIRST, SET UP RULES
    if not sequence.isalpha():
        return print("The sequence must be alphabetic.")
    
    sequence.upper()
    start = sequence.find("AUG")
    length = len(sequence)
    num_codon = 0
    cytosine = 0
    adenine = 0
    guanine = 0
    uracil = 0
    if start == -1:
        return print("There's no a start codon.")
    
    # SECOND, THE PROGRAM
    while not start == length:
        codon = sequence[start] + sequence[start + 1] + sequence[start + 2]
        cytosine += codon.count("C")
        adenine += codon.count("A")
        guanine += codon.count("G")
        uracil += codon.count("U")
        match codon:
            case "CGU" | "CGC" | "CGA" | "CGG" | "AGA" | "AGG":
                print("Arg", end=" ")
            case "UCU" | "UCC" | "UCA" | "UCG" | "AGU" | "AGC":
                print("Ser", end=" ")
            case "UUA" | "UUG" | "CUU" | "CUA" | "CUA"| "CUG":
                print("Leu", end=" ")
            case "GGU" | "GGC" | "GGA" | "GGG":
                print("Gly", end=" ")
            case "GCU" | "GCC" | "GCA" | "GCG":
                print("Ala", end=" ")
            case "ACU" | "ACC" | "ACA" | "ACG":
                print("Thr", end=" ")
            case "CCU" | "CCC" | "CCA" | "CCG":
                print("Pro", end=" ")
            case "GUU" | "GUC" | "GUA" | "GUG":
                print("Val", end=" ")
            case "AUU" | "AUC" | "AUA":
                print("Ile", end=" ")
            case "UUU" | "UUC":
                print("Phe", end=" ")
            case "UAU" | "UAC":
                print("Tyr", end=" ")
            case "CAU" | "CAC":
                print("His", end=" ")
            case "CAA" | "CAG":
                print("Gln", end=" ")
            case "AAU" | "AAC":
                print("Asn", end=" ")
            case "AAA" | "AAG":
                print("Lys", end=" ")
            case "GAU" | "GAC":
                print("Asp", end=" ")
            case "GAA" | "GAG":
                print("Glu", end=" ")
            case "UGU" | "UGC":
                print("Cys", end=" ")
            case "UGG":
                print("Trp", end=" ")
            case "AUG": # START CODON
                print("Met", end=" ")
            case "UAA" | "UAG" | "UGA": #END CODON
                tot_nitro_bases = adenine + cytosine + guanine + uracil
                print()
                print(f"The numbers of useful codons in this sequence is: {num_codon}")
                print(f"There is {tot_nitro_bases} nitrogenous bases in wich: {round(adenine/tot_nitro_bases*100, 2)}% are adenines, {round(cytosine/tot_nitro_bases*100, 2)}% cytosines, {round(guanine/tot_nitro_bases*100, 2)}% guanines, {round(uracil/tot_nitro_bases*100, 2)}% uraciles")
                break
            case _:
                print("The codon is incorect or incomplete")
                break
        num_codon += 1
        start += 3
        


#sequence = input("Write the genetic code for decode: ")
sequence = "AAAAAAAAAAAAAUGUUUGUGAACCAGCAUUUAUGUGGUAGUCACCUGGUAGAAGCCUUGUAUCUUGUCUGCGGGGAGCGAGGCUUCUUUUACACACCCAAAGCUUGAUUUUUUUUUUUUUUUCCUUAAAA"

decode(sequence)
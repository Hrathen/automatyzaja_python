#  Jesteś naukowcem i otrzymujesz sekwencję DNA do analizy. Musisz sprawdzić, czy sekwencja zawiera błędy sekwencjonowania i
#  przeprowadzić jej korektę.
#
# Twoje zadania:
# 1. Policzyć ile razy występuje w kodzie każda zasada azotowa – adenina(A), cytozyna(C), guanina(G), tymina(T).
# 2. Zidentyfikować i policzyć błędy sekwencjonowania – znaki, które nie są żadną z czterech zasad azotowych.
# 3. Skorygować sekwencje GAGA na AGAG .
# 4. Znaleźć indeks w skorygowanej sekwencji, gdzie występuje 7 guanin (G) z rzędu.
# 5. Znaleźć indeks, gdzie od końca skorygowanej sekwencji występuje 6 cytozyn (C) z rzędu.
# 6. Policzyć, ile razy w kodzie pojawiła się sekwencja CTGAAA .
# 7. Znaleźć i policzyć sekwencje CTGAAN (gdzie N może być dowolną zasadą azotową), traktując N jako potencjalną adeninę.
# 8. Oczyścić DNA z błędów (usunąć znaki - i N )
# 9. Na podstawie oczyszczonej nici DNA, utworzyć nić RNA, gdzie każda tymina ( T ) zostanie zastąpiona przez uracyl ( U ).
#
# Wskazówki:
# Do policzenia występowania zasad użyj metody .count() .
# Do znalezienia indeksów możesz użyć metody .find() lub .rfind() dla odnalezienia sekwencji od końca.
# Do zamiany GAGA na AGAG użyj metody .replace() .
# Do oczyszczenia DNA z błędów można użyć pętli lub wyrażeń regularnych, ale z powodu braku znajomości pętli, skupmy się na
# metodach stringa .replace() i .rfind() do identyfikacji wzorców.
# Do utworzenia nić RNA użyj ponownie metody .replace() .

# # Skopiuj tutaj całą sekwencję DNA jako DNA
# dna_seq = "ACTG..."
# # 1. Policz wystąpienia każdej zasady azotowej
# count_A = ...

dna_seq  = """
ACTGTGCTGACTCCCGGTGCTGCCGCTGCCATAGCTAAAGCCCGGGTCCTGGTAGGCAGGCGGGAAGCAG
GGTGGGGGTCCCGGGTACTGGTAGGGGTAGCCCTGACCCAGAGGCGGGGGGGCAGCCGGGTGGGGCAGCG
GGGCCAGCGTGTCCTGAA-CGAAGTCCCACTGGAGCCACTGTTGAGGTTCAGGGTGGCGAGATCTGGCGG
NNNAGGGTAGGTGAGGGCCGCGGAGGGGCCTCCGGCGTTCCCCTCCCCCCCGCCCTGAAACCCGAAGCCC
CCACTCACTGCTGCAGAGATCCCCTGAAAACGTAGTAGCACTGCTCgagacAGGTGATCTGTTGACCTGA
AACCGCAGGAAGCCGTGCTTCAGCAAGCTGCTGGCGTACTTCCGGGCCT---GCCGCTCCTTGAAGCCCT
CCACGTGTGTGTACAGCCAGTCCACCACGTCCGCCCCTGGCCGGCACCAGCGGTCAGCCCGCAGCCTCGA
GGCAAGCAGCCCTGCCNNTGGCACTATCCGC-CGCGGGGACGGCCACTCACCGATGACGGCATNNGCGAT
GGTGATCTTGAGCCACATGCGGTCGCGGATCTCCAGTCCCGAG---GGCAGCTGCATGACCCGGACGACG
GCGCTCATGTCACtcaccgtcagcggcgcctcttccagCCAGCTCTGCAAAGCACAGACAGCCCCGCTTC
GCCCCAGCATCTGAAAGCGGGGGACTCggcAcgCTGCACCCCCAGGGGAGCCTCTGGGCAGAGCCTGCGC
CAGGGCGCAAGCTGGACGGTGCGTGACAGCAGGGCCCCGGCCCACTGCAGGATGCACCCCCGTGAGGCTG
GGGCGTGAGCAGGGGGGTTGGACAtttAGTCTCCCACTTCTACAGACACTTTTCATCAGGATCCTAGGCA
CAAACTGGGCTGAAACCCCACCCTGCAGACCAGGAAGTAATGAGAACAGGGCAGGCCCCTTCCCCTCNNC
GCATGCC-CACCCGAGAGCGCAGGCTGTTAGTCGTGTTAATGGCAGGAAGCAGAATGGAGACCTGGCCCC
TGCCTCTGAA-CCGTGGGTGCTCaactggctaGCCCTACGTACATCCCCTGTTCcggCCAACACACAGAC
ATGAGCAGGATGGGCTGCACAAGGTGGGCACGGGTGCCTGTGCACACGTCTGTGCAGGGAGTTGGGGACA
GGCAACACACACGTGTCACAGCCCCATGACGGggcaattgcGCCATGCTGGCTGAATGGCAGAGACGCCC
CTCCAAGCCTCGGTTTCTGCTGGGGCCCTCAGGAGCTGCCACTTACGTGGAGCACCAGGCACGGAGCTGG
TTAGTGAGGAGGAGCTGGTGCGCGTGACGGCGCTGGAGCAGGGACTCGTACCGTAGCGGGGCAGGGCNNN
TGTCAGTGCCGCCGTGTGGtcagcggcgatCGGCG-GGTCGATGGGCCGCACCGGGTCAGCTGGGTGNAG
ACACGTGGCGATGACAGGCGGACAGATGGACAGGGTGGGAGGGCAGGGTGCAGGGCACAGAGGAGAGAGG
CCTTCAGGCTAGGTAGGCGCCCCCTCCCCATCCCGccccGTGTGCCCCGAGGGCCACTCACCCCGTGGGA
CGGTGAAGTAGCTTCG-GGCGTTGGGTCCAGCACTTGGCCACAGTGAGGCTGNAAATGGCTGCAGGAACG
GTGGTCCCCCCGCAAGGCCCCCATGGTCCCACCTCCCTGCCTGGCCCCTCCCGCTCCAGCGCCNCCAGCC
"""

#1

print("\n1. Wyniki anlizy DNA: \n------------------\n")

dna1 = dna_seq

count_A =dna1.count("A")
print(f"W sekwencji znajduje się {count_A} cząsteczek adeniny")

dna2 = dna_seq

count_C =dna2.count("C")
print(f"W sekwencji znajduje się {count_C} cząsteczek cytozyny")

dna3 = dna_seq

count_G =dna1.count("G")
print(f"W sekwencji znajduje się {count_G} cząsteczek guaniny")

dna4 = dna_seq

count_T =dna1.count("T")
print(f"W sekwencji znajduje się {count_T} cząsteczek tyminy \n")

print("***Analiza zakończona***")

#2

print("\n2. Wykrywanie błędów sekwencjonowania:")


#3

print("\n3. Zmiana sekwencji DNA:")

dna3 = dna_seq

dna_replace = dna3.replace("GAGA", "AGAG")

print(dna_replace)
print("***Zmiana sekwencji zakończona***")

#8

print("\n8. Oczyszczanie próbki DNA")

dna8 = dna_seq

clean_DNA = dna8.replace("-","").replace("N","")
print(clean_DNA)

print("\n***Oczyszczanie próbki DNA zakończono")

#9

print("\n9. Tworzenie nici RNA")

dna9 = clean_DNA

rna = dna9.replace("T","U")
print(rna)

print("\n***Tworzenie nici RNA zakończone")




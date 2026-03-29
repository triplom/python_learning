# Bioinformatics with Python
# Course 3 (Python para Bioinformática) · Course 1 §8
# pip install biopython (optional — core logic works without it)

# ═══════════════════════════════════════
#  DNA / RNA / PROTEIN BASICS
# ═══════════════════════════════════════

DNA_COMPLEMENT = str.maketrans("ATCG", "TAGC")
CODON_TABLE = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}


def gc_content(seq):
    """Return GC content as percentage."""
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100 if seq else 0


def complement(dna):
    """Return DNA complement (5'→3')."""
    return dna.upper().translate(DNA_COMPLEMENT)


def reverse_complement(dna):
    """Return reverse complement (antiparallel strand)."""
    return complement(dna)[::-1]


def transcribe(dna):
    """DNA → mRNA (T → U)."""
    return dna.upper().replace("T", "U")


def translate(mrna, start=0):
    """mRNA → protein (stop at * codon)."""
    protein = []
    mrna = mrna.upper().replace("U", "T")
    for i in range(start, len(mrna) - 2, 3):
        codon = mrna[i : i + 3]
        aa = CODON_TABLE.get(codon, "?")
        if aa == "*":
            break
        protein.append(aa)
    return "".join(protein)


# ─── Demo ─────────────────────────────────────────────────────────────────────
sample_dna = "ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG"
print("=== DNA Analysis ===")
print(f"Sequence:           {sample_dna}")
print(f"Length:             {len(sample_dna)} bp")
print(f"GC content:         {gc_content(sample_dna):.1f}%")
print(f"Complement:         {complement(sample_dna)}")
print(f"Reverse complement: {reverse_complement(sample_dna)}")
mrna = transcribe(sample_dna)
print(f"mRNA:               {mrna}")
protein = translate(mrna)
print(f"Protein:            {protein}")

# ═══════════════════════════════════════
#  FASTA PARSING (without Biopython)
# ═══════════════════════════════════════

SAMPLE_FASTA = """>seq1 Homo sapiens BRCA1 fragment
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTT
AGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTT
>seq2 Mus musculus Brca1 fragment  
ATGGATTTATCTGCTCTGCGCGTTGAAGAAGTACAAAATGTCGTTAATGCTATGCAGAAAATCTT
AGAGTGTCCCATCTGTCTGGAGTTGATCAAGAAACCTGTCTCCACAAAGTGTGACCACATATTTT
>seq3 Pan troglodytes BRCA1 fragment
ATGGATTTATCTGCTCTTCGCGTTGAAGAAGTACAAAATGTCATTAATGCTATGCAGAAAATCTT
AGAGTGTCCCATCTGTCTGGAGTTGATCAAGGAACCTGTCTCCACAAAGTGTGACCACATATTTT
"""


def parse_fasta(fasta_text):
    """Parse FASTA format into list of (id, description, sequence) tuples."""
    sequences = []
    current_id = current_desc = current_seq = None
    for line in fasta_text.strip().split("\n"):
        if line.startswith(">"):
            if current_id:
                sequences.append((current_id, current_desc, current_seq))
            parts = line[1:].split(None, 1)
            current_id = parts[0]
            current_desc = parts[1] if len(parts) > 1 else ""
            current_seq = ""
        else:
            current_seq += line.strip()
    if current_id:
        sequences.append((current_id, current_desc, current_seq))
    return sequences


sequences = parse_fasta(SAMPLE_FASTA)
print("\n=== FASTA Sequences ===")
for sid, desc, seq in sequences:
    print(f"\nID:   {sid}")
    print(f"Desc: {desc}")
    print(f"Len:  {len(seq)} bp")
    print(f"GC:   {gc_content(seq):.1f}%")
    print(f"Protein: {translate(seq)}")

# ═══════════════════════════════════════
#  PAIRWISE ALIGNMENT (Needleman-Wunsch)
# ═══════════════════════════════════════


def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
    """Global sequence alignment — Needleman-Wunsch algorithm."""
    n, m = len(seq1), len(seq2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i * gap
    for j in range(m + 1):
        dp[0][j] = j * gap

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            score = match if seq1[i - 1] == seq2[j - 1] else mismatch
            dp[i][j] = max(
                dp[i - 1][j - 1] + score,
                dp[i - 1][j] + gap,
                dp[i][j - 1] + gap,
            )

    # Traceback
    aligned1, aligned2 = [], []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            score = match if seq1[i - 1] == seq2[j - 1] else mismatch
            if dp[i][j] == dp[i - 1][j - 1] + score:
                aligned1.append(seq1[i - 1])
                aligned2.append(seq2[j - 1])
                i -= 1
                j -= 1
                continue
        if i > 0 and dp[i][j] == dp[i - 1][j] + gap:
            aligned1.append(seq1[i - 1])
            aligned2.append("-")
            i -= 1
        else:
            aligned1.append("-")
            aligned2.append(seq2[j - 1])
            j -= 1

    a1 = "".join(reversed(aligned1))
    a2 = "".join(reversed(aligned2))
    identity = sum(c1 == c2 and c1 != "-" for c1, c2 in zip(a1, a2))
    match_line = "".join("|" if c1 == c2 else " " for c1, c2 in zip(a1, a2))
    return a1, match_line, a2, dp[n][m], identity / max(n, m) * 100


print("\n=== Pairwise Alignment ===")
s1 = sequences[0][2][:40]
s2 = sequences[1][2][:40]
a1, match_line, a2, score, pct_id = needleman_wunsch(s1, s2)
print(f"Seq1: {a1}")
print(f"      {match_line}")
print(f"Seq2: {a2}")
print(f"Score: {score}  |  Identity: {pct_id:.1f}%")

# ═══════════════════════════════════════
#  STATISTICS — GC content across sequences
# ═══════════════════════════════════════

import statistics

gc_values = [gc_content(seq) for _, _, seq in sequences]
print(f"\n=== GC Content Stats ===")
print(f"Mean:   {statistics.mean(gc_values):.2f}%")
print(f"Stdev:  {statistics.stdev(gc_values):.2f}%")
print(f"Min:    {min(gc_values):.2f}%")
print(f"Max:    {max(gc_values):.2f}%")

# LAB EXERCISES
# 1. Parse a real FASTA file (download one from NCBI GenBank).
# 2. Find all ORFs (Open Reading Frames) starting with ATG in a sequence.
# 3. Compute pairwise identity for all pairs in a set of 4+ sequences
#    and display as a distance matrix.
# 4. Plot GC content variation in a sliding window across a long sequence.

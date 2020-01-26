def to_rna(dna_strand):
    """
    Returns the RNA for a DNA strand

    :param
    dna_strand: string

    :return:
    RNA: string
    """
    dna_to_rna = (lambda rna: {
        'C': 'G',
        'G': 'C',
        'T': 'A',
        'A': 'U'
    }[rna])

    return ''.join(list(map(dna_to_rna, dna_strand)))

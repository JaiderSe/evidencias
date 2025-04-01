export function translate (rna) {
  const codonToProtein = {
    AUG: 'Methionine',
    UUU: 'Phenylalanine',
    UUC: 'Phenylalanine',
    UUA: 'Leucine',
    UUG: 'Leucine',
    UCU: 'Serine',
    UCC: 'Serine',
    UCA: 'Serine',
    UCG: 'Serine',
    UAU: 'Tyrosine',
    UAC: 'Tyrosine',
    UGU: 'Cysteine',
    UGC: 'Cysteine',
    UGG: 'Tryptophan',
    UAA: 'STOP',
    UAG: 'STOP',
    UGA: 'STOP'
  }

  if (!rna) return []

  const codons = rna.match(/.{1,3}/g) || []
  const proteins = []

  for (const codon of codons) {
    const protein = codonToProtein[codon]
    if (!protein) {
      throw new Error('Invalid codon')
    }
    if (protein === 'STOP') {
      break
    }
    proteins.push(protein)
  }

  return proteins
}

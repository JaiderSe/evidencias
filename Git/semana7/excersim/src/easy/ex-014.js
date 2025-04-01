export function findAnagrams (word, candidates) {
  const wordSorted = word.toLowerCase().split('').sort().join('')
  const anagrams = []

  for (let i = 0; i < candidates.length; i++) {
    const candidate = candidates[i]
    const candidateSorted = candidate.toLowerCase().split('').sort().join('')

    if (wordSorted === candidateSorted && word.toLowerCase() !== candidate.toLowerCase()) {
      anagrams.push(candidate)
    }
  }

  return anagrams
}

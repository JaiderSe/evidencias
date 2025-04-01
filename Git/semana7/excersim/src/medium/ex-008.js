export function rows (str) {
  if (str === 'A') return ['A']

  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  const indexstr = alphabet.indexOf(str)
  const firstPart = alphabet.slice(0, indexstr)
  const lastPart = firstPart.split('').reverse().join('')
  const strsNeeded = firstPart + str + lastPart
  const rowWidth = strsNeeded.length
  const result = []

  result.push(' '.repeat((rowWidth - 1) / 2) + strsNeeded[0] + ' '.repeat((rowWidth - 1) / 2))

  const upperRows = []

  for (let i = 1; i < (Math.floor(rowWidth / 2)); i++) {
    const rowPart1 = ' '.repeat((rowWidth - 1) / 2 - i)
    const rowPart2 = strsNeeded[i]
    const rowPart3 = ' '.repeat(Math.max(0, i * 2 - 1))
    const rowPart4 = strsNeeded[i]
    const rowPart5 = ' '.repeat((rowWidth - 1) / 2 - i)
    const row = rowPart1 + rowPart2 + rowPart3 + rowPart4 + rowPart5
    upperRows.push(row)
  }

  result.push(...upperRows)
  result.push(str + ' '.repeat(rowWidth - 2) + str)
  result.push(...upperRows.reverse())
  result.push(' '.repeat((rowWidth - 1) / 2) + strsNeeded[0] + ' '.repeat((rowWidth - 1) / 2))

  return result
}

export function convert (value) {
  let result = ''
  if (value % 3 === 0) result += 'Pling'
  if (value % 5 === 0) result += 'Plang'
  if (value % 7 === 0) result += 'Plong'
  return result || value.toString()
}

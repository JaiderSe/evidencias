export function rotate (str, num) {
  const alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  const alphabetArr = alphabet.split('')
  const strArr = str.split('')
  let result = ''
  const uppercaseArr = strArr.map((char) => {
    if (alphabetArr.includes(char)) {
      const isUppercase = char === char.toUpperCase()
      const index = alphabetArr.indexOf(char.toLowerCase())
      const newIndex = (index + num) % 26
      const newChar = alphabetArr[newIndex]
      return isUppercase ? newChar.toUpperCase() : newChar
    } else {
      return char
    }
  })
  result = uppercaseArr.join('')
  return result
}

export function isArmstrongNumber (n) {
  const digits = n.toString().split('').map(Number)
  const p = digits.length
  let sum = 0
  for (let i = 0; i < digits.length; i++) {
    sum += Math.pow(digits[i], p)
  }
  return sum === n
}

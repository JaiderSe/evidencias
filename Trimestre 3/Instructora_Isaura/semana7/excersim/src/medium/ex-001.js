export function prime (position) {
  const primes = []

  if (position === 0) throw new Error('there is no zeroth prime')

  for (let i = 2; primes.length < position; i++) {
    if (isPrime(i)) primes.push(i)
  }

  return primes[position - 1]
}

function isPrime (n) {
  if (n <= 1) {
    return false
  }
  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) {
      return false
    }
  }
  return true
}

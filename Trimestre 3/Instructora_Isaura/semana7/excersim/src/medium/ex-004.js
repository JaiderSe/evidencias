export function primeFactors (n) {
  const primes = []
  for (let i = 2; i <= n; i++) {
    while (n % i === 0) {
      n /= i
      primes.push(i)
    }
  }
  return primes
}

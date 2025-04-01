export function primes (n) {
  const isPrime = new Array(n + 1).fill(true)

  isPrime[0] = false
  isPrime[1] = false

  for (let i = 2; i <= Math.sqrt(n); i++) {
    if (isPrime[i]) {
      for (let j = i * i; j <= n; j += i) {
        isPrime[j] = false
      }
    }
  }

  const primes = []
  for (let i = 2; i <= n; i++) {
    if (isPrime[i]) {
      primes.push(i)
    }
  }

  return primes
}

// export function primes (n) {
//   const primes = []

//   for (let i = 2; i <= n; i++) {
//     const res = isPrime(i)
//     if (res) {
//       primes.push(i)
//     }
//   }
//   return primes
// }

// function isPrime (n) {
//   if (n <= 1) {
//     return false
//   }
//   for (let i = 2; i <= Math.sqrt(n); i++) {
//     if (n % i === 0) {
//       return false
//     }
//   }
//   return true
// }

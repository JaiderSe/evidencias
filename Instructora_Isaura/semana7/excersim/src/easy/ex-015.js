export class DiffieHellman {
  constructor (p, g) {
    if (!this.isPrime(p)) {
      throw new Error('p must be prime')
    }
    if (!this.isPrime(g)) {
      throw new Error('g must be prime')
    }
    this.p = p
    this.g = g
  }

  getPublicKey (privateKey) {
    if (privateKey <= 1 || privateKey >= this.p) {
      throw new Error('privateKey must be greater than 1 and less than p')
    }
    return Math.pow(this.g, privateKey) % this.p
  }

  getSecret (theirPublicKey, myPrivateKey) {
    return Math.pow(theirPublicKey, myPrivateKey) % this.p
  }

  isPrime (n) {
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
}

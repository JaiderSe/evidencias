export function squareRoot (n) {
  if (n < 0) {
    return NaN
  }

  if (n === 0) {
    return 0
  }

  const precision = 0
  let start = 0
  let end = n

  if (n < 1) {
    end = 1
  }

  while (end - start > precision) {
    const mid = (start + end) / 2
    const midSqr = mid * mid
    if (midSqr === n) {
      return mid
    } else if (midSqr < n) {
      start = mid
    } else {
      end = mid
    }
  }

  return (start + end) / 2
}

// Math.sqrt(n)

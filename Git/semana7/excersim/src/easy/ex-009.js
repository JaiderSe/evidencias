/* eslint-disable no-unreachable */
export function timeToMixJuice (juice) {
  switch (juice) {
    case 'Pure Strawberry Joy':
      return 0.5
      break
    case 'Energizer':
      return 1.5
      break
    case 'Green Garden':
      return 1.5
      break
    case 'Tropical Island':
      return 3
      break
    case 'All or Nothing':
      return 5
      break
    default:
      return 2.5
      break
  }
}

export function limesToCut (wedgesNeeded, limes) {
  const recipe = {
    small: 6,
    medium: 8,
    large: 10
  }

  let sum = 0
  let count = 0

  if (limes.length === 0) return 0
  for (let i = 0; i < limes.length; i++) {
    if (sum >= wedgesNeeded) return count
    if (i + 1 === limes.length) return count + 1
    sum += recipe[limes[i]]
    count += 1
  }
}

export function remainingOrders (timeLeft, orders) {
  let sum = 0
  let time = 0

  do {
    time = timeToMixJuice(orders[0])
    sum += time
    orders.shift()
  } while (sum < timeLeft)
  return orders
}

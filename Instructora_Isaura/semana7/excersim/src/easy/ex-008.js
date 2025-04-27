export function totalBirdCount (birdsPerDay) {
  let sum = 0
  for (let index = 0; index < birdsPerDay.length; index++) {
    sum += birdsPerDay[index]
  }
  return sum
}

export function birdsInWeek (birdsPerDay, weekNumber) {
  const start = (weekNumber - 1) * 7
  const end = start + 7
  const birdsInWeek = birdsPerDay.slice(start, end)
  const sum = birdsInWeek.reduce((total, birds) => total + birds, 0)
  return sum
}

export function fixBirdCountLog (birdsPerDay) {
  for (let index = 0; index < birdsPerDay.length; index++) {
    if ((index + 1) % 2 !== 0) {
      birdsPerDay[index] += 1
    }
  }
  return birdsPerDay
}

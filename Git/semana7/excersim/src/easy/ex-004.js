const HOURS_PER_DAY = 8

export function dayRate (ratePerHour) {
  return ratePerHour * HOURS_PER_DAY
}

export function daysInBudget (budget, ratePerHour) {
  return Math.floor(budget / dayRate(ratePerHour))
}

export function priceWithMonthlyDiscount (ratePerHour, numDays, discount) {
  const DAYS_PER_MONTH = 22
  const ratePerDay = dayRate(ratePerHour)
  const numMonths = Math.floor(numDays / DAYS_PER_MONTH)
  const numDaysLeft = numDays % DAYS_PER_MONTH

  const pricePerMonthWithDiscount = DAYS_PER_MONTH * ratePerDay * (1 - discount)
  const totalPricePerMonth = numMonths * pricePerMonthWithDiscount
  const totalPricePerDay = numDaysLeft * ratePerDay

  return Math.ceil(totalPricePerMonth + totalPricePerDay)
}

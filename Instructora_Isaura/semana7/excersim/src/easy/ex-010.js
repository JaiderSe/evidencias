const GIGASECONDS = 10 ** 9

export const gigasecond = (date) => {
  const newDate = new Date(date.getTime())
  newDate.setUTCSeconds(date.getUTCSeconds() + GIGASECONDS)
  return newDate
}

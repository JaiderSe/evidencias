import { EXPECTED_MINUTES_IN_OVEN, remainingMinutesInOven, preparationTimeInMinutes, totalTimeInMinutes } from '../../src/easy/ex-002.js'

test('EXPECTED_MINUTES_IN_OVEN > constant is defined correctly', () => {
  expect(EXPECTED_MINUTES_IN_OVEN).toBe(40)
})

test('remainingMinutesInOven > calculates the remaining time', () => {
  expect(remainingMinutesInOven(25)).toBe(15)
  expect(remainingMinutesInOven(5)).toBe(35)
  expect(remainingMinutesInOven(39)).toBe(1)
})

test('remainingMinutesInOven > works correctly for the edge cases', () => {
  expect(remainingMinutesInOven(40)).toBe(0)
  expect(remainingMinutesInOven(0)).toBe(40)
})

test('preparationTimeInMinutes > calculates the preparation time', () => {
  expect(preparationTimeInMinutes(1)).toBe(2)
  expect(preparationTimeInMinutes(2)).toBe(4)
  expect(preparationTimeInMinutes(8)).toBe(16)
})

test('totalTimeInMinutes > calculates the total cooking time', () => {
  expect(totalTimeInMinutes(1, 5)).toBe(7)
  expect(totalTimeInMinutes(4, 15)).toBe(23)
  expect(totalTimeInMinutes(1, 35)).toBe(37)
})

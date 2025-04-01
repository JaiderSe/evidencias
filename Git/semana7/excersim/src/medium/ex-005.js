export function flatten (arr) {
  return arr.flatMap(item => Array.isArray(item) ? item.flat(Infinity) : item, Infinity).filter((item) => item !== null && item !== undefined)
}

// export function removeNulls (a) {
//   return a !== null && a !== undefined
// }

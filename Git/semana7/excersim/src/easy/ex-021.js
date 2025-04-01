export function encode (arr) {
  let result = ''
  let count = 1
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === arr[i + 1]) {
      count++
    } else {
      if (count > 1) {
        result += count
      }
      result += arr[i]
      count = 1
    }
  }
  return result
}

export function decode (arr) {
  let result = ''
  let count = ''
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= '0' && arr[i] <= '9') {
      count += arr[i]
    } else {
      if (count) {
        result += arr[i].repeat(count)
        count = ''
      } else {
        result += arr[i]
      }
    }
  }
  return result
}

// encode('') // ''
// encode('XYZ') // 'XYZ'
encode('AABBBCCCC') // '2A3B4C'

export function getItem (arr, position) {
  return arr[position]
}

export function setItem (arr, position, replacementCard) {
  arr[position] = replacementCard
  return arr
}

export function insertItemAtTop (arr, newCard) {
  arr.push(newCard)
  return arr
}

export function removeItem (arr, position) {
  arr.splice(position, 1)
  return arr
}

export function removeItemFromTop (arr) {
  arr.pop()
  return arr
}

export function insertItemAtBottom (arr, newCard) {
  arr.unshift(newCard)
  return arr
}

export function removeItemAtBottom (arr) {
  arr.shift()
  return arr
}

export function checkSizeOfStack (arr, stackSize) {
  return arr.length === stackSize
}

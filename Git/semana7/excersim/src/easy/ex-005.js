export function frontDoorResponse (line) {
  return line[0]
}

export function frontDoorPassword (str) {
  return str[0].toUpperCase() + str.slice(1).toLowerCase()
}

export function backDoorResponse (str) {
  return str.trim()[str.trim().length - 1]
}

export function backDoorPassword (str) {
  return frontDoorPassword(str) + ', please'
}

export function needsLicense (kind) {
  const types = ['car', 'truck']
  return types.includes(kind)
}

export function chooseVehicle (option1, option2) {
  const vehicle = [option1, option2]
  return `${vehicle.sort()[0]} is clearly the better choice.`
}

export function calculateResellPrice (originalPrice, age) {
  return (age < 3)
    ? originalPrice * 0.8
    : (age > 10)
        ? originalPrice * 0.5
        : (age >= 3 && age <= 10)
            ? originalPrice * 0.7
            : 0
}

export function canExecuteFastAttack (knightIsAwake) {
  return !knightIsAwake
}

export function canSpy (knightIsAwake, archerIsAwake, prisonerIsAwake) {
  return knightIsAwake || archerIsAwake || prisonerIsAwake
}

export function canSignalPrisoner (archerIsAwake, prisonerIsAwake) {
  return !!((prisonerIsAwake && archerIsAwake === false))
}

export function canFreePrisoner (knightIsAwake, archerIsAwake, prisonerIsAwake, petDogIsPresent) {
  return !!((petDogIsPresent && !archerIsAwake) || (!petDogIsPresent && prisonerIsAwake && !knightIsAwake && !archerIsAwake))
}

// export function canFreePrisoner (knightIsAwake, archerIsAwake, prisonerIsAwake, petDogIsPresent) {
//   if (petDogIsPresent && !archerIsAwake) return true
//   else if (!petDogIsPresent && prisonerIsAwake && !knightIsAwake && !archerIsAwake) return true
//   else return false
// }

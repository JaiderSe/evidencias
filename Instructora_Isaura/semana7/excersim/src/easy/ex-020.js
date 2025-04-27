const ABILITIES = [
  'strength',
  'dexterity',
  'intelligence',
  'constitution',
  'wisdom',
  'charisma'
]

export function abilityModifier (score) {
  if (score < 3) {
    throw new Error('Ability scores must be at least 3')
  }
  if (score > 18) {
    throw new Error('Ability scores can be at most 18')
  }
  return Math.floor(score / 2) - 5
}

export class Character {
  static rollAbility () {
    return Math.floor(Math.random() * 15) + 3
  }

  constructor () {
    ABILITIES.forEach(a => this[a] = Character.rollAbility())
    this.hitpoints = 10 + abilityModifier(this.constitution)
  }
}

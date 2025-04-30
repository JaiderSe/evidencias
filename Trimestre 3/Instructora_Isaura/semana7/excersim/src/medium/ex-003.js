export function recite (fromVerse, toVerse) {
  fromVerse -= 1
  toVerse = toVerse ? toVerse - 1 : fromVerse
  const verseValues = [
    ['first', 'a Partridge in a Pear Tree.'],
    ['second', 'two Turtle Doves, '],
    ['third', 'three French Hens, '],
    ['fourth', 'four Calling Birds, '],
    ['fifth', 'five Gold Rings, '],
    ['sixth', 'six Geese-a-Laying, '],
    ['seventh', 'seven Swans-a-Swimming, '],
    ['eighth', 'eight Maids-a-Milking, '],
    ['ninth', 'nine Ladies Dancing, '],
    ['tenth', 'ten Lords-a-Leaping, '],
    ['eleventh', 'eleven Pipers Piping, '],
    ['twelfth', 'twelve Drummers Drumming, ']
  ]
  let verses = ''
  for (let index = fromVerse; index <= toVerse; index++) {
    verses += `On the ${verseValues[index][0]} day of Christmas my true love gave to me: ${verseValues[index][1]}`
    for (let i = index - 1; i >= 0; i--) {
      verses += i === 0 ? `and ${verseValues[i][1]}` : verseValues[i][1]
    }
    verses += index === toVerse ? '\n' : '\n\n'
  }
  return verses
}

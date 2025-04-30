export function isPaired (str) {
  const brackets = str.split('')
  const stack = []
  const open = ['(', '[', '{']
  const close = [')', ']', '}']
  const pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
  }

  for (let i = 0; i < brackets.length; i++) {
    const bracket = brackets[i]

    if (open.includes(bracket)) {
      stack.push(bracket)
    } else if (close.includes(bracket)) {
      const last = stack.pop()

      if (last !== pairs[bracket]) {
        return false
      }
    }
  }

  return stack.length === 0
}

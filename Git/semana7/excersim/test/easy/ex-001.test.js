import { hello } from '../../src/easy/ex-001.js'

test('hello', () => {
  expect(hello()).toEqual('Hello, World!')
})

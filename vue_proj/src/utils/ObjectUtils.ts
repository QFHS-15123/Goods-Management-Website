import stringIsEmpty from './StringUtils'

function objectIsNull(obj: any, exclude_array: Array<string>): boolean {
  console.log(obj.name)
  for (const key in obj) {
    if (exclude_array.indexOf(key) !== -1) {
      continue
    }
    if (isEmpty(obj[key]) === false) {
      return false
    }
  }
  return true
}

export { objectIsNull }

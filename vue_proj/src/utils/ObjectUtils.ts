function objectIsNull(obj: any, exclude_array: Array<string>): boolean {
  console.log(obj.name)
  for (const key in obj) {
    if (exclude_array.indexOf(key) !== -1) {
      continue
    }
    if (obj[key] !== null && obj[key] !== undefined && obj[key].length !== 0) {
      return false
    }
  }
  return true
}

export { objectIsNull }

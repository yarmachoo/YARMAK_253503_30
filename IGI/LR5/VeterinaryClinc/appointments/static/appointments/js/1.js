const arr = [
'Hello',
 100,
  true,
  {name: 'Alex'},
  () => console.log('xaxa'),
  [true, true, true]] //объект

console.log('arr:', arr[4]())
arr[4] = ()=>console.log('miumiu');
console.log('arr:', arr[4]())
console.log('arr:', arr[6], arr)
arr[6]='pipi'
console.log('arr:', arr[6], arr, arr.length)

arr.push('A', 'B', 'C')

console.log(arr)


arr.unshift('A', 'B', 'C')
console.log(arr)
console.log(arr.at(-1))

arr.pop()

console.log(arr.shift())

console.log(arr.toString())

console.log(arr.join(''))

arr.forEach((element, index, array)=>{
    console.log(element);
});
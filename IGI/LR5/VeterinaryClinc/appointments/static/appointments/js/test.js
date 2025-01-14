
//1
let a3;
true || (a3=1)
console.log(a3)

//2
let a1 = [1, 2, 3]
let a2 = [1, 2, 3]
console.log(a1==a2)

//3
let a = Array();
a[a.length] = 0;
a[a.length] = 1;
console.log(a.length);

//4
let a4 = {toString: function() {return '1'}};
console.log(1+a4+1);


//5
let a6 = 7//prompt('input a num');
let a7 = a6+1;
console.log("Task 7:")
console.log(a7);

//62
console.log("Task 6:")
console.log(1||4&&5||0)

//7


//8
console.log(new Date())

//9
//возвращает текущее количество миллисекунд, прошедших с 1 января 1970
console.log(Date.now()) //???

//10
var a8 = new Array(1, 2);
//создается массив с длиной 3
var a9 = new Array(3);
console.log(a8[0]+a9[0])

//11
console.log(a10+a11+a12);
var a10 = 1;
var a11 = {toString: function() {return '1';}}
var a12 = 1;
console.log(a10+a11+a12);


//12
function F() {return F;}
console.log(typeof F);
console.log(new F() instanceof F);
console.log(F instanceof Function);
//13
console.log((2.5-1)*2);

//14
let str = 'abc'
str.property = 'd';
console.log(str.property)


//15
console.log(parseInt('$12'))

console.log('123'[0])

//16
console.log(parseInt('1п'))
//17

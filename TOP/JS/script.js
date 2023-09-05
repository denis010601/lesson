// console.log(2+2*2);
// let int = 1;
// let str = "1";
// let bool = true || false;
// let massiv = [1,2,3,4,5,6];
// let obj = {
//     "name" : "name",
//     "age" : 22,
// }
// class Auto{
//     constructor(name,age){
//         this.name = name;
//         this.age = age;
//     }
//     changeName(){
//         console.log(this.name)
//     }
// }
// class AutoV2 extends Auto{
//     constructor(name,age){
//         this.name = name;
//         this.age = age;
//     }
// }

// function sum(a,b){
//     return a + b
// }

// let sum2 = (a,b) => {
//     return a + b
// }
// console.log(5/0)

// // let x = prompt("Введите ваше имя"); // строка
// // let y = +prompt("введите только число"); // число +
// // console.log(x,y)

// let i = 0;

// while(i < 10){
//     i++;
//     console.log(i)
// }

// for(let i = 0; i < 10; i++){
//     console.log(i)
// }

// let z = 1;
// let k = 2;

// if(z < k){
//     console.log("z < k")
// }
// else if(k < z){
//     console.log("k < z")
// }
// else if(k == z){
//     console.log("k = z")
// }
// else{
//     console.log("ошибка")
// }

// let hi = "hisdasdsadsad"
// console.log(`${hi} adsdsaas`)
// console.log(hi + " adsdsaas")

// let x1 = +prompt("введите 1е число");
// let x2 = +prompt("введите 2е число");
// let x3 = +prompt("введите 3е число");
// let vs = +prompt("1 - сумма всех чисел;\n2 - произведение всех чисел.")

// if(vs == 1){
//     alert(x1+x2+x3)
// }
// else if(vs == 2){
//     alert(x1*x2*x3)
// }
// else {
//     alert("Ошибка!!!")
// }
// // русский   pyton    js
// // или       or       ||
// // и         and      &&


// Math.floor(12/5)

// console.log(plus);
// console.log(minus);
// console.log(out)




let h1 = document.querySelector("#h1");
h1.innerHTML = "УРОК " + 5;

let title = document.querySelector("title");
title.innerHTML= "урок " + 5;
// let x = confirm("вы подтверждаете??")
// console.log(x)
// let plus1 = document.getElementById("plus")
let plus = document.querySelector("#plus");
let minus = document.querySelector("#minus");
let out = document.querySelector("#out");

let i = 0;

function plusOut(){
    i++;
    out.innerHTML = i;
}
function minusOut(){
    i--;
    out.innerHTML = i;
}

plus.addEventListener("click",plusOut);
minus.addEventListener("click",minusOut)

let number1 = document.querySelector("#number1");
let number2 = document.querySelector("#number2");

let calcPlus = document.querySelector("#calcPlus");
let calcMinus = document.querySelector("#calcMinus");
let calcMul = document.querySelector("#calcMul");
let calcDiv = document.querySelector("#calcDiv");

let otvet = document.querySelector("#otvet");
let ffff = "123";
ffff = Number(ffff)
function fPlus(){
    otvet.innerHTML = Number(number1.value) + Number(number2.value);

}
function fMul(){
    otvet.innerHTML = number1.value * number2.value;
}

calcPlus.addEventListener("click", fPlus)
calcMul.addEventListener("click", fMul)


let body = document.body;




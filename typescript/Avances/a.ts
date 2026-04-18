import readline from 'node:readline/promises';
import {stdin as input, stdout as output } from 'node:process'
const rl = readline.createInterface({input, output})

function mayor(a: number, b: number, c: number){
let ma: number
if(a >= b && a >= c) ma=a;
else if(b >= a && b >= c) ma=b;
else ma=c;
return `Mayor: ${ma}`;
}
function menor(a: number, b: number, c: number){
let me: number
if(a <= b && a <= c) me=a;
else if(b <= a && b <= c) me=b;
else me=c;
return `Menor: ${me}`;
}

    
console.log("********Mayor Menor**********")
const a = await rl.question("Introduzca el valor de a: ")
const b = await rl.question("Introduzca el valor de b: ")
const c = await rl.question("Introduzca el valor de c: ")

console.log(mayor(a,b,c));
console.log(menor(a,b,c));
rl.close();
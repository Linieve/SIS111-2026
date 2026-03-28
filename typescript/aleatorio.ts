import readline from 'node:readline/promises';
import {stdin as input, stdout as output } from 'node:process'
const rl = readline.createInterface({input, output})

function aleatorio(a: number){
    let pares = "pares: ";
    let impares = "impares: ";
    let k = "";
    for(let i:number = 0; i<a; i++){
        let numero = (Math.random()*100) * 1;
        console.log(numero)
        if(numero%2==0){
            pares += `${numero}, `;
        }else{
            impares += `${numero}, `;
        }
    }
    k = pares + impares;
    return k;
}

const a = await rl.question("Introduzca el valor de a: ")
console.log(aleatorio(a));
rl.close;
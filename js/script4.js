//OBJETO LITERAL
/*
var coche = {
    marca: "inventada",
    modelo: "camioneta",
    color: "verde",
    numRuedas: 4,
    numPuertas: 6,
    precio: 300000,
};

console.log("Información del coche");
console.log("Marca: " + coche.marca + ".");
console.log("Modelo: " + coche.modelo + ".");
console.log("Color: " + coche.color + ".");
console.log("Ruedas: " + coche.numRuedas + ".");
console.log("Puertas: " + coche.numPuertas + ".");
console.log("Precio: $" + coche.precio + ".");
*/

//ARRAY OBJETOS LITERALES
/*
var empleados = [
    {
        nombre: 'Juan',
        apellido: 'Gonzales',
        edad: 40
    },
    {
        nombre: 'Ana',
        apellido: 'Gutierrez',
        edad: 25 
    },
    {
        nombre: 'Fernando',
        apellido: 'Perez',
        edad: 34
    }
]
*/

//SORT
/*
empleados.sort((a, b) => (a.edad - b.edad));
// (a, b) => (a - b) ordena los num de menor a mayor
console.log(empleados);

//IMPRIMIR EN EL HTML
var nombreCompledo = "Gonzalo Hernandez.";
document.write ("El empleado se llama " + nombreCompledo);
*/

//INSERTAR EN UN ALERTA
/*
var miParrafo = document.getElementById('parrafo');
alert(miParrafo.innerHTML);

// inserta la lista en un contenedor
var listaNombres = ['Juan', 'Martin', 'María'];
document.getElementById('caja').innerHTML = listaNombres;
*/

//BUCLE FOR
/*
for (let i = 1; i <= 5; i++){
    console.log(i);
};
*/

//FUNCIONES
/*
function sumar(a, b){
    console.log(a + b);
};

sumar(5, 4);

//FUNCIONES ANÓNIMAS
const saludar = function(nombre) {
    console.log('Hola ' + nombre + "!")
};

saludar('Carlos');

//FUNCIONES FLECHA
const saludar2 = (nombre2) => {
    console.log('Hola ' + nombre2 + "!")
};

saludar2('María');
*/


// CLOSURES
/*
function contador() {
    let cuenta = 0;

    function incrementar() {
        cuenta++; // Se incrementa en 1
        console.log(cuenta); // devuelve por consola
    }

    return incrementar;
}

const contador1 = contador();
contador1();
contador1();
contador1();
contador1();
contador1();


//FUNCION PASA COMO ARGUMENTO
function ejecutarFuncion(func) {
    func(); // saludar();
}

function saludar3() {
    console.log('Hola!');
}

ejecutarFuncion(saludar3);

//DEVOLVER FUNCIONES COMO VALORES
function crearFuncion() {
    return function() {
        console.log("Función devuelta");
    };
}

const miFuncion = crearFuncion();
miFuncion();
*/

//RECURSIVIDAD
/*
function factorial(n) {
    if (n === 0) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

console.log(factorial(5)); // devuelve 120

/* n = 5 -> 5 * factorial(5 - 1)
n = 4 -> 4 * factorial(4 - 1)
n = 3 -> 3 * factorial(3 - 1)
n = 2 -> 2 * factorial(2 - 1)
n = 1 -> 1 * factorial(1 - 1)
n = 0 -> 1

1 * 1 = 1
2 * 1 = 2
3 * 2 = 6
4 * 6 = 24
5 * 24 = 120 */
/*

/*--------------------------------------------------------*/

//EJERCICIO 1
/*
var x = 10;
var y = 20;

//Test A (x=21 y=-21)
x = x + x +1;
y = y - y - x;

//Test B (x=6 y=-29)
//x = (x - y) + 4;
//y = 4 + (y + 5);

//Test C (x=16 y=36)
//x = x * 2 - 4;
//y = 4 - y * 2;

console.log("El valor de x: " + x);
console.log("El valor de y: " + y);
*/

//EJERCICIO 2
/*
var articulo = prompt("Nombre del artículo"); // variable global
var precio = parseInt(prompt("Precio del artículo")); // variable global

producto();

function producto() {
    var iva = 1.21; // variable local
    precioConIva = precio * iva; // variable global
    var mensaje = "El artículo " + articulo + " cuesta $ " + precio + " (IVA no incluido)"; // variable local

    console.log(mensaje);
}

console.log("El precio con IVA incluido es de: " + precioConIva.toFixed(2));
*/

//EJERCICIO 3
/*
//Crear un array para guardar los nombres de los días de la semana, empezando por 0 para el domingo.
//Para comprobar el funcionamiento, pide al usuario un número entre 0 y 6 y devuelve el nombre del día.

let dias = ['domingo', 'lunes','martes', 'miércoles', 'jueves', 'viernes', 'sábado'];

let pregunta = parseInt(prompt("Digite un numero entre 0 y 6"));

if(pregunta >= 0 && pregunta <= 6){
 
    console.log('Hoy es ' + dias[pregunta] + '.')     

} else {

    console.log("Numero fuera del limite")

}
*/

//EJERCICIO 4
/*
//Generar 4 botones y escribir 1 sola función. 
//Cada botón hace referencia a un color diferente.
//Al hacer click en cada botón imprimir por consola: El color es:

var boton = document.querySelectorAll('button');

for(var i = 0; i < boton.length; i++) {

boton[i].onclick = function() {

    console.log('El color es: ' + this.innerHTML);
};

}
*/
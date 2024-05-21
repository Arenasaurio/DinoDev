use std::io;
/*
:: Se usa para funciones asociadas, constantes y constructores, 
mientras que . se usa para métodos y campos de una instancia. 
*/
// Es buena practica para rust declarar o sugerir el tipo de datos al compilador de rust
fn main() {
    let mut equisde: String = String::new();
    //String::new() es para poner una cadena de texto después
    //en rust es beneficioso el almacenar los propios metodos dentro de las variables
    let stdin: io::Stdin = io::stdin();
    //para evitar llamarla despues
    println!("Dime tu nombre: ");
    stdin.read_line(&mut equisde).expect("A ochoa lo mataron a balazos");
    //es un puntero hacia los caracteres que vamos llevando al string, y pues debe ser mutable
    println!("Eres una caca {}, porque te burlas de tu hermano el Luis", equisde);
    //tambien se pueden mandar cadenas sin caracteres a la cadena y no da error

    //ahora leeremos numeros
    let mut numba: String = String::new();
    println!("Dame dos números: ");
    stdin.read_line(&mut numba).expect("Valor no aceptado");
    let nmb1: i32 = numba.trim().parse().expect("Error de conversion!");
    stdin.read_line(&mut numba).expect("Valor no aceptado");
    println!("Cadena sin vaciar: <{}>", numba);
    numba.clear(); //se debe vaciar para que no de error la conversion ya que no acepta saltos de linea
    stdin.read_line(&mut numba).expect("Valor no aceptado");
    //let nmb2: i64 = numba.trim().parse().expect("Error de conversion!");
    //let res: i32 = nmb + 5;
    //let res: i32 = nmb1 +nmb2; no se puede añadir un valor de diferente tamaño con otro
    //let res: i64 = nmb1 +nmb2;
    let nmb2: i32 = numba.trim().parse().expect("Error de conversion!");
    let res: i32 = nmb2+nmb1;
    if nmb2 < 0{
        println!("{} {} = {}", nmb1, nmb2, res);
    }else{
        println!("{} + {} = {}", nmb1, nmb2, res);
    }
    println!("Aprieta enter para salir...");
    stdin.read_line(&mut numba).expect("Valor no aceptado");
}

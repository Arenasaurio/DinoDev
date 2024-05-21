//mi dulce y preciosa niña, flor blanca nacida de la primavera solo tengo ojos para ti, por favor no te alejes más alla de lo
//que puedo verte, desearía que te apoyases más en mi de ser necesario.

fn combinaciones(n: usize, p: usize) -> usize{
    let mut t=vec![vec![0; p+1]; n+1];

    for i in 0..=n{
        for j in 0..=p{
            if j == 0 || j==i{
                t[i][j] = 1;
            }else if j > i{
                t[i][j] = 0;
            }else{
                t[i][j] = t[i-1][j-1] + t[i-1][j];
            }
        }
    }

    t[n][p]
}

fn main(){
    let n = 5;
    let r = 3;
    println!("La combinatoria de {} sobre {} es: {}", n, r, combinaciones(n, r));
}
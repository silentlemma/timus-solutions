use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<i64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let (a, b, c, d) = match v[..] {
        [a, b, c, d] => (a, b, c, d),
        _ => return,
    };
    let (mut petya, mut driver) = (a, c);
    // the driver never asks less than Petya offers, and the other way round
    if petya >= driver {
        println!("{}", petya);
        return;
    }
    loop {
        petya += b;
        if petya >= driver {
            println!("{}", driver);
            return;
        }
        driver -= d;
        if driver <= petya {
            println!("{}", petya);
            return;
        }
    }
}

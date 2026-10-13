use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace().map(|x| x.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (ar, ai, br, bi) = (next(), next(), next(), next());
    let norm = br * br + bi * bi;
    if norm == 0 {
        println!("0"); // no remainder is shorter than zero
        return;
    }
    // a / b = (x + y i) / norm; every quotient q lies within 1 of it
    let (x, y) = (ar * br + ai * bi, ai * br - ar * bi);
    let (fx, fy) = (x.div_euclid(norm), y.div_euclid(norm));
    let mut count = 0;
    for qr in fx - 1..=fx + 1 {
        for qi in fy - 1..=fy + 1 {
            let (rr, ri) = (ar - (br * qr - bi * qi), ai - (br * qi + bi * qr));
            if rr * rr + ri * ri < norm {
                count += 1;
            }
        }
    }
    println!("{}", count);
}

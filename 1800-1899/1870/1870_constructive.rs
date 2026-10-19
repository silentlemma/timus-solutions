use std::io::{self, Read, Write};

// 2 * 3: both must be invertible modulo n
const BAD: usize = 6;

fn gcd(a: usize, b: usize) -> usize {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    if gcd(n, BAD) != 1 {
        println!("No");
        return;
    }
    // queen i on row 2i: rows 2i, diagonals 3i and anti-diagonals i are all
    // different modulo n
    let rows: Vec<String> = (0..n).map(|i| (2 * i % n + 1).to_string()).collect();
    let out = format!("Yes\n{}\n", rows.join(" "));
    io::stdout().write_all(out.as_bytes()).unwrap();
}

use std::io::{self, Read};

const STEP: usize = 5; // four characters of a pigeon and a separating column

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let top = it.next().unwrap().as_bytes();
    // halves counts the pigeons that break the pattern with the left half looking
    // left, parity those that break the pattern with even positions looking left,
    // and the two opposite patterns break exactly at the other pigeons
    let (mut halves, mut parity) = (0, 0);
    for i in 0..n {
        let left = top[i * STEP] == b'<';
        if left != (i < n / 2) {
            halves += 1;
        }
        if left != (i % 2 == 0) {
            parity += 1;
        }
    }
    println!("{}", halves.min(n - halves).min(parity).min(n - parity));
}

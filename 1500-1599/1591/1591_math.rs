use std::io::{self, Read};

const FOUR: u64 = 4; // one corner inside: 4 points, one triangle on each side
const FIVE: u64 = 5; // two corners inside: 5 points, one triangle per apex
const SIX: u64 = 6; // three corners inside: 6 points, the three long diagonals

fn choose(n: u64, k: u64) -> u64 {
    // stays below C(n, k) * n
    (1..=k).fold(1, |c, i| c * (n - k + i) / i)
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let n: u64 = match s.trim().parse() {
        Ok(v) => v,
        Err(_) => return,
    };
    // a triangle is fixed by the set of chord ends it uses, and a set of
    // k points on the circle gives a fixed number of triangles
    println!(
        "{}",
        choose(n, SIX) + FIVE * choose(n, FIVE) + FOUR * choose(n, FOUR)
    );
}

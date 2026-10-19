use std::io::{self, Read};

const LETTERS: usize = 100000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let mut read_counts = || {
        let length = it.next().unwrap();
        let mut count = vec![0i64; LETTERS + 1];
        for _ in 0..length {
            count[it.next().unwrap()] += 1;
        }
        (length as i64, count)
    };
    let (n, mut a) = read_counts();
    let (m, mut b) = read_counts();
    // every position of t meets every position of the cyclic s exactly once,
    // so the distance is n m minus the number of equal pairs
    let (p, q) = (a[0], b[0]);
    a[0] = 0;
    b[0] = 0;
    let equal: i64 = a.iter().zip(&b).map(|(x, y)| x * y).sum();
    // the gain is linear in the letters chosen for the question marks of one
    // string, so all of them take one letter: the same letter for both
    // strings, or the best letter for each
    let same = a.iter().zip(&b).map(|(x, y)| p * y + q * x).max().unwrap() + p * q;
    let apart = p * b.iter().max().unwrap() + q * a.iter().max().unwrap();
    println!("{}", n * m - equal - same.max(apart));
}

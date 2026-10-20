use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let mut a: Vec<i64> = it.by_ref().take(n).collect();
    let mut b: Vec<i64> = it.by_ref().take(n).collect();
    let p = it.next().unwrap();
    a.sort_unstable();
    b.sort_unstable();
    // The i-th weakest student can take any of the problems they can solve,
    // except the i problems already taken by weaker students.
    let mut ways = 1 % p;
    let mut solvable = 0;
    for (i, &knowledge) in a.iter().enumerate() {
        while solvable < n && b[solvable] <= knowledge {
            solvable += 1;
        }
        ways = ways * ((solvable as i64 - i as i64) % p) % p;
    }
    println!("{}", ways);
}

use std::fmt::Write as _;
use std::io::{self, Read};

const PERIOD: usize = 6; // the simple pattern fails exactly when n mod 6 is 2

// the row of the queen in each column 1 ... n for even n; the main
// diagonal stays free
fn even_rows(n: usize) -> Vec<usize> {
    let half = n / 2;
    let mut rows = vec![0; n];
    for i in 1..=half {
        if n % PERIOD != 2 {
            // the even rows in the left half, the odd rows in the right half
            rows[i - 1] = 2 * i;
            rows[half + i - 1] = 2 * i - 1;
        } else {
            let shift = (2 * (i - 1) + half - 1) % n;
            rows[i - 1] = 1 + shift;
            rows[n - i] = n - shift;
        }
    }
    rows
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // an odd board is an even one plus the free corner (n, n)
    let mut rows = even_rows(n - n % 2);
    if n % 2 == 1 {
        rows.push(n);
    }
    let mut out = String::new();
    for (col, row) in rows.iter().enumerate() {
        writeln!(out, "{} {}", col + 1, row).unwrap();
    }
    print!("{}", out);
}

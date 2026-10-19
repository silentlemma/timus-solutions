use std::io::{self, Read};

const DIGITS: [&str; 10] = [
    "._.|.||_|", ".....|..|", "._.._||_.", "._.._|._|", "...|_|..|",
    "._.|_.._|", "._.|_.|_|", "._...|..|", "._.|_||_|", "._.|_|._|",
];
const COLUMNS: [usize; 4] = [0, 4, 10, 14]; // where the four digits start
const WIDTH: usize = 3;
const SECONDS: usize = 60; // MM:SS runs from 00:00 to 59:59

// every lit segment must belong to the digit
fn fits(shown: &[u8], digit: usize) -> bool {
    shown.iter().zip(DIGITS[digit].bytes()).all(|(&c, d)| c == b'.' || c == d)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut out = String::new();
    let mut previous = SECONDS * SECONDS;
    for _ in 0..n {
        let rows: Vec<&[u8]> = (0..WIDTH).map(|_| words.next().unwrap().as_bytes()).collect();
        let ok: Vec<Vec<bool>> = COLUMNS
            .iter()
            .map(|&c| {
                let cell: Vec<u8> =
                    rows.iter().flat_map(|row| row[c..c + WIDTH].iter().copied()).collect();
                (0..10).map(|d| fits(&cell, d)).collect()
            })
            .collect();
        // the largest time that fits and stays below the previous one leaves the
        // most room for the rest, so it never spoils a solution
        let mut value = previous - 1;
        loop {
            let (m, s) = (value / SECONDS, value % SECONDS);
            let digits = [m / 10, m % 10, s / 10, s % 10];
            if digits.iter().enumerate().all(|(k, &d)| ok[k][d]) {
                out.push_str(&format!("{:02}:{:02}\n", m, s));
                break;
            }
            value -= 1;
        }
        previous = value;
    }
    print!("{}", out);
}

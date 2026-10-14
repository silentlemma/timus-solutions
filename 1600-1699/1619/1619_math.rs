use std::fmt::Write as _;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<u64>().unwrap());
    let t = words.next().unwrap();
    let mut out = String::new();
    for _ in 0..t {
        let (k, m) = (words.next().unwrap(), words.next().unwrap());
        // the ballot theorem: the elder stays ahead or level with this chance
        if m > k {
            out.push_str("0\n");
        } else {
            writeln!(out, "{:.10}", (k - m + 1) as f64 / (k + 1) as f64).unwrap();
        }
    }
    print!("{}", out);
}

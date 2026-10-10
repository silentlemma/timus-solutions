use std::collections::VecDeque;
use std::fmt::Write;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let m = tok.next().unwrap() as usize;
    let values: Vec<i64> = tok.take_while(|&v| v >= 0).collect();
    // indices of the window whose values decrease from front to back: the
    // front is the maximum, and a value never matters once a later one is larger
    let mut window: VecDeque<usize> = VecDeque::new();
    let mut out = String::new();
    for (i, &v) in values.iter().enumerate() {
        while window.back().map_or(false, |&b| values[b] <= v) {
            window.pop_back();
        }
        window.push_back(i);
        if window[0] + m <= i {
            window.pop_front();
        }
        if i + 1 >= m {
            writeln!(out, "{}", values[window[0]]).unwrap();
        }
    }
    print!("{}", out);
}

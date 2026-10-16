use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut point = || (words.next().unwrap(), words.next().unwrap());
    let (a, b, c, d) = (point(), point(), point(), point());
    // both walks stay in the boxes of their ends, so the shared part lies in
    // the overlap of the two boxes
    let overlap = |p: i64, q: i64, r: i64, s: i64| p.max(q).min(r.max(s)) - p.min(q).max(r.min(s));
    let width = overlap(a.0, b.0, c.0, d.0);
    let height = overlap(a.1, b.1, c.1, d.1);
    if width < 0 || height < 0 {
        println!("0");
        return;
    }
    // walks rising the same way can share a staircase across the overlap, while
    // one rising and one falling share only one straight piece
    let first = (b.0 - a.0).signum() * (b.1 - a.1).signum();
    let second = (d.0 - c.0).signum() * (d.1 - c.1).signum();
    let answer = if first * second < 0 { width.max(height) } else { width + height };
    println!("{}", answer);
}

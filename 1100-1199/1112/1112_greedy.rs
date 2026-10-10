use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let n = tok.next().unwrap() as usize;
    let mut segs: Vec<(i32, i32)> = (0..n)
        .map(|_| (tok.next().unwrap(), tok.next().unwrap()))
        .collect();
    // the segment that ends first leaves the most room for the rest; touching
    // ends share no inner point
    segs.sort_by_key(|s| s.1);
    let mut chosen: Vec<(i32, i32)> = Vec::new();
    for s in segs {
        if chosen.last().map_or(true, |c| s.0 >= c.1) {
            chosen.push(s);
        }
    }
    let mut out = format!("{}\n", chosen.len());
    for (a, b) in chosen {
        out.push_str(&format!("{} {}\n", a, b));
    }
    print!("{}", out);
}

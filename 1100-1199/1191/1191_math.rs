use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i32> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let mut gap = v[0];
    // at a stop with trams every k minutes the officer, arriving gap
    // minutes after the thief, leaves at best gap - gap % k minutes later,
    // and a gap below k means the thief may still be waiting there
    for &k in &v[2..] {
        gap -= gap % k;
        if gap == 0 {
            println!("YES");
            return;
        }
    }
    println!("NO");
}

use std::io::{self, Read};

const TARGET: i32 = 10000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i32>().unwrap());
    let mut read_list = || {
        let n = it.next().unwrap() as usize;
        (0..n).map(|_| it.next().unwrap()).collect::<Vec<i32>>()
    };
    let up = read_list();
    let down = read_list();
    // up increases and down decreases: walking both forward, a sum that is
    // too small can only grow by moving in up, a sum too big only shrink in down
    let (mut i, mut j) = (0, 0);
    while i < up.len() && j < down.len() && up[i] + down[j] != TARGET {
        if up[i] + down[j] < TARGET {
            i += 1;
        } else {
            j += 1;
        }
    }
    let found = i < up.len() && j < down.len();
    println!("{}", if found { "YES" } else { "NO" });
}

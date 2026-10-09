use std::io::{self, Read};
use std::mem::swap;

// the disks start on the source rod and go to the target rod
const SOURCE: usize = 1;
const TARGET: usize = 2;
const SPARE: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0];
    let rod = &v[1..=n];
    // disks 1..k are being moved from a to b over c; disk k moves once, in the
    // middle: before it the others go to c, after it they go from c to b
    let (mut a, mut b, mut c) = (SOURCE, TARGET, SPARE);
    let mut steps: i64 = 0;
    for k in (1..=n).rev() {
        if rod[k - 1] == a {
            swap(&mut b, &mut c);
        } else if rod[k - 1] == b {
            steps += 1 << (k - 1);
            swap(&mut a, &mut c);
        } else {
            steps = -1;
            break;
        }
    }
    println!("{}", steps);
}

use std::io::{self, Read};

const LETTERS: usize = 26;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let _m: usize = it.next().unwrap().parse().unwrap();
    let p: usize = it.next().unwrap().parse().unwrap();
    // the words take their letters out of the grid one cell each, so what is
    // left does not depend on where they lie
    let mut left = [0i32; LETTERS];
    for _ in 0..n {
        for c in it.next().unwrap().bytes() {
            left[(c - b'A') as usize] += 1;
        }
    }
    for _ in 0..p {
        for c in it.next().unwrap().bytes() {
            left[(c - b'A') as usize] -= 1;
        }
    }
    let answer: String = (0..LETTERS)
        .flat_map(|c| std::iter::repeat((b'A' + c as u8) as char).take(left[c] as usize))
        .collect();
    println!("{}", answer);
}

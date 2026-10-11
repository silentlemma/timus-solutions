use std::io;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    // a row ends in white or red; it comes from a row one shorter ending in
    // the other of the two, or from one two shorter followed by blue
    let (mut prev, mut cur) = (2u64, 2u64);
    for _ in 2..n.max(2) {
        (prev, cur) = (cur, prev + cur);
    }
    println!("{}", cur);
}

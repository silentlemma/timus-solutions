use std::io::{self, Read};

const END: i64 = 1_000_000_000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut paints = Vec::with_capacity(n);
    let mut xs = vec![0, END];
    for _ in 0..n {
        let a: i64 = tokens.next().unwrap().parse().unwrap();
        let b: i64 = tokens.next().unwrap().parse().unwrap();
        let c = tokens.next().unwrap().as_bytes()[0];
        paints.push((a, b, c));
        xs.push(a);
        xs.push(b);
    }
    xs.sort_unstable();
    xs.dedup();
    let index = |x: i64| xs.binary_search(&x).unwrap();

    // piece i is [xs[i], xs[i + 1]); repaint the pieces of every segment
    let mut piece = vec![b'w'; xs.len() - 1];
    for &(a, b, c) in &paints {
        piece[index(a)..index(b)].fill(c);
    }

    // the longest run of white pieces; a strict comparison keeps the leftmost
    let (mut best_x, mut best_y) = (0, 0);
    let mut i = 0;
    while i < piece.len() {
        let mut j = i;
        while j < piece.len() && piece[j] == piece[i] {
            j += 1;
        }
        if piece[i] == b'w' && xs[j] - xs[i] > best_y - best_x {
            best_x = xs[i];
            best_y = xs[j];
        }
        i = j;
    }
    println!("{} {}", best_x, best_y);
}

use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let points: Vec<(i32, i32)> = (0..n)
        .map(|_| {
            (
                tokens.next().unwrap().parse().unwrap(),
                tokens.next().unwrap().parse().unwrap(),
            )
        })
        .collect();
    let mut best = 2;
    // Every line through two input points is tried; cross products are exact.
    for i in 0..n {
        for j in i + 1..n {
            let (dx, dy) = (points[j].0 - points[i].0, points[j].1 - points[i].1);
            let count = points
                .iter()
                .filter(|&&(x, y)| (x - points[i].0) * dy == (y - points[i].1) * dx)
                .count();
            best = best.max(count);
            if best == n {
                println!("{}", best);
                return;
            }
        }
    }
    println!("{}", best);
}

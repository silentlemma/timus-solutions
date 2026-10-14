use std::io::{self, Read};

const MACHINES: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let n = v[0] as usize;
    let toys: Vec<&[i64]> = v[1..].chunks(MACHINES).take(n).collect();
    // machine B never holds the line, so the line behaves like two machines
    // with times a + b and b + c, where Johnson's rule is optimal: toys
    // faster on the first come first, by its time, the rest by the second
    let first = |i: usize| toys[i][0] + toys[i][1];
    let second = |i: usize| toys[i][1] + toys[i][2];
    let (mut early, mut late): (Vec<usize>, Vec<usize>) =
        (0..n).partition(|&i| first(i) < second(i));
    early.sort_by_key(|&i| first(i));
    late.sort_by_key(|&i| std::cmp::Reverse(second(i)));
    early.extend(late);
    let (mut done_a, mut done_b, mut done_c) = (0i64, 0i64, 0i64);
    for &i in &early {
        done_a += toys[i][0];
        done_b = done_b.max(done_a) + toys[i][1];
        done_c = done_c.max(done_b) + toys[i][2];
    }
    let order: Vec<String> = early.iter().map(|i| (i + 1).to_string()).collect();
    println!("{}\n{}", done_c, order.join(" "));
}

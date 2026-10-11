use std::io;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let v: Vec<i64> = line
        .split_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (mut x, mut y) = (v[0], v[1]);
    // each turn of the loop swaps x and y, and there are x + y turns; the
    // sum survives, so an odd sum of positive numbers means one swap
    if x > 0 && y > 0 && (x + y) % 2 == 1 {
        std::mem::swap(&mut x, &mut y);
    }
    println!("{} {}", x, y);
}

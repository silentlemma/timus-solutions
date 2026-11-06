use std::io;

const BASE: usize = 10;

fn choose(n: usize, k: usize) -> i64 {
    (1..=k).fold(1, |product, i| product * (n - i + 1) as i64 / i as i64)
}

fn equal_sums(size: usize) -> i64 {
    if size == 0 {
        return 1;
    }
    let target = (BASE - 1) * size;
    let variables = 2 * size;
    let mut count = 0;
    // Complement one group of digits, then exclude entries outside 0..=9.
    for excluded in 0..=target / BASE {
        let remaining = target - excluded * BASE;
        let ways = choose(variables, excluded) * choose(remaining + variables - 1, variables - 1);
        if excluded % 2 == 0 {
            count += ways;
        } else {
            count -= ways;
        }
    }
    count
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    let half = n / 2;
    println!("{}", equal_sums(half / 2) * equal_sums((half + 1) / 2));
}

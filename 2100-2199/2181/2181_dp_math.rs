use std::io::{self, Read};

const MODULUS: i64 = 1_000_000_007;

fn count_paths(
    n: usize,
    m: usize,
    down: &[bool],
    right: &[bool],
    source_row: usize,
    source_column: usize,
) -> (i64, i64) {
    let mut dp = vec![0_i64; m];
    let mut upper = 0;
    let mut lower = 0;
    for row in 0..n {
        for column in 0..m {
            let index = row * m + column;
            let mut value = 0;
            if row == source_row && column == source_column {
                value = 1;
            } else {
                if row > 0 && !down[index - m] {
                    value = dp[column];
                }
                if column > 0 && !right[index - 1] {
                    value += dp[column - 1];
                }
                if value >= MODULUS {
                    value -= MODULUS;
                }
            }
            dp[column] = value;
            if row == n - 2 && column == m - 1 {
                upper = value;
            }
            if row == n - 1 && column == m - 2 {
                lower = value;
            }
        }
    }
    (upper, lower)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|value| value.parse::<usize>().unwrap());
    let n = values.next().unwrap();
    let m = values.next().unwrap();
    let missing = values.next().unwrap();
    let mut down = vec![false; n * m];
    let mut right = vec![false; n * m];
    for _ in 0..missing {
        let a = values.next().unwrap() - 1;
        let b = values.next().unwrap() - 1;
        let c = values.next().unwrap() - 1;
        let d = values.next().unwrap() - 1;
        if a == c {
            right[a * m + b.min(d)] = true;
        } else {
            down[a.min(c) * m + b] = true;
        }
    }
    if right[0] || down[0] || down[(n - 2) * m + m - 1] || right[(n - 1) * m + m - 2] {
        println!("0");
        return;
    }

    let upper = count_paths(n, m, &down, &right, 0, 1);
    let lower = count_paths(n, m, &down, &right, 1, 0);
    // Swapping tails cancels every pair that shares an internal vertex.
    let mut answer = (upper.0 * lower.1 - upper.1 * lower.0) % MODULUS;
    answer = (answer + MODULUS) % MODULUS;
    println!("{}", answer * 2 % MODULUS);
}

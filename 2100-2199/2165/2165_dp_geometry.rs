use std::io::{self, Read};

const COORDINATE_LIMIT: i64 = 100_000_000;
const AREA_BOUND_FACTOR: i64 = 8;
const INFINITY: i64 = AREA_BOUND_FACTOR * COORDINATE_LIMIT * COORDINATE_LIMIT;
const WHOLE_SUFFIX: &str = ".0";
const HALF_SUFFIX: &str = ".5";

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut x = Vec::with_capacity(n);
    let mut y = Vec::with_capacity(n);
    for _ in 0..n {
        x.push(tokens.next().unwrap().parse::<i64>().unwrap());
        y.push(tokens.next().unwrap().parse::<i64>().unwrap());
    }

    let mut dp = vec![vec![0; n]; n];
    for i in 0..n - 1 {
        dp[i][i + 1] = INFINITY;
    }
    for width in 2..n {
        for left in 0..n - width {
            let right = left + width;
            let mut best = 0;
            let dx = x[right] - x[left];
            let dy = y[right] - y[left];
            for middle in left + 1..right {
                let mut candidate = dp[left][middle].min(dp[middle][right]);
                if candidate <= best {
                    continue;
                }
                let area = (x[middle] - x[left]) * dy - (y[middle] - y[left]) * dx;
                candidate = candidate.min(area);
                best = best.max(candidate);
            }
            dp[left][right] = best;
        }
    }
    let answer = dp[0][n - 1];
    let suffix = if answer % 2 == 0 {
        WHOLE_SUFFIX
    } else {
        HALF_SUFFIX
    };
    println!("{}{}", answer / 2, suffix);
}

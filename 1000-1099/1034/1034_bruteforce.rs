use std::io::{self, Read};

const MOVED: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    // col[r] is the column of the queen in row r; sum[r + c] and diff[r + n - c]
    // count the queens on each diagonal
    let mut col = vec![0; n];
    for _ in 0..n {
        let x = it.next().unwrap();
        col[x - 1] = it.next().unwrap() - 1;
    }
    let mut sum = vec![0; 2 * n];
    let mut diff = vec![0; 2 * n];
    for r in 0..n {
        sum[r + col[r]] += 1;
        diff[r + n - col[r]] += 1;
    }
    let mut count = 0u64;
    for a in 0..n {
        for b in a + 1..n {
            for c in b + 1..n {
                let rows = [a, b, c];
                for &r in &rows {
                    sum[r + col[r]] -= 1;
                    diff[r + n - col[r]] -= 1;
                }
                // all three queens move only when the columns are shifted cyclically
                for shift in 1..MOVED {
                    let mut placed = 0;
                    while placed < MOVED {
                        let (r, cl) = (rows[placed], col[rows[(placed + shift) % MOVED]]);
                        if sum[r + cl] > 0 || diff[r + n - cl] > 0 {
                            break;
                        }
                        sum[r + cl] += 1;
                        diff[r + n - cl] += 1;
                        placed += 1;
                    }
                    if placed == MOVED {
                        count += 1;
                    }
                    for k in 0..placed {
                        let (r, cl) = (rows[k], col[rows[(k + shift) % MOVED]]);
                        sum[r + cl] -= 1;
                        diff[r + n - cl] -= 1;
                    }
                }
                for &r in &rows {
                    sum[r + col[r]] += 1;
                    diff[r + n - col[r]] += 1;
                }
            }
        }
    }
    println!("{}", count);
}

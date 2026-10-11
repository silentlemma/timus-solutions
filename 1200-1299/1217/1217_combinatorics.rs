use std::io;

const DIGITS: usize = 10;

// ways[s]: strings of k digits with digit sum s
fn sums(k: usize) -> Vec<i64> {
    let mut ways = vec![1i64];
    for _ in 0..k {
        let mut next = vec![0i64; ways.len() + DIGITS - 1];
        for (s, &w) in ways.iter().enumerate() {
            for d in 0..DIGITS {
                next[s + d] += w;
            }
        }
        ways = next;
    }
    ways
}

// pairs of a k-digit and an m-digit string with equal digit sums
fn matching(k: usize, m: usize) -> i64 {
    sums(k).iter().zip(sums(m).iter()).map(|(a, b)| a * b).sum()
}

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let n: usize = line.trim().parse().unwrap();
    // size[in the first half][odd] counts positions; lucky both ways means the
    // odd digits of the first half sum like the even ones of the second half,
    // and the even digits of the first half like the odd ones of the second
    let mut size = [[0usize; 2]; 2];
    for p in 1..=n {
        size[(p <= n / 2) as usize][p % 2] += 1;
    }
    println!(
        "{}",
        matching(size[1][1], size[0][0]) * matching(size[1][0], size[0][1])
    );
}

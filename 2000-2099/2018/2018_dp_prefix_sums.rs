use std::io;

const MOD: i64 = 1_000_000_007;

fn main() {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    let v: Vec<usize> = line
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (n, a, b) = (v[0], v[1], v[2]);
    // one[i], two[i]: sequences of length i that end with a run of ones or twos,
    // the empty sequence counts once on both sides, so one[0] = two[0] = 1
    let mut one = vec![0i64; n + 1];
    let mut two = vec![0i64; n + 1];
    let mut sum_one = vec![0i64; n + 1];
    let mut sum_two = vec![0i64; n + 1];
    one[0] = 1;
    two[0] = 1;
    sum_one[0] = 1;
    sum_two[0] = 1;
    for i in 1..=n {
        // the last run of ones has length 1..a and follows a sequence ending in twos
        one[i] = sum_two[i - 1] - if i > a { sum_two[i - a - 1] } else { 0 };
        two[i] = sum_one[i - 1] - if i > b { sum_one[i - b - 1] } else { 0 };
        one[i] = one[i].rem_euclid(MOD);
        two[i] = two[i].rem_euclid(MOD);
        sum_one[i] = (sum_one[i - 1] + one[i]) % MOD;
        sum_two[i] = (sum_two[i - 1] + two[i]) % MOD;
    }
    println!("{}", (one[n] + two[n]) % MOD);
}

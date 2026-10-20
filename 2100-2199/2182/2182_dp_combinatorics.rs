use std::io::{self, Read};

const SMALL: u64 = 60; // only boxes up to the number of bits can receive extra bottles

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<u64>().unwrap());
    let n = it.next().unwrap() as usize;
    let q = it.next().unwrap() as usize;
    let mut binom = vec![vec![0u64; n + 1]; n + 1];
    for i in 0..=n {
        binom[i][0] = 1;
        for j in 1..=i {
            binom[i][j] = binom[i - 1][j - 1] + binom[i - 1][j];
        }
    }
    let top = (1u64 << n) - 1;
    let last = top.min(SMALL) as usize;
    // Box k gets one bottle for every bottle placed in a box j != k with
    // popcount(j) = k; boxes above 60 hold only their own one, and the small
    // boxes are filled from the top down, as popcount(j) < j for j > 1.
    let mut count = vec![1u64; last + 1];
    for k in (1..=last).rev() {
        let wanted = if k <= n { binom[n][k] } else { 0 };
        let mut total = 1 + wanted - u64::from(k == 1);
        for j in k + 1..=last {
            if j.count_ones() as usize == k {
                total += count[j] - 1;
            }
        }
        count[k] = total;
    }
    let answers: Vec<String> = it
        .take(q)
        .map(|a| if a <= last as u64 { count[a as usize] } else { 1 }.to_string())
        .collect();
    println!("{}", answers.join(" "));
}

use std::io::{self, Read};

// the sums of all subsets of the weights, sorted
fn subset_sums(weights: &[i32]) -> Vec<i32> {
    let mut sums = Vec::with_capacity(1 << weights.len());
    sums.push(0);
    for &weight in weights {
        let count = sums.len();
        for index in 0..count {
            sums.push(sums[index] + weight);
        }
    }
    sums.sort_unstable();
    sums
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let weights: Vec<i32> = tokens.take(n).map(|s| s.parse().unwrap()).collect();
    let total: i32 = weights.iter().sum();
    let left = subset_sums(&weights[..n / 2]);
    let right = subset_sums(&weights[n / 2..]);
    // a pile is a subset of each half; walk the left sums up and the right sums
    // down, moving the side that brings the pile closer to total / 2
    let mut best = total;
    let mut i = 0;
    let mut j = right.len();
    while i < left.len() && j > 0 {
        let difference = total - 2 * (left[i] + right[j - 1]);
        best = best.min(difference.abs());
        // the difference has the parity of the total, so it cannot be smaller
        if best == total % 2 {
            break;
        }
        if difference > 0 {
            i += 1;
        } else {
            j -= 1;
        }
    }
    println!("{}", best);
}

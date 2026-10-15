use std::io::{self, Read};

const INF: usize = usize::MAX;
const TOP: usize = 10000; // the largest vertex number

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let n = nums[0];
    let chain = &nums[1..=n];
    let end = chain[n - 1];
    if chain[0] == end {
        println!("{}", end);
        return;
    }
    // dp[i]: fewest edges from position i to the final vertex, taking only
    // edges of p from i on; reaching the final vertex anywhere ends it
    let mut dp = vec![INF; n];
    let mut step = vec![0; n];
    // per vertex: the best dp after leaving it and where, latest on ties
    let mut best_value = vec![INF; TOP + 1];
    let mut best_at = vec![0; TOP + 1];
    dp[n - 1] = 0;
    for i in (0..n - 1).rev() {
        let u = chain[i];
        if dp[i + 1] < best_value[u] {
            best_value[u] = dp[i + 1];
            best_at[u] = i + 1;
        }
        if u == end {
            dp[i] = 0;
        } else if best_value[u] < INF {
            dp[i] = best_value[u] + 1;
            step[i] = best_at[u];
        }
    }
    let mut path = vec![chain[0].to_string()];
    let mut i = 0;
    while chain[i] != end {
        i = step[i];
        path.push(chain[i].to_string());
    }
    println!("{}", path.join(" "));
}

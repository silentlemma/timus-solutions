use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let s = text.trim().as_bytes();
    let n = s.len();
    // dp[j]: fewest palindromes for the prefix of length j. Centres go left
    // to right, so every palindrome s[l..r] meets a final dp[l]: those that
    // end before l have their centres before l.
    let mut dp = vec![n + 1; n + 1];
    let mut prev = vec![0; n + 1];
    dp[0] = 0;
    for twice in 0..2 * n - 1 {
        let (mut l, mut r) = (twice / 2, twice / 2 + twice % 2);
        while r < n && s[l] == s[r] {
            if dp[l] + 1 < dp[r + 1] {
                dp[r + 1] = dp[l] + 1;
                prev[r + 1] = l;
            }
            if l == 0 {
                break;
            }
            l -= 1;
            r += 1;
        }
    }
    let mut parts = Vec::new();
    let mut end = n;
    while end > 0 {
        parts.push(std::str::from_utf8(&s[prev[end]..end]).unwrap());
        end = prev[end];
    }
    parts.reverse();
    println!("{}\n{}", dp[n], parts.join(" "));
}

use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let (n, m) = (tok.next().unwrap(), tok.next().unwrap());
    let mut count = vec![0; n + 1];
    for x in tok.take(m) {
        count[x] += 1;
    }
    // card k shows k - 1 and k, so the number x fits cards x and x + 1; going
    // up from the smallest number, card x is useless to anything later, so it
    // is taken first
    let mut used = vec![false; n + 2];
    for x in 0..=n {
        for card in x..=x + 1 {
            if count[x] > 0 && (1..=n).contains(&card) && !used[card] {
                used[card] = true;
                count[x] -= 1;
            }
        }
        if count[x] > 0 {
            println!("NO");
            return;
        }
    }
    println!("YES");
}

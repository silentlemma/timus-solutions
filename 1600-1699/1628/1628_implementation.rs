use std::collections::HashSet;
use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut nums = text.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let mut next = || nums.next().unwrap();
    let (m, n, k) = (next(), next(), next());
    let mut black = HashSet::new();
    let mut rows = vec![Vec::new(); m + 2];
    let mut cols = vec![Vec::new(); n + 2];
    for _ in 0..k {
        let (x, y) = (next(), next());
        black.insert((x, y));
        rows[x].push(y);
        cols[y].push(x);
    }
    let closed = |x: usize, y: usize| x < 1 || x > m || y < 1 || y > n || black.contains(&(x, y));
    let mut count: u64 = 0;
    // A white run of length 2 or more is a strip by itself; a single white
    // cell is one only if it is closed in the other direction too.
    for x in 1..=m {
        let r = &mut rows[x];
        r.sort_unstable();
        r.push(n + 1);
        let mut prev = 0;
        for &b in r.iter() {
            let length = b - prev - 1;
            if length >= 2 || (length == 1 && closed(x - 1, prev + 1) && closed(x + 1, prev + 1)) {
                count += 1;
            }
            prev = b;
        }
    }
    for y in 1..=n {
        let c = &mut cols[y];
        c.sort_unstable();
        c.push(m + 1);
        let mut prev = 0;
        for &b in c.iter() {
            if b - prev - 1 >= 2 {
                count += 1;
            }
            prev = b;
        }
    }
    println!("{}", count);
}

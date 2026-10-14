use std::io::{self, Read};

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let v: Vec<i64> = s
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    if v.is_empty() {
        return;
    }
    let n = v[0] as usize;
    // (y, x, number), sorted from the top of the slope down
    let mut flags: Vec<(i64, i64, usize)> = (0..n)
        .map(|i| (v[2 * i + 2], v[2 * i + 1], i + 1))
        .collect();
    flags.sort_unstable_by(|a, b| b.cmp(a));
    // down the slope the x coordinates must zigzag; the longest zigzag keeps
    // the first flag, the last one of every run in one direction, and the end
    let mut path = vec![flags[0].2.to_string()];
    for i in 1..n {
        let last = i == n - 1;
        let turns = !last && (flags[i].1 > flags[i - 1].1) != (flags[i + 1].1 > flags[i].1);
        if last || turns {
            path.push(flags[i].2.to_string());
        }
    }
    println!("{}\n{}", path.len(), path.join(" "));
}

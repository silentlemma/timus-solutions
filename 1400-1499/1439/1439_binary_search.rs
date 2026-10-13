use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    it.next();
    let m: usize = it.next().unwrap().parse().unwrap();
    let mut gone: Vec<i64> = Vec::new(); // original numbers of destroyed rooms, sorted
    let mut out = String::new();
    for _ in 0..m {
        let letter = it.next().unwrap();
        let x: i64 = it.next().unwrap().parse().unwrap();
        // gone[j] - j <= x holds for a prefix: the rooms gone below room x
        let lo = {
            let (mut lo, mut hi) = (0usize, gone.len());
            while lo < hi {
                let mid = (lo + hi) / 2;
                if gone[mid] - mid as i64 <= x {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            lo
        };
        let original = x + lo as i64;
        if letter == "D" {
            gone.insert(lo, original);
        } else {
            out.push_str(&original.to_string());
            out.push('\n');
        }
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}

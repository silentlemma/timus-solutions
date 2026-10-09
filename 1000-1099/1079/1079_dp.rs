use std::io::{self, Read};

const TOP: usize = 99999;

fn main() {
    let mut a = vec![0u32; TOP + 1];
    let mut best = vec![0u32; TOP + 1];
    a[1] = 1;
    best[1] = 1;
    for i in 2..=TOP {
        a[i] = if i % 2 == 0 {
            a[i / 2]
        } else {
            a[i / 2] + a[i / 2 + 1]
        };
        best[i] = best[i - 1].max(a[i]);
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut out = String::new();
    for n in input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap())
    {
        if n == 0 {
            break;
        }
        out.push_str(&best[n].to_string());
        out.push('\n');
    }
    print!("{}", out);
}

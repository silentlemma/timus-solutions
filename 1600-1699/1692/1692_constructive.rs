use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let n: usize = text.trim().parse().unwrap();
    // every two flags need a common color, and a color on at most two flags
    // serves one pair only, so k(k - 1) / 2 <= n; one color per pair is enough
    let mut k = 1;
    while (k + 1) * k / 2 <= n {
        k += 1;
    }
    let mut flags = vec![Vec::new(); k];
    let mut color = 0;
    for a in 0..k {
        for b in a + 1..k {
            color += 1;
            flags[a].push(color);
            flags[b].push(color);
        }
    }
    let mut out = format!("{}\n", k);
    for flag in &flags {
        out += &flag.len().to_string();
        for c in flag {
            out += &format!(" {}", c);
        }
        out.push('\n');
    }
    print!("{}", out);
}

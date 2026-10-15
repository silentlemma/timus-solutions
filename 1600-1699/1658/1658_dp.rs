use std::io::{self, Read};

const LONGEST: usize = 100; // digits allowed in the answer
const TOP: usize = 9; // the largest digit
const S1: usize = LONGEST * TOP;
const S2: usize = LONGEST * TOP * TOP;
const NONE: u8 = 255;

fn main() {
    // fewest[s1][s2]: the fewest nonzero digits with these sums, NONE if
    // more than 100 are needed or none will do
    let at = |s1: usize, s2: usize| s1 * (S2 + 1) + s2;
    let mut fewest = vec![NONE; (S1 + 1) * (S2 + 1)];
    fewest[0] = 0;
    for s1 in 1..=S1 {
        for s2 in 1..=S2 {
            let mut best = NONE as usize;
            let mut d = 1;
            while d <= TOP && d <= s1 && d * d <= s2 {
                best = best.min(fewest[at(s1 - d, s2 - d * d)] as usize + 1);
                d += 1;
            }
            if best <= LONGEST {
                fewest[at(s1, s2)] = best as u8;
            }
        }
    }
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let nums: Vec<usize> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut out = String::new();
    for q in nums[1..].chunks(2).take(nums[0]) {
        let (mut s1, mut s2) = (q[0], q[1]);
        if s1 > S1 || s2 > S2 || fewest[at(s1, s2)] == NONE {
            out.push_str("No solution\n");
            continue;
        }
        // the smallest digit first that still leaves a way to finish; the
        // digits come out sorted, so each search starts at the last one
        let mut d = 1;
        for left in (0..fewest[at(s1, s2)] as usize).rev() {
            while d * d > s2 || d > s1 || fewest[at(s1 - d, s2 - d * d)] as usize != left {
                d += 1;
            }
            out.push((b'0' + d as u8) as char);
            s1 -= d;
            s2 -= d * d;
        }
        out.push('\n');
    }
    print!("{}", out);
}

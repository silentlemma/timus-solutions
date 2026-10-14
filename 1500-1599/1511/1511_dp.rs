use std::io::{self, Read};

const BASE: usize = 10;
const INF: usize = usize::MAX;

// digit i of s from the lowest, zero past its length
fn digit(s: &[u8], i: usize) -> usize {
    if i < s.len() {
        (s[s.len() - 1 - i] - b'0') as usize
    } else {
        0
    }
}

// the lowest digit position i may take: the first digit may not become zero
fn least(s: &[u8], i: usize) -> usize {
    (i + 1 == s.len()) as usize
}

// the highest: past its own length a number has only the digit 0
fn most(s: &[u8], i: usize) -> usize {
    if i < s.len() {
        BASE - 1
    } else {
        0
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<&[u8]> = input
        .split_ascii_whitespace()
        .map(|t| t.as_bytes())
        .collect();
    let (a, b, c) = (nums[0], nums[1], nums[2]);
    let width = c.len();
    if a.len().max(b.len()) > width {
        println!("-1"); // the sum would be longer than C
        return;
    }
    // cost[carry]: the cheapest fix of the lower positions that carries this
    let mut cost = [0, INF];
    for i in 0..width {
        let mut next = [INF, INF];
        for carry in 0..2 {
            if cost[carry] == INF {
                continue;
            }
            for x in least(a, i)..=most(a, i) {
                for y in least(b, i)..=most(b, i) {
                    let total = x + y + carry;
                    let z = total % BASE;
                    if z < least(c, i) {
                        continue;
                    }
                    let v = cost[carry]
                        + x.abs_diff(digit(a, i))
                        + y.abs_diff(digit(b, i))
                        + z.abs_diff(digit(c, i));
                    next[total / BASE] = next[total / BASE].min(v);
                }
            }
        }
        cost = next;
    }
    if cost[0] < INF {
        println!("{}", cost[0]);
    } else {
        println!("-1");
    }
}

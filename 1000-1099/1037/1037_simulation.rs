use std::cmp::Reverse;
use std::collections::{BinaryHeap, VecDeque};
use std::fmt::Write as _;
use std::io::{self, Read};

const BLOCKS: usize = 30000;
const LIFETIME: u32 = 600;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    // expiry[b]: when block b becomes free, unless it is accessed again
    let mut expiry = vec![0u32; BLOCKS + 1];
    let mut busy = vec![false; BLOCKS + 1];
    // times never decrease, so the expiries are queued in order; an entry is
    // stale when the block was accessed again later
    let mut expiries: VecDeque<(u32, usize)> = VecDeque::new();
    let mut freed = BinaryHeap::new();
    let mut fresh = 1;
    let mut out = String::new();
    while let Some(tok) = it.next() {
        let t: u32 = tok.parse().unwrap();
        let op = it.next().unwrap();
        while let Some(&(e, b)) = expiries.front() {
            if e > t {
                break;
            }
            expiries.pop_front();
            if busy[b] && expiry[b] == e {
                busy[b] = false;
                freed.push(Reverse(b));
            }
        }
        let b;
        if op == "+" {
            // freed blocks are all smaller than the never used ones
            b = match freed.pop() {
                Some(Reverse(v)) => v,
                None => {
                    fresh += 1;
                    fresh - 1
                }
            };
            writeln!(out, "{}", b).unwrap();
        } else {
            b = it.next().unwrap().parse().unwrap();
            if !busy[b] {
                out.push_str("-\n");
                continue;
            }
            out.push_str("+\n");
        }
        busy[b] = true;
        expiry[b] = t + LIFETIME;
        expiries.push_back((expiry[b], b));
    }
    print!("{}", out);
}

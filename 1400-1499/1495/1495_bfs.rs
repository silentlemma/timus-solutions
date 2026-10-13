use std::io::{self, Read};

const LONGEST: u32 = 30;
const BASE: usize = 10;
const DIGITS: [usize; 2] = [1, 2];
const UNSEEN: usize = usize::MAX;
const ROOT: usize = usize::MAX - 1;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let n: usize = input.trim().parse().unwrap();
    // breadth-first search over remainders: shorter numbers come first, and
    // within one length the queue keeps numeric order, so the first number
    // to reach a remainder is the smallest one with it
    let mut parent = vec![UNSEEN; n];
    let mut digit = vec![0usize; n];
    let mut length = vec![0u32; n];
    let mut queue = Vec::with_capacity(n);
    for &d in &DIGITS {
        let r = d % n;
        if parent[r] == UNSEEN {
            parent[r] = ROOT;
            digit[r] = d;
            length[r] = 1;
            queue.push(r);
        }
    }
    let mut head = 0;
    while head < queue.len() && parent[0] == UNSEEN {
        let r = queue[head];
        head += 1;
        if length[r] == LONGEST {
            continue;
        }
        for &d in &DIGITS {
            let s = (r * BASE + d) % n;
            if parent[s] == UNSEEN {
                parent[s] = r;
                digit[s] = d;
                length[s] = length[r] + 1;
                queue.push(s);
            }
        }
    }
    if parent[0] == UNSEEN {
        println!("Impossible");
        return;
    }
    let mut out = Vec::new();
    let mut r = 0;
    while r != ROOT {
        out.push(b'0' + digit[r] as u8);
        r = parent[r];
    }
    out.reverse();
    println!("{}", String::from_utf8(out).unwrap());
}

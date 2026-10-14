use std::collections::HashMap;
use std::io::{self, Read};

const OPEN: u64 = 1; // the ends of a path piece, matched like brackets
const CLOSE: u64 = 2;
const FLIP: u64 = OPEN ^ CLOSE; // turns one end into the other
const BITS: usize = 2; // bits per plug
const MASK: u64 = 3; // one plug

// the plug matching the bracket at pos, searching towards step
fn partner(state: u64, mut pos: i32, step: i32) -> i32 {
    let mut depth = 0;
    loop {
        match state >> (BITS as i32 * pos) & MASK {
            OPEN => depth += step,
            CLOSE => depth -= step,
            _ => {}
        }
        if depth == 0 {
            return pos;
        }
        pos += step;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let m: usize = it.next().unwrap().parse().unwrap();
    let mut free = vec![vec![false; m + 1]; n + 1];
    let mut last = 0;
    for i in 0..n {
        for (j, ch) in it.next().unwrap().bytes().enumerate() {
            if ch == b'.' {
                free[i][j] = true;
                last = i * m + j;
            }
        }
    }
    // a state holds m + 1 plugs: plug j is the left side of the current cell
    // when j is its column, plug j + 1 its upper side; the rest are the lower
    // sides of the row above or this row
    let mut ways: HashMap<u64, u64> = HashMap::new();
    ways.insert(0, 1);
    let mut total = 0u64;
    for i in 0..n {
        for j in 0..m {
            let mut next: HashMap<u64, u64> = HashMap::with_capacity(ways.len() * 2);
            let (sl, su) = (BITS * j, BITS * (j + 1));
            let clear = !(MASK << sl) & !(MASK << su);
            let (down, right) = (free[i + 1][j], free[i][j + 1]);
            for (&state, &count) in &ways {
                let (left, up, base) = (state >> sl & MASK, state >> su & MASK, state & clear);
                let mut add = |s: u64| *next.entry(s).or_insert(0) += count;
                if !free[i][j] {
                    if left == 0 && up == 0 {
                        add(state);
                    }
                } else if left == 0 && up == 0 {
                    if down && right {
                        add(base | OPEN << sl | CLOSE << su);
                    }
                } else if left == 0 || up == 0 {
                    let end = left | up;
                    if down {
                        add(base | end << sl);
                    }
                    if right {
                        add(base | end << su);
                    }
                } else if left == up {
                    // two openings or two closings: the far end of one of the
                    // joined pieces changes its kind
                    let far = if left == OPEN {
                        partner(state, j as i32 + 1, 1)
                    } else {
                        partner(state, j as i32, -1)
                    };
                    add(base ^ FLIP << (BITS as i32 * far));
                } else if left == CLOSE {
                    add(base);
                } else if i * m + j == last && base == 0 {
                    total += count; // the loop closes on the last free cell
                }
            }
            ways = next;
        }
        // the next row starts with an empty left plug
        ways = ways.into_iter().map(|(s, c)| (s << BITS, c)).collect();
    }
    println!("{}", total);
}

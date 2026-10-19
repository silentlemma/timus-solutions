use std::io::{self, Read};

const FRAMES: usize = 10;
const PINS: usize = 10;
const ROLL: usize = PINS + 1; // a roll knocks down 0 to 10 pins

// table[x][y]: the least and the most points of the frames from the current
// one on, when the rolls from the current frame on start with x and y
type Table = [[(i32, i32); ROLL]; ROLL];

fn put(t: &mut Table, x: usize, y: usize, a: i32, b: i32) {
    t[x][y].0 = t[x][y].0.min(a);
    t[x][y].1 = t[x][y].1.max(b);
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let total: Vec<usize> = input.split_whitespace().map(|t| t.parse().unwrap()).collect();
    let empty: Table = [[(i32::MAX, i32::MIN); ROLL]; ROLL];
    let mut cur = empty;
    // rolls of the last frame: two, and a third one after a strike or a spare
    let last = total[FRAMES - 1];
    for r1 in 0..=PINS {
        let top = if r1 == PINS { PINS } else { PINS - r1 };
        for r2 in 0..=top {
            if r1 < PINS && r1 + r2 < PINS {
                if r1 + r2 == last {
                    put(&mut cur, r1, r2, last as i32, last as i32);
                }
                continue;
            }
            let cap = if r1 < PINS || r2 == PINS { PINS } else { PINS - r2 };
            if last >= r1 + r2 && last - r1 - r2 <= cap {
                put(&mut cur, r1, r2, last as i32, last as i32);
            }
        }
    }
    for f in (0..FRAMES - 1).rev() {
        let t = total[f];
        let mut nxt = empty;
        for x in 0..ROLL {
            for y in 0..ROLL {
                if cur[x][y].0 == i32::MAX {
                    continue;
                }
                let (a, b) = (cur[x][y].0 + t as i32, cur[x][y].1 + t as i32);
                if t < PINS {
                    for r1 in 0..=t {
                        put(&mut nxt, r1, t - r1, a, b);
                    }
                    continue;
                }
                // a strike takes the next two rolls, a spare the next one
                let (sx, sy) = (x as i32, y as i32);
                put(&mut nxt, PINS, x, a + sx + sy, b + sx + sy);
                for r1 in 0..PINS {
                    put(&mut nxt, r1, PINS - r1, a + sx, b + sx);
                }
            }
        }
        cur = nxt;
    }
    let lo = cur.iter().flatten().map(|v| v.0).min().unwrap();
    let hi = cur.iter().flatten().map(|v| v.1).max().unwrap();
    println!("{} {}", lo, hi);
}

use std::collections::HashMap;
use std::io::{self, Read};

/// A wall or door: kind 0 lies above row r, kind 1 left of column c.
type Edge = (usize, i64, i64);

fn edge_of(r: i64, c: i64, d: u8) -> Edge {
    match d {
        b'N' => (0, r, c),
        b'S' => (0, r + 1, c),
        b'W' => (1, r, c),
        _ => (1, r, c + 1),
    }
}

#[derive(Default)]
struct Scout {
    r: i64, // the position relative to the unknown start
    c: i64,
    lo_r: i64,
    hi_r: i64,
    lo_c: i64,
    hi_c: i64,
    seen: HashMap<Edge, usize>,  // 1 for a door, 0 for a wall
    by_kind: [[Vec<Edge>; 2]; 2], // [kind][door?]: the edges seen
}

struct Prison {
    w: i64,
    h: i64,
    width: i64,
    conflict: Vec<u32>, // reports ruling out the second start being the first shifted
}

impl Prison {
    /// The start pairs left: 0, 1, or 2 for two or more.
    fn starts(&self, a: &Scout, b: &Scout) -> i64 {
        let (w, h) = (self.w, self.h);
        let (lo1r, hi1r, lo1c, hi1c) = (-a.lo_r, h - 1 - a.hi_r, -a.lo_c, w - 1 - a.hi_c);
        let (lo2r, hi2r, lo2c, hi2c) = (-b.lo_r, h - 1 - b.hi_r, -b.lo_c, w - 1 - b.hi_c);
        let mut total = 0;
        for dr in -(h - 1)..h {
            let (top, bottom) = (lo1r.max(lo2r - dr), hi1r.min(hi2r - dr));
            if top > bottom {
                continue;
            }
            for dc in -(w - 1)..w {
                if self.conflict[((dr + h - 1) * self.width + dc + w - 1) as usize] != 0 {
                    continue;
                }
                let (left, right) = (lo1c.max(lo2c - dc), hi1c.min(hi2c - dc));
                if left <= right {
                    total += (bottom - top + 1) * (right - left + 1);
                    if total > 1 {
                        return 2;
                    }
                }
            }
        }
        total
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let w: i64 = words.next().unwrap().parse().unwrap();
    let h: i64 = words.next().unwrap().parse().unwrap();
    let k: usize = words.next().unwrap().parse().unwrap();
    let width = 2 * w - 1;
    let mut prison = Prison {
        w,
        h,
        width,
        conflict: vec![0; ((2 * h - 1) * width) as usize],
    };
    let mut scouts = [Scout::default(), Scout::default()];
    let mut safe = 0;
    let mut count = prison.starts(&scouts[0], &scouts[1]);
    for step in 1..=k {
        let report = words.next().unwrap().as_bytes();
        let (d, door) = (report[0], (report[1] == b'+') as usize);
        let who = (step - 1) % 2;
        let (first, second) = scouts.split_at_mut(1);
        let (me, other) = if who == 0 {
            (&mut first[0], &second[0])
        } else {
            (&mut second[0], &first[0])
        };
        let e = edge_of(me.r, me.c, d);
        let mut changed = false;
        match me.seen.get(&e) {
            None => {
                me.seen.insert(e, door);
                me.by_kind[e.0][door].push(e);
                let sign = if who == 0 { 1 } else { -1 };
                for f in &other.by_kind[e.0][1 - door] {
                    let (dr, dc) = (sign * (e.1 - f.1), sign * (e.2 - f.2));
                    if -h < dr && dr < h && -w < dc && dc < w {
                        prison.conflict[((dr + h - 1) * width + dc + w - 1) as usize] += 1;
                        changed = true;
                    }
                }
            }
            Some(&old) if old != door => {
                println!("A mistake has been made at step number {}", step);
                return;
            }
            _ => {}
        }
        if door == 1 {
            match d {
                b'N' => me.r -= 1,
                b'S' => me.r += 1,
                b'W' => me.c -= 1,
                _ => me.c += 1,
            }
            if me.r < me.lo_r || me.r > me.hi_r || me.c < me.lo_c || me.c > me.hi_c {
                me.lo_r = me.lo_r.min(me.r);
                me.hi_r = me.hi_r.max(me.r);
                me.lo_c = me.lo_c.min(me.c);
                me.hi_c = me.hi_c.max(me.c);
                changed = true;
            }
        }
        if changed {
            // the count changes only with a new conflict or a wider path
            count = prison.starts(&scouts[0], &scouts[1]);
        }
        if count == 0 {
            println!("A mistake has been made at step number {}", step);
            return;
        }
        if count == 1 && safe == 0 {
            safe = step;
        }
    }
    if safe > 0 {
        println!("The scouts are safe at step number {}", safe);
    } else {
        println!("There is not enough data");
    }
}

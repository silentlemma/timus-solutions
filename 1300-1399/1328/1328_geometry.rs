use std::io::{self, Read};

const HALF_TURN: f64 = 180.0;

struct Room {
    w: i64,
    h: i64,
    bx: i64,
    by: i64,
}

impl Room {
    // the mirror images of B that a straight line from A reaches after
    // the given number of bounces: i walls across, j walls up
    fn image(&self, i: i64, j: i64) -> (i64, i64) {
        let x = i * self.w
            + if i % 2 == 0 {
                self.bx
            } else {
                self.w - self.bx
            };
        let y = j * self.h
            + if j % 2 == 0 {
                self.by
            } else {
                self.h - self.by
            };
        (x, y)
    }

    fn images(&self, bounces: i64) -> Vec<(i64, i64)> {
        let mut found = Vec::new();
        for i in -bounces..=bounces {
            let rest = bounces - i.abs();
            found.push(self.image(i, rest));
            if rest != 0 {
                found.push(self.image(i, -rest));
            }
        }
        found
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (w, h, n, ax, ay) = (next(), next(), next(), next(), next());
    let room = Room {
        w,
        h,
        bx: next(),
        by: next(),
    };
    let mut best: Option<(i64, f64)> = None;
    for (x, y) in room.images(n) {
        let (dx, dy) = (x - ax, y - ay);
        let length = dx * dx + dy * dy;
        let mut angle = (dy as f64).atan2(dx as f64) * HALF_TURN / std::f64::consts::PI;
        if angle < 0.0 {
            angle += 2.0 * HALF_TURN;
        }
        let better = match best {
            None => true,
            Some((l, a)) => length < l || (length == l && angle < a),
        };
        if better {
            best = Some((length, angle));
        }
    }
    println!("{:.2}", best.map_or(0.0, |(_, a)| a));
}

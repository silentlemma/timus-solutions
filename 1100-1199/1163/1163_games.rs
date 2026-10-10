use std::collections::BTreeSet;
use std::f64::consts::PI;
use std::io::{self, Read};

// a draught is hit when its centre is this close to the path of the centre of
// the moving one, two radii of 0.4
const REACH: f64 = 0.8;
const EPS: f64 = 1e-9;
const SIDE: usize = 8;
const PIECES: usize = 2 * SIDE;

struct Game {
    kills: Vec<Vec<usize>>,
    memo: Vec<Option<bool>>,
}

impl Game {
    // the player to move, red (0) or white (1), wins from here
    fn wins(&mut self, alive: usize, turn: usize) -> bool {
        let key = alive << 1 | turn;
        if let Some(w) = self.memo[key] {
            return w;
        }
        let colour = ((1 << SIDE) - 1) << (SIDE * turn);
        let own = alive & colour;
        let mut result = false;
        'search: for p in 0..PIECES {
            if own >> p & 1 == 1 {
                for k in 0..self.kills[p].len() {
                    let s = self.kills[p][k];
                    if !self.wins(alive & !s, 1 - turn) {
                        result = true;
                        break 'search;
                    }
                }
            }
        }
        self.memo[key] = Some(result);
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (x, y): (Vec<f64>, Vec<f64>) = v.chunks(2).map(|c| (c[0], c[1])).unzip();
    // every direction kills the draughts within REACH of its ray; the set
    // changes only where the ray becomes tangent to some draught, so the
    // tangent directions and the gaps between them give every possible set
    let mut kills = Vec::new();
    for p in 0..PIECES {
        let mut angles = Vec::new();
        for q in (0..PIECES).filter(|&q| q != p) {
            let d = (x[q] - x[p]).hypot(y[q] - y[p]);
            let centre = (y[q] - y[p]).atan2(x[q] - x[p]);
            let half = (REACH / d).min(1.0).asin();
            for a in [centre - half, centre + half] {
                angles.push(a.rem_euclid(2.0 * PI));
            }
        }
        angles.sort_by(|a, b| a.partial_cmp(b).unwrap());
        let mut tries = angles.clone();
        for k in 0..angles.len() {
            let next = if k + 1 < angles.len() {
                angles[k + 1]
            } else {
                angles[0] + 2.0 * PI
            };
            tries.push((angles[k] + next) / 2.0);
        }
        let mut sets = BTreeSet::new();
        for t in tries {
            let (ux, uy) = (t.cos(), t.sin());
            let mut mask = 1usize << p;
            for q in (0..PIECES).filter(|&q| q != p) {
                let (dx, dy) = (x[q] - x[p], y[q] - y[p]);
                if dx * ux + dy * uy >= 0.0 && (dx * uy - dy * ux).abs() <= REACH + EPS {
                    mask |= 1 << q;
                }
            }
            sets.insert(mask);
        }
        kills.push(sets.into_iter().collect());
    }
    let mut game = Game {
        kills,
        memo: vec![None; 1 << (PIECES + 1)],
    };
    let red = game.wins((1 << PIECES) - 1, 0);
    println!("{}", if red { "RED" } else { "WHITE" });
}

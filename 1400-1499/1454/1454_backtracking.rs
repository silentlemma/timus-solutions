use std::collections::HashSet;
use std::io::{self, Read};

/// A stretch of the outline: its start, width and level.
#[derive(Clone, Copy)]
struct Seg {
    x: usize,
    span: usize,
    level: usize,
}

struct Search {
    pieces: Vec<(usize, usize)>,
    used: Vec<bool>,
    height: usize,
}

impl Search {
    /// Skyline filling: the lowest, then leftmost, stretch of the outline must
    /// hold the bottom-left corner of some piece in every tiling.
    fn fill(&mut self, sky: &[Seg], left: usize) -> bool {
        if left == 0 {
            return true;
        }
        let mut k = 0;
        for i in 1..sky.len() {
            if sky[i].level < sky[k].level {
                k = i;
            }
        }
        let s = sky[k];
        let mut tried = HashSet::new();
        for i in 0..self.pieces.len() {
            if self.used[i] {
                continue;
            }
            let (a, b) = self.pieces[i];
            for (w, h) in [(a, b), (b, a)] {
                if tried.contains(&(w, h)) || w > s.span || s.level + h > self.height {
                    continue;
                }
                tried.insert((w, h));
                let mut all: Vec<Seg> = sky[..k].to_vec();
                all.push(Seg {
                    x: s.x,
                    span: w,
                    level: s.level + h,
                });
                if w < s.span {
                    all.push(Seg {
                        x: s.x + w,
                        span: s.span - w,
                        level: s.level,
                    });
                }
                all.extend_from_slice(&sky[k + 1..]);
                let mut next: Vec<Seg> = Vec::new();
                for g in all {
                    match next.last_mut() {
                        Some(last) if last.level == g.level => last.span += g.span,
                        _ => next.push(g),
                    }
                }
                self.used[i] = true;
                if self.fill(&next, left - 1) {
                    return true;
                }
                self.used[i] = false;
            }
        }
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let pieces: Vec<(usize, usize)> = v.chunks(2).map(|c| (c[0], c[1])).collect();
    let area: usize = pieces.iter().map(|&(w, h)| w * h).sum();
    let count = pieces.len();
    let mut search = Search {
        pieces,
        used: vec![false; count],
        height: 0,
    };
    let mut width = 1;
    while width * width <= area {
        if area % width == 0 {
            search.height = area / width;
            if search.fill(
                &[Seg {
                    x: 0,
                    span: width,
                    level: 0,
                }],
                count,
            ) {
                println!("YES");
                return;
            }
        }
        width += 1;
    }
    println!("NO");
}

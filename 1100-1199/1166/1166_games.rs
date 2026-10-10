use std::io::{self, Read};

// value, suit, announced suit (0 unless a queen) and the index of the top:
// a turn-skipping card, or the face-up card before the first move
#[derive(Clone, Copy)]
struct Top {
    value: u8,
    suit: u8,
    announced: u8,
    index: usize,
}

fn covers(card: &[u8], top: Top) -> bool {
    if top.announced != 0 {
        return card[1] == top.announced;
    }
    card[1] == top.suit || card[0] == top.value
}

struct Game {
    // the cards after which the second player loses the turn: 6, 7, ace,
    // king of spades
    skips: Vec<String>,
    real: Vec<String>,
    last: Option<String>,
    jokers: usize,
    failed: Vec<bool>,
}

impl Game {
    fn top_of(&self, k: usize) -> Top {
        let b = self.skips[k].as_bytes();
        Top {
            value: b[0],
            suit: b[1],
            announced: 0,
            index: k,
        }
    }

    // lays the cards still left after top, or reports false; every card but
    // the last must make the opponent skip, and the last may be anything
    fn finish(&mut self, mask: usize, used: usize, top: Top, out: &mut Vec<String>) -> bool {
        let rest = self.real.len() - mask.count_ones() as usize + self.jokers - used
            + self.last.is_some() as usize;
        if rest == 1 {
            if let Some(last) = &self.last {
                if !covers(last.as_bytes(), top) {
                    return false;
                }
                out.push(if last.starts_with('Q') {
                    format!("{}{}", last, &last[1..2])
                } else {
                    last.clone()
                });
                return true;
            }
            if used < self.jokers {
                let suit = if top.announced != 0 {
                    top.announced
                } else {
                    top.suit
                };
                out.push(format!("*2{}", suit as char));
                return true;
            }
            let k = (0..self.real.len()).find(|&k| mask >> k & 1 == 0).unwrap();
            if !covers(self.real[k].as_bytes(), top) {
                return false;
            }
            out.push(self.real[k].clone());
            return true;
        }
        let key = (mask * (self.jokers + 1) + used) * (self.skips.len() + 1) + top.index;
        if self.failed[key] {
            return false;
        }
        for k in 0..self.real.len() {
            if mask >> k & 1 == 0 && covers(self.real[k].as_bytes(), top) {
                let s = self.skips.iter().position(|c| *c == self.real[k]).unwrap();
                out.push(self.real[k].clone());
                if self.finish(mask | 1 << k, used, self.top_of(s), out) {
                    return true;
                }
                out.pop();
            }
        }
        if used < self.jokers {
            for s in 0..self.skips.len() {
                if covers(self.skips[s].as_bytes(), top) {
                    out.push(format!("*{}", self.skips[s]));
                    if self.finish(mask, used + 1, self.top_of(s), out) {
                        return true;
                    }
                    out.pop();
                }
            }
        }
        self.failed[key] = true;
        false
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let hand: Vec<String> = lines
        .next()
        .unwrap()
        .split_whitespace()
        .map(String::from)
        .collect();
    let face_up = lines
        .next()
        .unwrap()
        .trim()
        .trim_start_matches('*')
        .as_bytes();
    let mut skips: Vec<String> = Vec::new();
    for v in "67A".chars() {
        for s in "SCDH".chars() {
            skips.push(format!("{}{}", v, s));
        }
    }
    skips.push("KS".to_string());
    let top = Top {
        value: face_up[0],
        suit: face_up[1],
        announced: if face_up[0] == b'Q' { face_up[2] } else { 0 },
        index: skips.len(),
    };
    let jokers = hand.iter().filter(|w| *w == "*").count();
    let real: Vec<String> = hand.iter().filter(|w| skips.contains(w)).cloned().collect();
    let others: Vec<String> = hand
        .iter()
        .filter(|w| *w != "*" && !skips.contains(w))
        .cloned()
        .collect();
    if others.len() > 1 {
        println!("NO");
        return;
    }
    let size = (1 << real.len()) * (jokers + 1) * (skips.len() + 1);
    let mut game = Game {
        skips,
        real,
        last: others.into_iter().next(),
        jokers,
        failed: vec![false; size],
    };
    let mut order = Vec::new();
    if game.finish(0, 0, top, &mut order) {
        println!("YES\n{}", order.join(" "));
    } else {
        println!("NO");
    }
}

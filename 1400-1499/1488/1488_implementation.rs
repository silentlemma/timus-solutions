use std::io::{self, Read};

const THREE: u32 = 3;
const CARDS: usize = 8; // three of Sasha's, three of Dima's, two in the sleeve
const HAND: usize = 3;
const SLEEVE: usize = 6;
const FIRST_FACE: u32 = 11; // J, Q, K, A rank from 11 to 14
const FACES: &str = "JQKA";
// combinations from the lowest: high card, pair, flush, straight,
// three of a kind, straight flush, three threes
const HIGH: u32 = 0;
const PAIR: u32 = 1;
const FLUSH: u32 = 2;
const STRAIGHT: u32 = 3;
const TRIPLE: u32 = 4;
const STRAIGHT_FLUSH: u32 = 5;
const THREE_THREES: u32 = 6;
const KEY: usize = 4; // the combination and up to three ranks

fn rank_of(card: &str) -> u32 {
    let name = &card[..card.len() - 1];
    match FACES.find(name) {
        Some(i) if name.len() == 1 => FIRST_FACE + i as u32,
        _ => name.parse().unwrap(),
    }
}

/// A key that orders hands from the weakest to the strongest.
fn value(h: &[&str]) -> [u32; KEY] {
    let mut r: Vec<u32> = h.iter().map(|c| rank_of(c)).collect();
    r.sort_unstable_by(|x, y| y.cmp(x));
    let (a, b, c) = (r[0], r[1], r[2]);
    let suit = |s: &str| s.as_bytes()[s.len() - 1];
    let flush = suit(h[0]) == suit(h[1]) && suit(h[1]) == suit(h[2]);
    let straight = a == b + 1 && b == c + 1;
    if a == THREE && c == THREE {
        [THREE_THREES, 0, 0, 0]
    } else if straight && flush {
        [STRAIGHT_FLUSH, a, b, c]
    } else if a == c {
        [TRIPLE, a, b, c]
    } else if straight {
        [STRAIGHT, a, b, c]
    } else if flush {
        [FLUSH, a, b, c]
    } else if a == b {
        [PAIR, a, c, 0]
    } else if b == c {
        [PAIR, b, a, 0]
    } else {
        [HIGH, a, b, c]
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let tokens: Vec<&str> = input.split_ascii_whitespace().collect();
    let mut out = String::new();
    for card in tokens.chunks(CARDS).filter(|g| g.len() == CARDS) {
        let (sasha, dima) = (&card[..HAND], &card[HAND..SLEEVE]);
        let usable: Vec<&str> = card[SLEEVE..]
            .iter()
            .filter(|c| !sasha.contains(c))
            .copied()
            .collect();
        // Dima's hands: as dealt, one card swapped, or two swapped for both
        let mut hands: Vec<Vec<&str>> = vec![dima.to_vec()];
        for &c in &usable {
            for i in 0..HAND {
                let mut h = dima.to_vec();
                h[i] = c;
                hands.push(h);
            }
        }
        if usable.len() == 2 {
            for keep in 0..HAND {
                hands.push(vec![dima[keep], usable[0], usable[1]]);
            }
        }
        let target = value(sasha);
        let mut win = false;
        let mut draw = false;
        for h in &hands {
            if h[0] == h[1] || h[1] == h[2] || h[0] == h[2] {
                continue;
            }
            let v = value(h);
            win |= v > target;
            draw |= v == target;
        }
        out.push_str(if win {
            "Dima\n"
        } else if draw {
            "Artyom\n"
        } else {
            "Sasha\n"
        });
    }
    print!("{}", out);
}

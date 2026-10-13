use std::io::{self, Read};

const PLAYERS: usize = 3;
const SUITS: usize = 4;
const RANKS: usize = 8;
const HAND: usize = 10; // cards per player
const SUIT_BITS: u32 = 14; // an owner string of a suit fits in this many bits
const CACHE_BITS: u32 = 20; // 8 MB of remembered positions, well inside 16 MB
const FULL_SUIT: u32 = (1 << RANKS) - 1;
const GOLDEN: u64 = 0x9E37_79B9_7F4A_7C15;
const RANK_NAMES: [&str; RANKS] = ["7", "8", "9", "10", "J", "Q", "K", "A"];

struct Game {
    // hand[p] holds player p's cards, suit s in bits 8 s .. 8 s + 7, rank upwards
    hand: [u32; PLAYERS],
    cache: Vec<u64>,
}

impl Game {
    /// The suits play alike and only the order of the cards inside a suit
    /// matters, so a position is the sorted owner strings of the suits.
    fn key(&self, leader: usize) -> u64 {
        let mut codes = [0u64; SUITS];
        for (s, code) in codes.iter_mut().enumerate() {
            let mut v = 1;
            for c in s * RANKS..(s + 1) * RANKS {
                for p in 0..PLAYERS {
                    if self.hand[p] >> c & 1 == 1 {
                        v = v * PLAYERS as u64 + p as u64;
                    }
                }
            }
            *code = v;
        }
        codes.sort_unstable();
        codes
            .iter()
            .fold(leader as u64 + 1, |k, &v| k << SUIT_BITS | v)
    }

    /// One card from each run of touching cards, where no other player's
    /// card lies between two cards of a run.
    fn choices(&self, p: usize, allowed: u32, everyone: u32) -> Vec<usize> {
        (0..SUITS * RANKS)
            .filter(|&c| {
                if allowed >> c & 1 == 0 {
                    return false;
                }
                let s = c / RANKS;
                let below = everyone & ((1u32 << c) - 1) & (FULL_SUIT << (s * RANKS));
                below == 0 || self.hand[p] >> (u32::BITS - 1 - below.leading_zeros()) & 1 == 0
            })
            .collect()
    }

    /// The first player looks for any good card, the other two for any card
    /// that makes the first player take the trick.
    fn play(
        &mut self,
        leader: usize,
        step: usize,
        suit: usize,
        best: i32,
        best_player: usize,
        everyone: u32,
    ) -> bool {
        let p = (leader + step) % PLAYERS;
        let mut allowed = self.hand[p];
        if step > 0 && allowed & (FULL_SUIT << (suit * RANKS)) != 0 {
            allowed &= FULL_SUIT << (suit * RANKS);
        }
        for c in self.choices(p, allowed, everyone) {
            let (mut s, mut b, mut bp) = (suit, best, best_player);
            if step == 0 {
                s = c / RANKS;
                b = c as i32;
                bp = p;
            } else if c / RANKS == suit && c as i32 > best {
                b = c as i32;
                bp = p;
            }
            self.hand[p] &= !(1u32 << c);
            let ok = if step + 1 < PLAYERS {
                self.play(leader, step + 1, s, b, bp, everyone)
            } else {
                bp != 0 && self.survive(bp)
            };
            self.hand[p] |= 1u32 << c;
            if ok == (p == 0) {
                return ok;
            }
        }
        p != 0
    }

    /// Can the first player take no trick from here, whatever the others do.
    fn survive(&mut self, leader: usize) -> bool {
        if self.hand[0] == 0 {
            return true;
        }
        let k = self.key(leader);
        let slot = (k.wrapping_mul(GOLDEN) >> (u64::BITS - CACHE_BITS)) as usize;
        if self.cache[slot] >> 1 == k {
            return self.cache[slot] & 1 == 1;
        }
        let everyone = self.hand[0] | self.hand[1] | self.hand[2];
        let result = self.play(leader, 0, 0, -1, 0, everyone);
        self.cache[slot] = k << 1 | result as u64;
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let words: Vec<&str> = input.split_ascii_whitespace().collect();
    let mut game = Game {
        hand: [0; PLAYERS],
        cache: vec![0; 1 << CACHE_BITS],
    };
    for p in 0..PLAYERS {
        for t in &words[p * HAND..(p + 1) * HAND] {
            let s = "SCDH".find(&t[t.len() - 1..]).unwrap();
            let r = RANK_NAMES
                .iter()
                .position(|&n| n == &t[..t.len() - 1])
                .unwrap();
            game.hand[p] |= 1 << (s * RANKS + r);
        }
    }
    let leader: usize = words[PLAYERS * HAND].parse().unwrap();
    println!("{}", if game.survive(leader - 1) { ";)" } else { ";(" });
}

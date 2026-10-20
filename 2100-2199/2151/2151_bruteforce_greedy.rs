use std::io::{self, Read};

const SUIT_COUNT: usize = 3;
const RANK_COUNT: usize = 9;
const TILE_TYPES: usize = SUIT_COUNT * RANK_COUNT;
const HAND_SIZE: usize = 14;
const GROUP_SIZE: u8 = 3;

fn winning(counts: &[u8; TILE_TYPES]) -> bool {
    let mut pair_suit = SUIT_COUNT;
    for suit in 0..SUIT_COUNT {
        let total: u8 = counts[suit * RANK_COUNT..(suit + 1) * RANK_COUNT]
            .iter()
            .sum();
        match total % GROUP_SIZE {
            0 => {}
            2 => {
                if pair_suit != SUIT_COUNT {
                    return false;
                }
                pair_suit = suit;
            }
            _ => return false,
        }
    }
    if pair_suit == SUIT_COUNT {
        return false;
    }

    for pair in pair_suit * RANK_COUNT..(pair_suit + 1) * RANK_COUNT {
        if counts[pair] < 2 {
            continue;
        }
        let mut remaining = *counts;
        remaining[pair] -= 2;
        let mut valid = true;
        for tile in 0..TILE_TYPES {
            let needed = remaining[tile] % GROUP_SIZE;
            if needed == 0 {
                continue;
            }
            // Three parallel sequences can be replaced by three equal triples.
            if tile % RANK_COUNT >= RANK_COUNT - 2
                || remaining[tile + 1] < needed
                || remaining[tile + 2] < needed
            {
                valid = false;
                break;
            }
            remaining[tile + 1] -= needed;
            remaining[tile + 2] -= needed;
        }
        if valid {
            return true;
        }
    }
    false
}

fn classify(mut counts: [u8; TILE_TYPES]) -> &'static str {
    if winning(&counts) {
        return "Tsumo";
    }
    for removed in 0..TILE_TYPES {
        if counts[removed] == 0 {
            continue;
        }
        counts[removed] -= 1;
        for added in 0..TILE_TYPES {
            if added == removed {
                continue;
            }
            counts[added] += 1;
            if winning(&counts) {
                return "Tenpai";
            }
            counts[added] -= 1;
        }
        counts[removed] += 1;
    }
    "Noten"
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut counts = [0; TILE_TYPES];
    for token in input.split_whitespace().take(HAND_SIZE) {
        let bytes = token.as_bytes();
        let rank = usize::from(bytes[0] - b'1');
        let suit = usize::from(bytes[1] - b'a');
        counts[suit * RANK_COUNT + rank] += 1;
    }
    println!("{}", classify(counts));
}

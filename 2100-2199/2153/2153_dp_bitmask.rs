use std::io::{self, Read};

const ROLE_COUNT: usize = 4;
const STATE_COUNT: usize = 1 << ROLE_COUNT;
const ROLE_LETTERS: &[u8; ROLE_COUNT] = b"WMCR";
const ROLE_NAMES: [&str; ROLE_COUNT] = ["warrior", "mage", "cleric", "rogue"];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let member_count: usize = tokens.next().unwrap().parse().unwrap();
    let mut reachable = [false; STATE_COUNT];
    reachable[0] = true;

    for _ in 0..member_count {
        let qualifications = tokens.next().unwrap().as_bytes();
        let mut skills = 0;
        for (role, letter) in ROLE_LETTERS.iter().enumerate() {
            if qualifications.contains(letter) {
                skills |= 1 << role;
            }
        }
        // Larger masks are visited first, so this member fills at most one role.
        for mask in (0..STATE_COUNT).rev() {
            if !reachable[mask] {
                continue;
            }
            for role in 0..ROLE_COUNT {
                let bit = 1 << role;
                if skills & bit != 0 && mask & bit == 0 {
                    reachable[mask | bit] = true;
                }
            }
        }
    }

    let mut best = 0;
    let mut common = STATE_COUNT - 1;
    for (mask, &possible) in reachable.iter().enumerate() {
        if !possible {
            continue;
        }
        let size = mask.count_ones() as usize;
        if size > best {
            best = size;
            common = mask;
        } else if size == best {
            common &= mask;
        }
    }

    println!("{}", best);
    if best < ROLE_COUNT {
        let mut announcement = String::from("Looking for");
        for (role, name) in ROLE_NAMES.iter().enumerate() {
            if common & (1 << role) == 0 {
                announcement.push(' ');
                announcement.push_str(name);
            }
        }
        println!("{}", announcement);
    }
}

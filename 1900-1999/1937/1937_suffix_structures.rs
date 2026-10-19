use std::io::{self, Read};

const ALPHABET_SIZE: usize = 26;

fn palindrome_radii(text: &[u8], odd: bool) -> Vec<i32> {
    let count = text.len();
    let mut radius = vec![0i32; count];
    let mut left = 0;
    let mut right: isize = -1;
    if odd {
        for center in 0..count {
            let mut current = if center as isize > right {
                0
            } else {
                (radius[left + right as usize - center] as usize).min(right as usize - center)
            };
            while center > current
                && center + current + 1 < count
                && text[center - current - 1] == text[center + current + 1]
            {
                current += 1;
            }
            radius[center] = current as i32;
            if (center + current) as isize > right {
                left = center - current;
                right = (center + current) as isize;
            }
        }
    } else {
        for center in 0..count {
            let mut current = if center as isize > right {
                0
            } else {
                (radius[left + right as usize - center + 1] as usize)
                    .min(right as usize - center + 1)
            };
            while center > current
                && center + current < count
                && text[center - current - 1] == text[center + current]
            {
                current += 1;
            }
            radius[center] = current as i32;
            let candidate_right = (center + current) as isize - 1;
            if candidate_right > right {
                left = center - current;
                right = candidate_right;
            }
        }
    }
    radius
}

struct SuffixAutomaton {
    transitions: Vec<i32>,
    length: Vec<i32>,
    link: Vec<i32>,
    first_end: Vec<i32>,
}

impl SuffixAutomaton {
    fn new(pattern: &[u8]) -> Self {
        let capacity = 2 * pattern.len();
        let mut automaton = Self {
            transitions: vec![-1; capacity * ALPHABET_SIZE],
            length: vec![0; capacity],
            link: vec![-1; capacity],
            first_end: vec![-1; capacity],
        };
        let mut states = 1;
        let mut last = 0;
        for (position, &letter) in pattern.iter().enumerate() {
            let symbol = (letter - b'a') as usize;
            let current = states;
            states += 1;
            automaton.length[current] = automaton.length[last] + 1;
            automaton.first_end[current] = position as i32;
            let mut previous = last as i32;
            while previous >= 0
                && automaton.transitions[previous as usize * ALPHABET_SIZE + symbol] < 0
            {
                automaton.transitions[previous as usize * ALPHABET_SIZE + symbol] = current as i32;
                previous = automaton.link[previous as usize];
            }
            if previous < 0 {
                automaton.link[current] = 0;
            } else {
                let following =
                    automaton.transitions[previous as usize * ALPHABET_SIZE + symbol] as usize;
                if automaton.length[previous as usize] + 1 == automaton.length[following] {
                    automaton.link[current] = following as i32;
                } else {
                    let clone = states;
                    states += 1;
                    automaton.length[clone] = automaton.length[previous as usize] + 1;
                    automaton.link[clone] = automaton.link[following];
                    automaton.first_end[clone] = automaton.first_end[following];
                    let source = following * ALPHABET_SIZE;
                    automaton
                        .transitions
                        .copy_within(source..source + ALPHABET_SIZE, clone * ALPHABET_SIZE);
                    while previous >= 0
                        && automaton.transitions[previous as usize * ALPHABET_SIZE + symbol]
                            == following as i32
                    {
                        automaton.transitions[previous as usize * ALPHABET_SIZE + symbol] =
                            clone as i32;
                        previous = automaton.link[previous as usize];
                    }
                    automaton.link[following] = clone as i32;
                    automaton.link[current] = clone as i32;
                }
            }
            last = current;
        }
        automaton
    }
}

fn find_rotations(first: &[u8], second: &[u8]) -> Option<(usize, usize)> {
    let first_size = first.len();
    let second_size = second.len();
    let middle_size = first_size - second_size;
    let mut doubled = Vec::with_capacity(2 * first_size);
    doubled.extend_from_slice(first);
    doubled.extend_from_slice(first);
    let radius = palindrome_radii(&doubled, middle_size % 2 != 0);
    let half = middle_size / 2;
    let center_offset = second_size + half;
    if !(0..first_size).any(|start| radius[start + center_offset] as usize >= half) {
        return None;
    }
    let reversed_second: Vec<u8> = second.iter().rev().copied().collect();
    let mut pattern = reversed_second.clone();
    pattern.extend_from_slice(&reversed_second[..second_size - 1]);
    let automaton = SuffixAutomaton::new(&pattern);
    let mut state = 0;
    let mut matched = 0;
    for position in 0..first_size + second_size - 1 {
        let symbol = (doubled[position] - b'a') as usize;
        while state != 0 && automaton.transitions[state * ALPHABET_SIZE + symbol] < 0 {
            state = automaton.link[state] as usize;
            matched = automaton.length[state] as usize;
        }
        let following = automaton.transitions[state * ALPHABET_SIZE + symbol];
        if following >= 0 {
            state = following as usize;
            matched += 1;
        } else {
            state = 0;
            matched = 0;
        }
        if position + 1 >= second_size && matched >= second_size {
            let start = position + 1 - second_size;
            if radius[start + center_offset] as usize >= half {
                let reversed_start = automaton.first_end[state] as usize + 1 - second_size;
                return Some((start, (second_size - reversed_start) % second_size));
            }
        }
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let first = words.next().unwrap().as_bytes();
    let second = words.next().unwrap().as_bytes();
    match find_rotations(first, second) {
        Some((left, right)) => println!("Yes\n{} {}", left + 1, right + 1),
        None => println!("No"),
    }
}

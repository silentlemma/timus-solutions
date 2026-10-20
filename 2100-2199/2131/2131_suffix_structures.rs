use std::collections::HashSet;
use std::fmt::Write;
use std::io::{self, Read};

const LETTERS: usize = 26;
const ALPHABET: usize = LETTERS + 1;
const NONE: usize = usize::MAX;
const INF: usize = usize::MAX;

struct Automaton {
    next: Vec<[u32; ALPHABET]>,
    length: Vec<usize>,
    link: Vec<usize>,
    first_end: Vec<usize>,
    negative: Vec<usize>,
    missing: Vec<usize>,
    bags: Vec<Option<HashSet<usize>>>,
    team_count: usize,
}

impl Automaton {
    fn new(capacity: usize, team_count: usize) -> Self {
        let mut result = Self {
            next: Vec::with_capacity(capacity),
            length: Vec::with_capacity(capacity),
            link: Vec::with_capacity(capacity),
            first_end: Vec::with_capacity(capacity),
            negative: Vec::with_capacity(capacity),
            missing: Vec::with_capacity(capacity),
            bags: Vec::with_capacity(capacity),
            team_count,
        };
        result.add_state(0);
        result.link[0] = NONE;
        result
    }

    fn add_state(&mut self, length: usize) -> usize {
        let state = self.length.len();
        self.next.push([0; ALPHABET]);
        self.length.push(length);
        self.link.push(0);
        self.first_end.push(INF);
        self.negative.push(self.team_count);
        self.missing.push(1);
        self.bags.push(None);
        state
    }

    fn clone_state(&mut self, state: usize, length: usize) -> usize {
        let clone = self.add_state(length);
        self.next[clone] = self.next[state];
        self.link[clone] = self.link[state];
        clone
    }

    fn extend(&mut self, last: usize, character: usize) -> usize {
        let mut parent = last;
        let mut target = self.next[parent][character] as usize;
        if target != 0 {
            if self.length[parent] + 1 == self.length[target] {
                return target;
            }
            let clone = self.clone_state(target, self.length[parent] + 1);
            while parent != NONE && self.next[parent][character] as usize == target {
                self.next[parent][character] = clone as u32;
                parent = self.link[parent];
            }
            self.link[target] = clone;
            return clone;
        }

        let current = self.add_state(self.length[last] + 1);
        while parent != NONE && self.next[parent][character] == 0 {
            self.next[parent][character] = current as u32;
            parent = self.link[parent];
        }
        if parent == NONE {
            return current;
        }
        target = self.next[parent][character] as usize;
        if self.length[parent] + 1 == self.length[target] {
            self.link[current] = target;
            return current;
        }
        let clone = self.clone_state(target, self.length[parent] + 1);
        while parent != NONE && self.next[parent][character] as usize == target {
            self.next[parent][character] = clone as u32;
            parent = self.link[parent];
        }
        self.link[target] = clone;
        self.link[current] = clone;
        current
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let team_count: usize = tokens.next().unwrap().parse().unwrap();
    let rows: Vec<&[u8]> = tokens.take(team_count).map(str::as_bytes).collect();
    let total_length: usize = rows
        .iter()
        .map(|row| row.len() - usize::from(row.last() == Some(&b'+')))
        .sum();
    let mut automaton = Automaton::new(2 * total_length + 1, team_count);
    let mut positive_times = vec![0; team_count + 1];
    let mut positive_count = 0;

    for (team, row) in rows.iter().enumerate() {
        let positive = row.last() == Some(&b'+');
        let name = &row[..row.len() - usize::from(positive)];
        if team > 0 && positive {
            positive_count += 1;
            positive_times[positive_count] = team;
        }
        let mut last = 0;
        for (position, &letter) in name.iter().enumerate() {
            let character = if letter == b'_' {
                LETTERS
            } else {
                (letter - b'a') as usize
            };
            last = automaton.extend(last, character);
            if team == 0 {
                automaton.first_end[last] = automaton.first_end[last].min(position);
            } else if positive {
                automaton.bags[last]
                    .get_or_insert_with(|| HashSet::with_capacity(2))
                    .insert(positive_count);
            } else {
                automaton.negative[last] = automaton.negative[last].min(team);
            }
        }
    }
    positive_times[positive_count + 1] = team_count;
    automaton.next = Vec::new();

    let state_count = automaton.length.len();
    let mut counts = vec![0; total_length + 1];
    for &length in &automaton.length {
        counts[length] += 1;
    }
    for index in 1..counts.len() {
        counts[index] += counts[index - 1];
    }
    let mut order = vec![0; state_count];
    for state in 0..state_count {
        let length = automaton.length[state];
        counts[length] -= 1;
        order[counts[length]] = state;
    }

    let mut best = vec![(INF, INF); team_count + 1];
    // Suffix links collect all teams containing a state's substrings.
    for &state in order[1..].iter().rev() {
        let bag = automaton.bags[state].take();
        let mut absent = automaton.missing[state];
        if let Some(ref values) = bag {
            while values.contains(&absent) {
                absent += 1;
            }
        }
        // Every substring in this state stops working at the same arrival.
        let deadline = automaton.negative[state].min(positive_times[absent]);
        let parent = automaton.link[state];
        let length = automaton.length[parent] + 1;
        if automaton.first_end[state] != INF {
            let left = automaton.first_end[state] + 1 - length;
            best[deadline] = best[deadline].min((length, left));
        }

        automaton.first_end[parent] = automaton.first_end[parent].min(automaton.first_end[state]);
        automaton.negative[parent] = automaton.negative[parent].min(automaton.negative[state]);
        automaton.missing[parent] = automaton.missing[parent].max(absent);
        if let Some(mut source) = bag {
            if let Some(mut target) = automaton.bags[parent].take() {
                if target.len() < source.len() {
                    std::mem::swap(&mut target, &mut source);
                }
                target.extend(source);
                automaton.bags[parent] = Some(target);
            } else {
                automaton.bags[parent] = Some(source);
            }
        }
    }

    for time in (1..team_count).rev() {
        best[time] = best[time].min(best[time + 1]);
    }
    let mut output = String::new();
    for &(length, left) in &best[1..] {
        if length == INF {
            output.push_str("-1 -1\n");
        } else {
            writeln!(output, "{} {}", left, left + length - 1).unwrap();
        }
    }
    print!("{}", output);
}

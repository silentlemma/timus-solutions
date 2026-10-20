use std::io::{self, Read};

const LIMIT: usize = 2_000_000; // the largest possible sum of two notes

struct Matcher<'a> {
    composite: &'a [bool],
    odd: &'a [usize],
    even: &'a [usize],
    partner: Vec<usize>, // the odd note matched to each even note
    visited: Vec<bool>,
}

impl Matcher<'_> {
    fn augment(&mut self, u: usize) -> bool {
        for v in 0..self.even.len() {
            if self.visited[v] || self.composite[self.odd[u] + self.even[v]] {
                continue;
            }
            self.visited[v] = true;
            if self.partner[v] == usize::MAX || self.augment(self.partner[v]) {
                self.partner[v] = u;
                return true;
            }
        }
        false
    }
}

fn main() {
    let mut composite = vec![false; LIMIT + 1];
    composite[0] = true;
    composite[1] = true;
    let mut i = 2;
    while i * i <= LIMIT {
        if !composite[i] {
            let mut j = i * i;
            while j <= LIMIT {
                composite[j] = true;
                j += i;
            }
        }
        i += 1;
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let notes: Vec<usize> = it.take(n).collect();
    let ones = notes.iter().filter(|&&c| c == 1).count();
    let mut odd: Vec<usize> = notes.iter().copied().filter(|&c| c % 2 == 1 && c != 1).collect();
    let even: Vec<usize> = notes.iter().copied().filter(|&c| c % 2 == 0).collect();
    // A prime sum is 2 = 1 + 1 or an odd prime, the sum of an odd and an even
    // note. So the surplus of odd notes must be paired as ones among themselves.
    let total_odd = ones + odd.len();
    if total_odd < even.len() || total_odd - even.len() > ones {
        println!("NO");
        return;
    }
    let one_pairs = (total_odd - even.len()) / 2;
    odd.extend(std::iter::repeat(1).take(ones - 2 * one_pairs));
    let mut matcher = Matcher {
        composite: &composite,
        odd: &odd,
        even: &even,
        partner: vec![usize::MAX; even.len()],
        visited: Vec::new(),
    };
    for u in 0..odd.len() {
        matcher.visited = vec![false; even.len()];
        if !matcher.augment(u) {
            println!("NO");
            return;
        }
    }
    let mut out = String::from("YES\n");
    for _ in 0..one_pairs {
        out.push_str("1 1\n");
    }
    for (v, &e) in even.iter().enumerate() {
        out.push_str(&format!("{} {}\n", odd[matcher.partner[v]], e));
    }
    print!("{}", out);
}

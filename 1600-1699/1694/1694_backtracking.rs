use std::io::{self, Read};

struct Search {
    k: usize,
    longest: usize,
    word: Vec<usize>,
    counts: Vec<Vec<i64>>,
}

impl Search {
    // whether some k-repetition ends at the last letter of word
    fn repetition_at_end(&self) -> bool {
        let size = self.word.len();
        let mut block = 1;
        while block * self.k <= size {
            let mut i = size - self.k * block;
            while i < size - block && self.word[i] == self.word[i + block] {
                i += 1;
            }
            if i == size - block {
                return true;
            }
            block += 1;
        }
        false
    }

    // whether w^k has a k-repetition other than itself; w has none, and w^k
    // repeats with period |w|, so only windows that start in the first copy
    // and leave it need a look
    fn proper_repetition(&self) -> bool {
        let size = self.word.len();
        let total = size * self.k;
        for block in 1..=size {
            let span = self.k * block;
            let mut start = 0;
            while start < size && start + span <= total {
                if start + span > size && span != total {
                    let (mut i, end) = (start, start + span - block);
                    while i < end && self.word[i % size] == self.word[(i + block) % size] {
                        i += 1;
                    }
                    if i == end {
                        return true;
                    }
                }
                start += 1;
            }
        }
        false
    }

    fn extend(&mut self, distinct: usize) {
        // w^k may fail while a longer w still works, so this only skips counting
        if !self.word.is_empty() && !self.proper_repetition() {
            self.counts[self.word.len()][distinct] += 1;
        }
        if self.word.len() == self.longest {
            return;
        }
        for c in 0..=distinct {
            self.word.push(c);
            // a k-repetition inside w is one inside the killer word too
            if !self.repetition_at_end() {
                self.extend(distinct.max(c + 1));
            }
            self.word.pop();
        }
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let (m, k, n) = (v[0], v[1] as usize, v[2] as usize);
    // a killer word is w repeated k times; whether it works does not depend
    // on which letters w uses, so count the words w with letters numbered in
    // order of first appearance, by their number of different letters
    let longest = n / k;
    let counts = vec![vec![0; longest + 1]; longest + 1];
    let mut search = Search { k, longest, word: Vec::new(), counts };
    search.extend(0);
    let mut total: i64 = 0;
    for length in 1..=longest {
        let mut ways: i64 = 1;
        for distinct in 1..=length {
            ways *= (m - distinct as i64 + 1).max(0);
            total += search.counts[length][distinct] * ways;
        }
    }
    println!("{}", total);
}

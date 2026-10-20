use std::io::{self, Read};

const ALPHABET_SIZE: usize = 26;
const FIRST_LETTER: u8 = b'a';

fn suffix_array(text: &[u8]) -> Vec<usize> {
    let n = text.len();
    let length = n + 1;
    let mut symbols = vec![0; length];
    for i in 0..n {
        symbols[i] = usize::from(text[i] - FIRST_LETTER) + 1;
    }
    let mut order = vec![0; length];
    let mut classes = vec![0; length];
    let mut shifted = vec![0; length];
    let mut next_classes = vec![0; length];
    let mut counts = vec![0; length.max(ALPHABET_SIZE + 1)];
    for &symbol in &symbols {
        counts[symbol] += 1;
    }
    for i in 1..counts.len() {
        counts[i] += counts[i - 1];
    }
    for i in (0..length).rev() {
        counts[symbols[i]] -= 1;
        order[counts[symbols[i]]] = i;
    }
    let mut class_count = 1;
    for i in 1..length {
        if symbols[order[i]] != symbols[order[i - 1]] {
            class_count += 1;
        }
        classes[order[i]] = class_count - 1;
    }
    let mut shift = 1;
    while shift < length && class_count < length {
        for i in 0..length {
            shifted[i] = if order[i] >= shift {
                order[i] - shift
            } else {
                order[i] + length - shift
            };
        }
        counts[..class_count].fill(0);
        for &index in &shifted {
            counts[classes[index]] += 1;
        }
        for i in 1..class_count {
            counts[i] += counts[i - 1];
        }
        for &index in shifted.iter().rev() {
            counts[classes[index]] -= 1;
            order[counts[classes[index]]] = index;
        }
        let mut next_count = 1;
        next_classes[order[0]] = 0;
        for i in 1..length {
            let current = order[i];
            let previous = order[i - 1];
            let current_next = (current + shift) % length;
            let previous_next = (previous + shift) % length;
            if classes[current] != classes[previous]
                || classes[current_next] != classes[previous_next]
            {
                next_count += 1;
            }
            next_classes[current] = next_count - 1;
        }
        std::mem::swap(&mut classes, &mut next_classes);
        class_count = next_count;
        shift *= 2;
    }
    order[1..].to_vec()
}

struct CommonPrefixes {
    size: usize,
    ranks: Vec<usize>,
    minimum: Vec<usize>,
}

impl CommonPrefixes {
    fn new(text: &[u8]) -> Self {
        let size = text.len();
        let order = suffix_array(text);
        let mut ranks = vec![0; size];
        let mut minimum = vec![size; 2 * size];
        for i in 0..size {
            ranks[order[i]] = i;
        }
        let mut matched = 0;
        for i in 0..size {
            let rank = ranks[i];
            if rank + 1 == size {
                matched = 0;
                continue;
            }
            let other = order[rank + 1];
            while i + matched < size
                && other + matched < size
                && text[i + matched] == text[other + matched]
            {
                matched += 1;
            }
            minimum[size + rank] = matched;
            matched = matched.saturating_sub(1);
        }
        for i in (1..size).rev() {
            minimum[i] = minimum[2 * i].min(minimum[2 * i + 1]);
        }
        Self {
            size,
            ranks,
            minimum,
        }
    }

    fn query(&self, first: usize, second: usize) -> usize {
        let mut left = self.ranks[first];
        let mut right = self.ranks[second];
        if left > right {
            std::mem::swap(&mut left, &mut right);
        }
        left += self.size;
        right += self.size;
        let mut result = self.size;
        while left < right {
            if left % 2 == 1 {
                result = result.min(self.minimum[left]);
                left += 1;
            }
            if right % 2 == 1 {
                right -= 1;
                result = result.min(self.minimum[right]);
            }
            left /= 2;
            right /= 2;
        }
        result
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let text = tokens.next().unwrap().as_bytes();
    let prefixes = CommonPrefixes::new(text);
    let mut representative = [[0; ALPHABET_SIZE + 1]; ALPHABET_SIZE];
    let mut representative_cost = [[0; ALPHABET_SIZE + 1]; ALPHABET_SIZE];
    let mut representative_count = [0; ALPHABET_SIZE];
    let mut farthest = [0; ALPHABET_SIZE + 1];
    let mut skipped = 0;
    for position in 0..n {
        let letter = usize::from(text[position] - FIRST_LETTER);
        let count = representative_count[letter];
        let mut best_length = 0;
        for index in (0..count).rev() {
            let previous = representative[letter][index];
            if text[previous + best_length] != text[position + best_length] {
                continue;
            }
            let length = prefixes.query(previous, position);
            if length > best_length {
                let cost = representative_cost[letter][index];
                farthest[cost] = farthest[cost].max(position + length);
                best_length = length;
                if best_length == n - position {
                    break;
                }
            }
        }
        // An earlier start with no larger cost dominates this start.
        if count == 0 || skipped < representative_cost[letter][count - 1] {
            representative[letter][count] = position;
            representative_cost[letter][count] = skipped;
            representative_count[letter] = count + 1;
        }
        let mut next_cost = skipped + 1;
        for (cost, &end) in farthest.iter().enumerate().take(next_cost) {
            if end >= position + 1 {
                next_cost = cost;
                break;
            }
        }
        skipped = next_cost;
    }
    println!("{}", n - skipped);
}

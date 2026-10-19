use std::io::{self, Read};

// character classes, ordered: the end, other characters, dot, at, letters
const OTHER: u8 = 1;
const DOT: u8 = 2;
const AT: u8 = 3;
const LETTER: u8 = 4;
const ALPHABET: usize = LETTER as usize + 26;

// cyclic prefix doubling with counting sort; code ends with a 0
fn suffix_array(code: &[u8]) -> (Vec<u32>, Vec<u32>) {
    let n = code.len();
    let mut count = vec![0u32; n.max(ALPHABET)];
    let mut order = vec![0u32; n];
    let mut cls = vec![0u32; n];
    let mut shifted = vec![0u32; n];
    let mut fresh = vec![0u32; n];
    for &c in code {
        count[c as usize] += 1;
    }
    for i in 1..ALPHABET {
        count[i] += count[i - 1];
    }
    for i in (0..n).rev() {
        count[code[i] as usize] -= 1;
        order[count[code[i] as usize] as usize] = i as u32;
    }
    let mut classes = 1;
    for i in 1..n {
        if code[order[i] as usize] != code[order[i - 1] as usize] {
            classes += 1;
        }
        cls[order[i] as usize] = classes - 1;
    }
    let mut shift = 1;
    while shift < n && (classes as usize) < n {
        for i in 0..n {
            shifted[i] = ((order[i] as usize + n - shift) % n) as u32;
        }
        count[..classes as usize].iter_mut().for_each(|c| *c = 0);
        for &p in &shifted {
            count[cls[p as usize] as usize] += 1;
        }
        for i in 1..classes as usize {
            count[i] += count[i - 1];
        }
        for i in (0..n).rev() {
            let p = shifted[i] as usize;
            count[cls[p] as usize] -= 1;
            order[count[cls[p] as usize] as usize] = p as u32;
        }
        fresh[order[0] as usize] = 0;
        classes = 1;
        for i in 1..n {
            let (cur, prev) = (order[i] as usize, order[i - 1] as usize);
            if cls[cur] != cls[prev] || cls[(cur + shift) % n] != cls[(prev + shift) % n] {
                classes += 1;
            }
            fresh[cur] = classes - 1;
        }
        std::mem::swap(&mut cls, &mut fresh);
        shift *= 2;
    }
    (order, cls)
}

fn main() {
    let mut text = Vec::new();
    io::stdin().read_to_end(&mut text).unwrap();
    let n = text.len();
    let mut code = vec![0u8; n + 1];
    let mut letters = vec![0u32; n + 1];
    for (i, &ch) in text.iter().enumerate() {
        let letter = ch.is_ascii_lowercase();
        code[i] = match ch {
            b'a'..=b'z' => LETTER + ch - b'a',
            b'.' => DOT,
            b'@' => AT,
            _ => OTHER,
        };
        letters[i + 1] = letters[i] + letter as u32;
    }
    // around an at sign, users start no earlier than just past the last other
    // character, at or double dot, and domains end no later than just before
    // the next of them
    let mut first_start = vec![0usize; n];
    let mut last_end = vec![0usize; n];
    let mut next_at = vec![usize::MAX; n];
    let (mut barrier, mut twin) = (None, None);
    for i in 0..n {
        if code[i] == AT {
            first_start[i] = barrier.max(twin).map_or(0, |b: usize| b + 1);
        }
        if code[i] == DOT && i > 0 && code[i - 1] == DOT {
            twin = Some(i);
        }
        if code[i] == OTHER || code[i] == AT {
            barrier = Some(i);
        }
    }
    let (mut barrier, mut twin) = (n, n);
    let mut upcoming = usize::MAX;
    for i in (0..n).rev() {
        if code[i] == AT {
            last_end[i] = barrier.min(twin) - 1;
        }
        if code[i] == OTHER {
            upcoming = usize::MAX;
        }
        next_at[i] = upcoming;
        if code[i] == DOT && code[i + 1] == DOT {
            twin = i + 1;
        }
        if code[i] == OTHER || code[i] == AT {
            barrier = i;
        }
        if code[i] == AT {
            upcoming = i;
        }
    }
    let (order, rank) = suffix_array(&code);
    // being an address is a property of the string alone, so every address
    // is counted once, at the first suffix in sorted order that starts with
    // it: only prefixes longer than the common part with the suffix before
    let mut total: u64 = 0;
    let mut common = 0;
    for start in 0..n {
        let prev = order[rank[start] as usize - 1] as usize;
        while code[start + common] != 0 && code[start + common] == code[prev + common] {
            common += 1;
        }
        let lcp = common;
        common = common.saturating_sub(1);
        if code[start] < LETTER {
            continue;
        }
        let a = next_at[start];
        if a == usize::MAX || start < first_start[a] || code[a - 1] < LETTER {
            continue;
        }
        let end = last_end[a];
        if a + 1 > end || code[a + 1] < LETTER {
            continue;
        }
        let lo = (start + lcp).max(a + 1);
        if lo <= end {
            total += (letters[end + 1] - letters[lo]) as u64;
        }
    }
    println!("{}", total);
}

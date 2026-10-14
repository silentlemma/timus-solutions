use std::io::{self, Read, Write};

const LETTER_BITS: u32 = 5; // letters 1 to 26
const GAP_BITS: u32 = 4; // a place in the rest, at most 14
const CUT_BITS: u32 = 2; // 0, 1 or 2 letters deleted
const ID_SHIFT: u32 = CUT_BITS + 2 * GAP_BITS;
const ID_BITS: u32 = 13; // word numbers below 8192
const LOW_BITS: u32 = ID_BITS + ID_SHIFT;
const GAP_MASK: u32 = (1 << GAP_BITS) - 1;
const CUT_MASK: u32 = (1 << CUT_BITS) - 1;
const PAIR_MASK: u32 = (1 << (2 * GAP_BITS)) - 1;

/// The rest of a word without letters skip1 and skip2, packed with low.
fn pack(w: &[u8], skip1: usize, skip2: usize, low: u32) -> u128 {
    let mut k: u128 = 0;
    for (i, &c) in w.iter().enumerate() {
        if i != skip1 && i != skip2 {
            k = k << LETTER_BITS | (c - b'a' + 1) as u128;
        }
    }
    k << LOW_BITS | low as u128
}

fn low_of(x: u128) -> u32 {
    (x & ((1 << LOW_BITS) - 1)) as u32
}

/// Marks the words of one rest that have a close word in it.
fn mark_group(group: &[u128], found: &mut [bool]) {
    let lows: Vec<u32> = group.iter().map(|&x| low_of(x)).collect();
    if lows.iter().any(|&l| l >> (2 * GAP_BITS) & CUT_MASK == 0) {
        // the rest is a word itself, at most two deletions from every other
        for &l in &lows {
            found[(l >> ID_SHIFT) as usize] = true;
        }
        return;
    }
    let singles: Vec<u32> = lows
        .iter()
        .copied()
        .filter(|&l| l >> (2 * GAP_BITS) & CUT_MASK == 1)
        .collect();
    let mut doubles: Vec<u32> = lows
        .iter()
        .copied()
        .filter(|&l| l >> (2 * GAP_BITS) & CUT_MASK == 2)
        .collect();
    let mut gaps_with = [false; (GAP_MASK + 1) as usize];
    for &l in &singles {
        gaps_with[(l & GAP_MASK) as usize] = true;
    }
    // one deletion from each costs at most two edits
    if singles
        .iter()
        .any(|&l| l >> ID_SHIFT != singles[0] >> ID_SHIFT)
    {
        for &l in &singles {
            found[(l >> ID_SHIFT) as usize] = true;
        }
    }
    // the keys of one word differ in their gaps, so equal pairs come from different words
    doubles.sort_by_key(|&l| l & PAIR_MASK);
    let mut near_gap = [false; (GAP_MASK + 1) as usize];
    for (a, &l) in doubles.iter().enumerate() {
        let (g1, g2) = ((l >> GAP_BITS & GAP_MASK) as usize, (l & GAP_MASK) as usize);
        // the same two gaps: two substitutions
        let same = (a > 0 && doubles[a - 1] & PAIR_MASK == l & PAIR_MASK)
            || (a + 1 < doubles.len() && doubles[a + 1] & PAIR_MASK == l & PAIR_MASK);
        // one more letter in a gap shared with a single deletion
        let near = gaps_with[g1] || gaps_with[g2];
        if same || near {
            found[(l >> ID_SHIFT) as usize] = true;
        }
        if near {
            near_gap[g1] = true;
            near_gap[g2] = true;
        }
    }
    for &l in &singles {
        if near_gap[(l & GAP_MASK) as usize] {
            found[(l >> ID_SHIFT) as usize] = true;
        }
    }
}

fn main() {
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let mut it = s.split_ascii_whitespace();
    let k: usize = it.next().unwrap().parse().unwrap();
    let words: Vec<&[u8]> = (0..k).map(|_| it.next().unwrap().as_bytes()).collect();
    // two words are at most two edits apart when deleting at most two letters
    // from each leaves the same rest and, gap by gap of the rest, the larger
    // number of deleted letters adds up to at most two
    let none = usize::MAX;
    let mut keys: Vec<u128> = Vec::new();
    for (id, w) in words.iter().enumerate() {
        let n = w.len();
        let tag = (id as u32) << ID_SHIFT;
        keys.push(pack(w, none, none, tag));
        for i in 0..n {
            keys.push(pack(w, i, none, tag | 1 << (2 * GAP_BITS) | i as u32));
            // the second deleted letter, w[j + 1], sits in gap j of the rest
            for j in i..n - 1 {
                keys.push(pack(
                    w,
                    i,
                    j + 1,
                    tag | 2 << (2 * GAP_BITS) | (i as u32) << GAP_BITS | j as u32,
                ));
            }
        }
    }
    keys.sort_unstable();
    let mut found = vec![false; k];
    let mut start = 0;
    while start < keys.len() {
        let mut end = start + 1;
        while end < keys.len() && keys[end] >> LOW_BITS == keys[start] >> LOW_BITS {
            end += 1;
        }
        if end - start > 1 {
            mark_group(&keys[start..end], &mut found);
        }
        start = end;
    }
    let mut chosen: Vec<&[u8]> = (0..k).filter(|&id| found[id]).map(|id| words[id]).collect();
    chosen.sort();
    let mut out = format!("{}\n", chosen.len()).into_bytes();
    for w in chosen {
        out.extend_from_slice(w);
        out.push(b'\n');
    }
    io::stdout().write_all(&out).unwrap();
}

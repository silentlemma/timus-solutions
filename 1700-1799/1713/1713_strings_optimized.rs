use std::io::{self, BufWriter, Read, Write};

// Seven bits hold a start offset in a command of up to 100 letters.
const OFFSET_BITS: u32 = 7;
const OFFSET_MASK: u32 = (1 << OFFSET_BITS) - 1;

fn shortest_keys<'a>(words: &[&'a [u8]]) -> Vec<&'a [u8]> {
    let letters = words.iter().map(|word| word.len()).sum();
    let mut positions = Vec::with_capacity(letters);
    for (owner, word) in words.iter().enumerate() {
        for start in 0..word.len() {
            positions.push((owner as u32) << OFFSET_BITS | start as u32);
        }
    }
    let owner = |position: u32| (position >> OFFSET_BITS) as usize;
    let text = |position: u32| &words[owner(position)][(position & OFFSET_MASK) as usize..];
    positions.sort_unstable_by(|&a, &b| text(a).cmp(text(b)));

    // Keep the minimum adjacent LCP since the nearest suffix of another command.
    let mut adjacent = vec![0u8; letters];
    let mut left = vec![0u8; letters];
    let mut shared = 0;
    for (i, pair) in positions.windows(2).enumerate() {
        let (a, b) = (pair[0], pair[1]);
        let prefix = text(a)
            .iter()
            .zip(text(b))
            .take_while(|(x, y)| x == y)
            .count() as u8;
        adjacent[i + 1] = prefix;
        shared = if owner(a) != owner(b) {
            prefix
        } else {
            shared.min(prefix)
        };
        left[i + 1] = shared;
    }
    let mut best = words.to_vec();
    shared = 0;
    for (i, &position) in positions.iter().enumerate().rev() {
        let word = owner(position);
        if let Some(&next) = positions.get(i + 1) {
            let prefix = adjacent[i + 1];
            shared = if word != owner(next) {
                prefix
            } else {
                shared.min(prefix)
            };
        }
        let need = usize::from(left[i].max(shared)) + 1;
        let suffix = text(position);
        if need < best[word].len() && need <= suffix.len() {
            best[word] = &suffix[..need];
        }
    }
    best
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input.split_ascii_whitespace();
    let count = tokens.next().unwrap().parse().unwrap();
    let words: Vec<_> = tokens.take(count).map(str::as_bytes).collect();
    let mut output = BufWriter::new(io::stdout().lock());
    for key in shortest_keys(&words) {
        output.write_all(key)?;
        output.write_all(b"\n")?;
    }
    output.flush()
}

use std::io::{self, BufWriter, Read, Write};

fn counts(text: &[u8], width: usize) -> Vec<u32> {
    let size = text.len();
    if width == 1 || text.iter().all(|&letter| letter == text[0]) {
        return vec![width as u32; size];
    }

    let last_start = size + width - 2;
    let mut repeated = Vec::with_capacity(last_start + width);
    repeated.extend(text.iter().copied().cycle().take(last_start + width));
    let mut common = vec![0u16; width];
    let mut best = vec![0u16; repeated.len()];
    let mut answers = vec![0; size];
    for start in (0..=last_start).rev() {
        let letter = repeated[start];
        let mut total = width as u32;
        let end = start + width;
        // Update each diagonal and count new lengths while its maximum is in hand.
        for (distance, ((&next, length), longest)) in repeated[start..end]
            .iter()
            .zip(&mut common)
            .zip(&mut best[start..end])
            .enumerate()
            .skip(1)
        {
            *length = if letter == next { *length + 1 } else { 0 };
            *longest = (*longest).max(*length);
            total += (width - distance).saturating_sub(usize::from(*longest)) as u32;
        }
        if start < size {
            answers[start] = total;
        }
    }
    answers
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input.split_ascii_whitespace();
    let width = tokens.next().unwrap().parse().unwrap();
    let text = tokens.next().unwrap().as_bytes();
    let mut output = BufWriter::new(io::stdout().lock());
    for (position, answer) in counts(text, width).into_iter().enumerate() {
        if position != 0 {
            output.write_all(b" ")?;
        }
        write!(output, "{}", answer)?;
    }
    writeln!(output)
}

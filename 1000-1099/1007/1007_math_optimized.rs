use std::io::{self, BufRead, Write};

fn token(input: &mut impl BufRead, word: &mut Vec<u8>) -> io::Result<bool> {
    word.clear();
    loop {
        let block = input.fill_buf()?;
        if block.is_empty() {
            return Ok(!word.is_empty());
        }
        let start = if word.is_empty() {
            block
                .iter()
                .take_while(|byte| byte.is_ascii_whitespace())
                .count()
        } else {
            0
        };
        let suffix = &block[start..];
        let end = suffix.iter().position(u8::is_ascii_whitespace);
        let length = end.unwrap_or(suffix.len());
        word.extend_from_slice(&suffix[..length]);
        input.consume(start + length + usize::from(end.is_some()));
        if end.is_some() {
            return Ok(true);
        }
    }
}

fn restore(word: &mut Vec<u8>, size: usize) {
    let modulus = size + 1;
    let weight: usize = word
        .iter()
        .enumerate()
        .filter(|&(_, &byte)| byte == b'1')
        .map(|(i, _)| i + 1)
        .sum();
    let mut residue = weight % modulus;
    if word.len() == size {
        if residue != 0 {
            word[residue - 1] = b'0';
        }
    } else if word.len() < size {
        for i in (0..=word.len()).rev() {
            if residue == 0 || residue + i + 1 == modulus {
                word.insert(i, if residue == 0 { b'0' } else { b'1' });
                return;
            }
            if i > 0 && word[i - 1] == b'1' {
                residue += 1;
                if residue == modulus {
                    residue = 0;
                }
            }
        }
    } else {
        let mut position_residue = 0;
        for i in (0..word.len()).rev() {
            let one = word[i] == b'1';
            let removed = if one { position_residue } else { 0 };
            if residue == removed {
                word.remove(i);
                return;
            }
            if one {
                residue = if residue == 0 {
                    modulus - 1
                } else {
                    residue - 1
                };
            }
            position_residue = i;
        }
    }
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut word = Vec::new();
    if !token(&mut input, &mut word)? {
        return Ok(());
    }
    let size: usize = std::str::from_utf8(&word).unwrap().parse().unwrap();
    word.reserve(size + 1);
    let mut output = io::BufWriter::new(io::stdout().lock());
    while token(&mut input, &mut word)? {
        restore(&mut word, size);
        output.write_all(&word)?;
        output.write_all(b"\n")?;
    }
    output.flush()
}

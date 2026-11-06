use std::io::{self, BufRead, Write};

const DECIMAL: usize = 10;

fn token(input: &mut impl BufRead, word: &mut Vec<u8>) -> io::Result<()> {
    word.clear();
    loop {
        let block = input.fill_buf()?;
        if block.is_empty() {
            return Ok(());
        }
        let start = if word.is_empty() {
            block
                .iter()
                .take_while(|byte| byte.is_ascii_whitespace())
                .count()
        } else {
            0
        };
        let tail = &block[start..];
        let end = tail.iter().position(u8::is_ascii_whitespace);
        let length = end.unwrap_or(tail.len());
        word.extend_from_slice(&tail[..length]);
        input.consume(start + length + usize::from(end.is_some()));
        if end.is_some() {
            return Ok(());
        }
    }
}

fn number(input: &mut impl BufRead, word: &mut Vec<u8>) -> io::Result<usize> {
    token(input, word)?;
    Ok(word.iter().fold(0, |value, &digit| {
        value * DECIMAL + usize::from(digit - b'0')
    }))
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut word = Vec::new();
    let size = number(&mut input, &mut word)?;
    let mut menu = Vec::with_capacity(size);
    for _ in 0..size {
        token(&mut input, &mut word)?;
        menu.push(word.clone());
    }
    menu.sort_unstable();
    menu.dedup();
    let students = number(&mut input, &mut word)?;
    let mut safe_count = menu.len();
    let mut safe = vec![true; safe_count];
    let mut seen = vec![usize::MAX; safe_count];
    let mut risks = vec![0; students + 1];
    for (student, risk) in risks.iter_mut().enumerate() {
        let count = number(&mut input, &mut word)?;
        for _ in 0..count {
            token(&mut input, &mut word)?;
            let Ok(item) = menu.binary_search(&word) else {
                continue;
            };
            if !safe[item] || seen[item] == student {
                continue;
            }
            seen[item] = student;
            if student == 0 {
                safe[item] = false;
                safe_count -= 1;
            } else {
                *risk += 1;
            }
        }
    }
    let meal = number(&mut input, &mut word)?;
    let mut output = Vec::new();
    for risk in risks.into_iter().skip(1) {
        output.extend_from_slice(if meal == 0 || risk == 0 {
            b"YES\n"
        } else if safe_count - risk < meal {
            b"NO\n"
        } else {
            b"MAYBE\n"
        });
    }
    io::stdout().lock().write_all(&output)
}

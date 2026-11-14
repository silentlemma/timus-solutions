use std::io::{self, BufRead, BufWriter, Write};

fn states(text: &[u8]) -> Vec<u32> {
    let mut state = vec![0; text.len() + 1];
    let mut current = 0;
    for (index, &letter) in text.iter().enumerate() {
        // The state is the index after its creating character. For an opener,
        // the previous prefix already holds the parent state.
        current = if current != 0
            && text[current - 1] == letter.to_ascii_uppercase()
            && letter.is_ascii_lowercase()
        {
            state[current - 1] as usize
        } else {
            index + 1
        };
        state[index + 1] = current as u32;
    }
    state
}

fn number(input: &mut impl BufRead) -> usize {
    let mut value = 0;
    let mut started = false;
    loop {
        let bytes = input.fill_buf().unwrap();
        if bytes.is_empty() {
            return value;
        }
        let mut consumed = 0;
        for &byte in bytes {
            consumed += 1;
            if byte.is_ascii_digit() {
                value = value * 10 + usize::from(byte - b'0');
                started = true;
            } else if started {
                input.consume(consumed);
                return value;
            }
        }
        input.consume(consumed);
    }
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut text = String::new();
    input.read_line(&mut text)?;
    let state = states(text.trim().as_bytes());
    let queries = number(&mut input);
    let mut output = BufWriter::new(io::stdout().lock());
    for _ in 0..queries {
        let left = number(&mut input);
        let right = number(&mut input);
        let answer = if state[left - 1] == state[right] {
            b"1"
        } else {
            b"0"
        };
        output.write_all(answer)?;
    }
    output.write_all(b"\n")?;
    output.flush()
}

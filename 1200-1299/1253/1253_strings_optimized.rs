use std::io::{self, BufWriter, Read, Write};

const LIMIT: usize = 1_000_000;

enum Piece<'a> {
    Text(&'a [u8]),
    Reference(usize),
}

fn pieces(text: &[u8]) -> Vec<Piece<'_>> {
    let mut parts = text.split(|&byte| byte == b'*');
    let first = parts.next().unwrap();
    let mut result = Vec::new();
    if !first.is_empty() {
        result.push(Piece::Text(first));
    }
    for part in parts {
        result.push(Piece::Reference(usize::from(part[0] - b'0')));
        if part.len() > 1 {
            result.push(Piece::Text(&part[1..]));
        }
    }
    result
}

fn measure(index: usize, templates: &[Vec<Piece<'_>>], lengths: &mut [Option<usize>]) -> usize {
    if let Some(length) = lengths[index] {
        return length;
    }
    // Reentering an unfinished template is equivalent to exceeding the limit.
    lengths[index] = Some(LIMIT + 1);
    let mut length = 0;
    for part in &templates[index] {
        length += match part {
            Piece::Text(text) => text.len(),
            Piece::Reference(next) => measure(*next, templates, lengths),
        };
        if length > LIMIT {
            return LIMIT + 1;
        }
    }
    lengths[index] = Some(length);
    length
}

fn emit(
    index: usize,
    templates: &[Vec<Piece<'_>>],
    lengths: &[Option<usize>],
    output: &mut impl Write,
) -> io::Result<()> {
    for part in &templates[index] {
        match part {
            Piece::Text(text) => output.write_all(text)?,
            Piece::Reference(next) if lengths[*next] != Some(0) => {
                emit(*next, templates, lengths, output)?;
            }
            Piece::Reference(_) => (),
        }
    }
    Ok(())
}

fn main() -> io::Result<()> {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input)?;
    input.retain(|&byte| byte != b'\r');
    let newline = input.iter().position(|&byte| byte == b'\n').unwrap();
    let count: usize = std::str::from_utf8(&input[..newline])
        .unwrap()
        .trim()
        .parse()
        .unwrap();
    let mut templates = Vec::with_capacity(count + 1);
    templates.push(Vec::new());
    for (i, text) in input[newline + 1..]
        .split(|&byte| byte == b'#')
        .take(count)
        .enumerate()
    {
        let text = if i == 0 {
            text
        } else {
            text.strip_prefix(b"\n").unwrap_or(text)
        };
        templates.push(pieces(text));
    }
    let mut lengths = vec![None; count + 1];
    let stdout = io::stdout();
    let mut output = BufWriter::new(stdout.lock());
    if measure(1, &templates, &mut lengths) > LIMIT {
        output.write_all(b"#\n")?;
    } else {
        emit(1, &templates, &lengths, &mut output)?;
        output.write_all(b"\n")?;
    }
    output.flush()
}

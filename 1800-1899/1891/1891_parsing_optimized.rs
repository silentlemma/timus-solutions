use std::io::{self, BufRead, Cursor, Write};

const MAX_DECLARATIONS: usize = 100;
const MAX_NAME: usize = 20;
const TYPE_NAMES: [&[u8]; 4] = [b"auto", b"int", b"real", b"string"];
const SEPARATOR: &[u8] = b" : ";
const OUTPUT_SIZE: usize = MAX_DECLARATIONS * (MAX_NAME + SEPARATOR.len() + b"string".len() + 1);
const TABLE_SIZE: usize = 128;
const MULTIPLIER: u64 = 11_400_714_819_323_198_485;
const TABLE_SHIFT: u32 = u64::BITS - TABLE_SIZE.trailing_zeros();
const LETTER_BITS: u32 = 6;
const TYPE_BITS: u32 = 2;
const INTEGER: u8 = 1;
const REAL: u8 = 2;
const TEXT: u8 = 3;

struct Symbols {
    names: [u128; TABLE_SIZE],
    arguments: [u32; TABLE_SIZE],
    types: [u8; TABLE_SIZE],
}

impl Symbols {
    fn new() -> Self {
        Self {
            names: [0; TABLE_SIZE],
            arguments: [0; TABLE_SIZE],
            types: [0; TABLE_SIZE],
        }
    }

    fn slot(&self, name: u128, arguments: u32) -> usize {
        let high = (name >> u64::BITS) as u64;
        let hash = (name as u64 ^ high.wrapping_mul(MULTIPLIER)).wrapping_add(u64::from(arguments));
        let mut index = (hash.wrapping_mul(MULTIPLIER) >> TABLE_SHIFT) as usize;
        while self.types[index] != 0
            && (self.names[index], self.arguments[index]) != (name, arguments)
        {
            index = (index + 1) & (TABLE_SIZE - 1);
        }
        index
    }

    fn insert(&mut self, slot: usize, name: u128, arguments: u32, kind: u8) {
        self.names[slot] = name;
        self.arguments[slot] = arguments;
        self.types[slot] = kind;
    }

    fn get(&self, name: u128, arguments: u32) -> u8 {
        self.types[self.slot(name, arguments)]
    }
}

fn pack(word: &[u8]) -> u128 {
    word.iter().fold(0, |name, &letter| {
        let digit = if letter.is_ascii_lowercase() {
            letter - b'a' + 1
        } else {
            letter - b'A' + 1 + (b'z' - b'a' + 1)
        };
        (name << LETTER_BITS) | u128::from(digit)
    })
}

fn words(line: &[u8]) -> impl Iterator<Item = &[u8]> {
    line.split(|byte| !byte.is_ascii_alphabetic())
        .filter(|word| !word.is_empty())
}

fn kind(word: &[u8]) -> u8 {
    match word {
        b"int" => INTEGER,
        b"real" => REAL,
        b"string" => TEXT,
        _ => 0,
    }
}

fn read_line(input: &mut impl BufRead, line: &mut Vec<u8>) -> io::Result<()> {
    line.clear();
    input.read_until(b'\n', line)?;
    Ok(())
}

fn count(line: &[u8]) -> usize {
    std::str::from_utf8(line).unwrap().trim().parse().unwrap()
}

fn main() -> io::Result<()> {
    const LINE_CAPACITY: usize = 512;
    let mut input = io::stdin().lock();
    let mut output = io::stdout().lock();
    let mut line = Vec::with_capacity(LINE_CAPACITY);
    let mut functions = Symbols::new();
    let mut variables = Symbols::new();

    read_line(&mut input, &mut line)?;
    for _ in 0..count(&line) {
        read_line(&mut input, &mut line)?;
        let mut tokens = words(&line);
        let name = pack(tokens.next().unwrap());
        let mut result = kind(tokens.next().unwrap());
        let mut arguments = 0;
        for token in tokens {
            arguments = (arguments << TYPE_BITS) | u32::from(result);
            result = kind(token);
        }
        let slot = functions.slot(name, arguments);
        functions.insert(slot, name, arguments, result);
    }

    let mut buffer = [0; OUTPUT_SIZE];
    let mut inferred = Cursor::new(&mut buffer[..]);
    read_line(&mut input, &mut line)?;
    for number in 1..=count(&line) {
        read_line(&mut input, &mut line)?;
        let mut tokens = words(&line);
        let declared = kind(tokens.next().unwrap());
        let word = tokens.next().unwrap();
        let variable = pack(word);
        let target = variables.slot(variable, 0);
        if variables.types[target] != 0 {
            return writeln!(output, "Error on line {number}: Double declaration");
        }
        let function = pack(tokens.next().unwrap());
        let mut arguments = 0;
        for token in tokens {
            let arg = variables.get(pack(token), 0);
            if arg == 0 {
                return writeln!(output, "Error on line {number}: Unknown variable");
            }
            arguments = (arguments << TYPE_BITS) | u32::from(arg);
        }
        let result = functions.get(function, arguments);
        if result == 0 {
            return writeln!(output, "Error on line {number}: No such function");
        }
        if declared != 0 && declared != result {
            return writeln!(output, "Error on line {number}: Invalid initialization");
        }
        variables.insert(target, variable, 0, result);
        if declared == 0 {
            inferred.write_all(word)?;
            inferred.write_all(SEPARATOR)?;
            inferred.write_all(TYPE_NAMES[usize::from(result)])?;
            inferred.write_all(b"\n")?;
        }
    }
    let used = inferred.position() as usize;
    output.write_all(&buffer[..used])
}

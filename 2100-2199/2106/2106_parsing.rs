use std::collections::HashMap;
use std::fmt::Write as FormatWrite;
use std::io::{self, Read, Write};

const WORD_BYTES: usize = 4;
const BITS_PER_BYTE: u32 = 8;
const HEX_RADIX: u32 = 16;

#[derive(Clone, Copy)]
enum Field {
    Integer,
    Text,
    Structure(usize),
}

struct Structure {
    name: String,
    fields: Vec<Field>,
}

fn read_number(data: &[u8], position: &mut usize) -> u32 {
    let mut value = 0;
    for &byte in &data[*position..*position + WORD_BYTES] {
        value = (value << BITS_PER_BYTE) | u32::from(byte);
    }
    *position += WORD_BYTES;
    value
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let mut header = lines.next().unwrap().split_whitespace();
    header.next();
    let line_count: usize = header.next().unwrap().parse().unwrap();
    let mut structures: Vec<Structure> = Vec::new();
    let mut type_ids = HashMap::new();
    for _ in 0..line_count {
        let mut tokens = lines.next().unwrap().split_whitespace();
        let token = tokens.next().unwrap();
        if token == "struct" {
            let name = tokens.next().unwrap().to_owned();
            type_ids.insert(name.clone(), structures.len());
            structures.push(Structure {
                name,
                fields: Vec::new(),
            });
        } else {
            let field = match token {
                "int" => Field::Integer,
                "string" => Field::Text,
                name => Field::Structure(type_ids[name]),
            };
            structures.last_mut().unwrap().fields.push(field);
        }
    }

    let hex = lines.next().unwrap().trim().as_bytes();
    let data: Vec<u8> = hex
        .chunks_exact(2)
        .map(|pair| {
            let high = char::from(pair[0]).to_digit(HEX_RADIX).unwrap();
            let low = char::from(pair[1]).to_digit(HEX_RADIX).unwrap();
            (high * HEX_RADIX + low) as u8
        })
        .collect();
    let mut position = 0;
    let mut output = String::new();
    while position < data.len() {
        let root = read_number(&data, &mut position) as usize - 1;
        writeln!(output, "{}", structures[root].name).unwrap();
        let mut stack = vec![(root, 0)];
        while let Some(&(structure, next_field)) = stack.last() {
            if next_field == structures[structure].fields.len() {
                stack.pop();
                continue;
            }
            let field = structures[structure].fields[next_field];
            stack.last_mut().unwrap().1 += 1;
            for _ in 0..stack.len() {
                output.push(' ');
            }
            match field {
                Field::Integer => {
                    let value = read_number(&data, &mut position);
                    writeln!(output, "int {}", value).unwrap();
                }
                Field::Text => {
                    let length = read_number(&data, &mut position) as usize;
                    let text = std::str::from_utf8(&data[position..position + length]).unwrap();
                    writeln!(output, "string {}", text).unwrap();
                    position += length;
                }
                Field::Structure(child) => {
                    writeln!(output, "{}", structures[child].name).unwrap();
                    stack.push((child, 0));
                }
            }
        }
    }
    io::stdout().lock().write_all(output.as_bytes()).unwrap();
}

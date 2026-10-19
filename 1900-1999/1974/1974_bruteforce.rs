use std::io::{self, Read};

const OCTAVE_SIZE: usize = 12;
const PITCH_COUNT: usize = 96;
const NATURAL_SCALE: &[u8] = b"C D EF G A B";

fn parse_note(token: &str) -> usize {
    let bytes = token.as_bytes();
    let mut pitch = (bytes[0] - b'1') as usize * OCTAVE_SIZE;
    pitch += NATURAL_SCALE
        .iter()
        .position(|&note| note == bytes[1])
        .unwrap();
    if bytes.len() > 2 {
        if bytes[2] == b'+' {
            pitch += 1;
        } else {
            pitch -= 1;
        }
    }
    pitch
}

fn absolute_similarity(positions: &[Vec<usize>], source_length: usize, song: &[usize]) -> usize {
    let mut counts = vec![0; source_length + song.len() - 1];
    for (j, &pitch) in song.iter().enumerate() {
        let offset = song.len() - 1 - j;
        for &i in &positions[pitch] {
            counts[i + offset] += 1;
        }
    }
    counts.into_iter().max().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut positions = vec![Vec::new(); PITCH_COUNT];
    for i in 0..n {
        positions[parse_note(tokens.next().unwrap())].push(i);
    }
    let melodies: usize = tokens.next().unwrap().parse().unwrap();
    let mut output = String::new();
    for _ in 0..melodies {
        let length: usize = tokens.next().unwrap().parse().unwrap();
        let song: Vec<usize> = (0..length)
            .map(|_| parse_note(tokens.next().unwrap()))
            .collect();
        let best = absolute_similarity(&positions, n, &song);
        output.push_str(&format!("{:.12}\n", best as f64 / length as f64));
    }
    print!("{output}");
}

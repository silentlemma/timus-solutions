use std::io::{self, Read};

const CUBE_FACES: usize = 6;
const RING_SIZE: usize = 4;
const BYTE_VALUES: usize = 256;

const COLOURS: usize = 10;
const RINGS: usize = COLOURS.pow(4);
// One ring for each choice of opposite faces as the top and bottom.
const SIDES: [[usize; 4]; 3] = [[0, 1, 3, 2], [4, 1, 5, 2], [0, 4, 3, 5]];

fn key(cube: &[usize; CUBE_FACES], faces: [usize; RING_SIZE]) -> usize {
    let ring = faces.map(|face| cube[face]);
    let start = (0..ring.len()).min_by_key(|&i| ring[i]).unwrap();
    let a = ring[start];
    let b = ring[(start + 1) % ring.len()];
    let c = ring[(start + 2) % ring.len()];
    let d = ring[(start + RING_SIZE - 1) % ring.len()];
    // Rotate to the least colour, then take the smaller of the two directions.
    ((a * COLOURS + b.min(d)) * COLOURS + c) * COLOURS + b.max(d)
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace();
    let n = words.next().unwrap().parse::<usize>().unwrap();
    let mut ids = [u8::MAX; BYTE_VALUES];
    let mut next_id = 0;
    let mut counts = [0u16; RINGS];
    let mut best = 0;
    for token in words.take(n) {
        let mut cube = [0; CUBE_FACES];
        for (face, colour) in cube.iter_mut().zip(token.bytes()) {
            let id = &mut ids[usize::from(colour)];
            if *id == u8::MAX {
                *id = next_id;
                next_id += 1;
            }
            *face = usize::from(*id);
        }
        for faces in SIDES {
            let count = &mut counts[key(&cube, faces)];
            *count += 1;
            best = best.max(*count);
        }
    }
    println!("{}", best);
}

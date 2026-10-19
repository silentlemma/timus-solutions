use std::io::{self, Read};

const SIDE: usize = 4;
const TURNS: usize = 4;
const HALF: usize = SIDE / 2;
// position of each quadrant (top left, top right, bottom left, bottom right)
// in the order a quarter turn moves a square through them
const RING: [[usize; 2]; 2] = [[0, 1], [TURNS - 1, 2]];

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let cells: Vec<u32> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let mut count = [0usize; TURNS];
    for (k, &colour) in cells.iter().enumerate() {
        if colour == 1 {
            count[RING[k / SIDE / HALF][k % SIDE / HALF]] += 1;
        }
    }
    // every layer holds one square of each colour, one per quadrant; the
    // cube is solved when the colour 1 squares of all layers share a quadrant
    let best = (0..TURNS)
        .map(|t| {
            (0..TURNS)
                .map(|p| {
                    let d = (p + TURNS - t) % TURNS;
                    count[p] * d.min(TURNS - d)
                })
                .sum::<usize>()
        })
        .min()
        .unwrap();
    println!("{}", best);
}

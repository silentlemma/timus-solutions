use std::io::{self, Read};

const SIZE: usize = 4;

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let rows: Vec<&[u8]> = text.split_ascii_whitespace().map(|w| w.as_bytes()).collect();
    let mut grille: Vec<Vec<u8>> = rows[..SIZE].iter().map(|r| r.to_vec()).collect();
    let square = &rows[SIZE..2 * SIZE];
    let mut password = String::new();
    // read the windows row by row, then turn the grille clockwise:
    // the cell (r, c) of the turned grille is (SIZE - 1 - c, r) of the old one
    for _ in 0..SIZE {
        for r in 0..SIZE {
            for c in 0..SIZE {
                if grille[r][c] == b'X' {
                    password.push(square[r][c] as char);
                }
            }
        }
        grille = (0..SIZE)
            .map(|r| (0..SIZE).map(|c| grille[SIZE - 1 - c][r]).collect())
            .collect();
    }
    println!("{}", password);
}

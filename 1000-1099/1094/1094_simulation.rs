use std::io::{self, BufRead};

const WIDTH: i32 = 80;

fn main() {
    let mut line = String::new();
    io::stdin().lock().read_line(&mut line).unwrap();
    let mut screen = vec![b' '; WIDTH as usize];
    let mut cursor: i32 = 0;
    for key in line.trim_end_matches(['\r', '\n']).bytes() {
        match key {
            b'<' => cursor -= 1,
            b'>' => cursor += 1,
            _ => {
                screen[cursor as usize] = key;
                cursor += 1;
            }
        }
        // past either edge the cursor jumps to the leftmost position
        if !(0..WIDTH).contains(&cursor) {
            cursor = 0;
        }
    }
    println!("{}", String::from_utf8(screen).unwrap());
}

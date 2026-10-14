use std::io::{self, Read};

// the places a stick can take in one cell of the picture
const TOP: u32 = 1;
const MIDDLE: u32 = 1 << 1;
const BOTTOM: u32 = 1 << 2;
const UPPER_LEFT: u32 = 1 << 3;
const UPPER_RIGHT: u32 = 1 << 4;
const LOWER_LEFT: u32 = 1 << 5;
const LOWER_RIGHT: u32 = 1 << 6;
const UPPER_SLASH: u32 = 1 << 7;
const LOWER_SLASH: u32 = 1 << 8;
const PLUS_UPRIGHT: u32 = 1 << 9;
const EQUAL_UPPER: u32 = 1 << 10;
const EQUAL_LOWER: u32 = 1 << 11;
const SIDES: u32 = UPPER_LEFT | UPPER_RIGHT | LOWER_LEFT | LOWER_RIGHT;
const DIGIT_SHAPE: [u32; 10] = [
    TOP | SIDES | BOTTOM,
    UPPER_SLASH | UPPER_RIGHT | LOWER_RIGHT,
    TOP | UPPER_RIGHT | LOWER_SLASH | BOTTOM,
    TOP | UPPER_SLASH | MIDDLE | LOWER_SLASH,
    UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_RIGHT,
    TOP | UPPER_LEFT | MIDDLE | LOWER_RIGHT | BOTTOM,
    UPPER_SLASH | MIDDLE | LOWER_LEFT | LOWER_RIGHT | BOTTOM,
    TOP | UPPER_SLASH | LOWER_LEFT,
    TOP | SIDES | MIDDLE | BOTTOM,
    TOP | UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_SLASH,
];
const PLUS_SHAPE: u32 = MIDDLE | PLUS_UPRIGHT; // the bar lies where a middle stick does
const EQUAL_SHAPE: u32 = EQUAL_UPPER | EQUAL_LOWER;
const LONGEST: usize = 8; // digits in a number
const BASE: usize = 10;

fn shape_of(c: u8) -> u32 {
    match c {
        b'+' => PLUS_SHAPE,
        b'=' => EQUAL_SHAPE,
        _ => DIGIT_SHAPE[(c - b'0') as usize],
    }
}

fn sticks(shape: u32) -> usize {
    shape.count_ones() as usize
}

/// The best way to reach a state: sticks kept in place, the digits of the
/// last column and the previous state.
#[derive(Clone, Copy)]
struct Step {
    kept: usize,
    dx: usize,
    dy: usize,
    dz: usize,
    carry: usize,
    used: usize,
}

fn solve(text: &[u8], k: usize) -> String {
    let n = text.len();
    let cells: Vec<u32> = text.iter().map(|&c| shape_of(c)).collect();
    let total: usize = cells.iter().map(|&s| sticks(s)).sum();
    let kept = |pos: usize, shape: u32| sticks(cells[pos] & shape);
    for len_x in 1..=LONGEST {
        for len_y in 1..=LONGEST {
            if len_x + len_y + 2 >= n {
                continue;
            }
            let len_z = n - 2 - len_x - len_y;
            // no leading zeros, so z has at least as many digits as x and y
            if len_z < len_x.max(len_y) || len_z > LONGEST {
                continue;
            }
            let (plus, equal) = (len_x, len_x + len_y + 1);
            // table[col][carry][used]: the best way to fill col columns from the right
            let mut table =
                vec![[vec![None::<Step>; total + 1], vec![None::<Step>; total + 1]]; len_z + 1];
            table[0][0][sticks(PLUS_SHAPE) + sticks(EQUAL_SHAPE)] = Some(Step {
                kept: kept(plus, PLUS_SHAPE) + kept(equal, EQUAL_SHAPE),
                dx: 0,
                dy: 0,
                dz: 0,
                carry: 0,
                used: 0,
            });
            for col in 0..len_z {
                let pos_x = if col < len_x {
                    Some(len_x - 1 - col)
                } else {
                    None
                };
                let pos_y = if col < len_y {
                    Some(len_x + len_y - col)
                } else {
                    None
                };
                let pos_z = n - 1 - col;
                for carry in 0..2 {
                    for used in 0..=total {
                        let have = match table[col][carry][used] {
                            Some(s) => s.kept,
                            None => continue,
                        };
                        for dx in 0..if pos_x.is_some() { BASE } else { 1 } {
                            if pos_x.is_some() && dx == 0 && col == len_x - 1 && len_x > 1 {
                                continue;
                            }
                            for dy in 0..if pos_y.is_some() { BASE } else { 1 } {
                                if pos_y.is_some() && dy == 0 && col == len_y - 1 && len_y > 1 {
                                    continue;
                                }
                                let (dz, out) =
                                    ((dx + dy + carry) % BASE, (dx + dy + carry) / BASE);
                                if dz == 0 && col == len_z - 1 && len_z > 1 {
                                    continue;
                                }
                                let mut more = sticks(DIGIT_SHAPE[dz]);
                                let mut gain = kept(pos_z, DIGIT_SHAPE[dz]);
                                if let Some(p) = pos_x {
                                    more += sticks(DIGIT_SHAPE[dx]);
                                    gain += kept(p, DIGIT_SHAPE[dx]);
                                }
                                if let Some(p) = pos_y {
                                    more += sticks(DIGIT_SHAPE[dy]);
                                    gain += kept(p, DIGIT_SHAPE[dy]);
                                }
                                if used + more > total {
                                    continue;
                                }
                                let next = &mut table[col + 1][out][used + more];
                                if next.map_or(true, |s| s.kept < have + gain) {
                                    *next = Some(Step {
                                        kept: have + gain,
                                        dx,
                                        dy,
                                        dz,
                                        carry,
                                        used,
                                    });
                                }
                            }
                        }
                    }
                }
            }
            // every stick must be used, and the moved ones are those not kept
            match table[len_z][0][total] {
                Some(s) if total - s.kept <= k => {}
                _ => continue,
            }
            let (mut x, mut y, mut z) = (vec![b'0'; len_x], vec![b'0'; len_y], vec![b'0'; len_z]);
            let (mut carry, mut used) = (0, total);
            for col in (1..=len_z).rev() {
                let s = table[col][carry][used].unwrap();
                let c = col - 1;
                if c < len_x {
                    x[len_x - 1 - c] = b'0' + s.dx as u8;
                }
                if c < len_y {
                    y[len_y - 1 - c] = b'0' + s.dy as u8;
                }
                z[len_z - 1 - c] = b'0' + s.dz as u8;
                carry = s.carry;
                used = s.used;
            }
            let text = |v: Vec<u8>| String::from_utf8(v).unwrap();
            return format!("{}+{}={}", text(x), text(y), text(z));
        }
    }
    "Impossible".to_string()
}

fn main() {
    // the expression may be written with spaces, K comes last
    let mut s = String::new();
    io::stdin().read_to_string(&mut s).unwrap();
    let tokens: Vec<&str> = s.split_ascii_whitespace().collect();
    let k: usize = tokens[tokens.len() - 1].parse().unwrap();
    println!(
        "{}",
        solve(tokens[..tokens.len() - 1].concat().as_bytes(), k)
    );
}

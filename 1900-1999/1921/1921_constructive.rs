use std::io::{self, Read};

fn construct_board(
    rows: usize,
    columns: usize,
    palette: usize,
    level: usize,
) -> Option<Vec<String>> {
    let target = level - 1;
    let longest = rows.max(columns);
    let row_colors = rows.min(2);
    let column_colors = columns.min(2);
    if longest < target
        || (palette == 1 && longest != target)
        || (palette > 1 && target == 1 && palette < row_colors * column_colors)
    {
        return None;
    }
    let mut board = Vec::with_capacity(rows);
    for row in 0..rows {
        let mut line = String::with_capacity(columns);
        for column in 0..columns {
            let color = if palette == 1 {
                0
            } else if target == 1 {
                (row % 2) * column_colors + column % 2
            } else if columns >= target {
                (row + column / target) % 2
            } else {
                (column + row / target) % 2
            };
            line.push((b'A' + color as u8) as char);
        }
        board.push(line);
    }
    Some(board)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let rows = tokens.next().unwrap().parse().unwrap();
    let columns = tokens.next().unwrap().parse().unwrap();
    let palette = tokens.next().unwrap().parse().unwrap();
    let level = tokens.next().unwrap().parse().unwrap();
    if let Some(board) = construct_board(rows, columns, palette, level) {
        println!("YES\n{}", board.join("\n"));
    } else {
        println!("NO");
    }
}

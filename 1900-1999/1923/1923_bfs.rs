use std::io::{self, Read};

fn expand(
    player: usize,
    color: u8,
    neighbors: &[Vec<usize>],
    colors: &[u8],
    owners: &mut [i8],
    territories: &mut [Vec<usize>; 2],
) {
    let mut cursor = 0;
    while cursor < territories[player].len() {
        let cell = territories[player][cursor];
        for &adjacent in &neighbors[cell] {
            if owners[adjacent] == -1 && colors[adjacent] == color {
                owners[adjacent] = player as i8;
                territories[player].push(adjacent);
            }
        }
        cursor += 1;
    }
}

fn territory_sizes(board: &[String], moves: &[usize]) -> (usize, usize) {
    let rows = board.len();
    let columns = board[0].len();
    let cells = rows * columns;
    let colors: Vec<u8> = board.iter().flat_map(|row| row.bytes()).collect();
    let mut neighbors = vec![Vec::new(); cells];
    for row in 0..rows {
        for column in 0..columns {
            let cell = row * columns + column;
            if row > 0 {
                neighbors[cell].push(cell - columns);
            }
            if row + 1 < rows {
                neighbors[cell].push(cell + columns);
            }
            if column > 0 {
                neighbors[cell].push(cell - 1);
            }
            if column + 1 < columns {
                neighbors[cell].push(cell + 1);
            }
        }
    }
    let mut owners = vec![-1; cells];
    let mut territories = [Vec::new(), Vec::new()];
    for (player, &seed) in [cells - columns, columns - 1].iter().enumerate() {
        owners[seed] = player as i8;
        territories[player].push(seed);
        expand(
            player,
            colors[seed],
            &neighbors,
            &colors,
            &mut owners,
            &mut territories,
        );
    }
    for (turn, &color) in moves.iter().enumerate() {
        expand(
            turn % 2,
            b'0' + color as u8,
            &neighbors,
            &colors,
            &mut owners,
            &mut territories,
        );
    }
    (territories[0].len(), territories[1].len())
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let rows = tokens.next().unwrap().parse::<usize>().unwrap();
    let _columns = tokens.next().unwrap().parse::<usize>().unwrap();
    let board: Vec<String> = (0..rows)
        .map(|_| tokens.next().unwrap().to_string())
        .collect();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let moves: Vec<usize> = (0..count)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let (first, second) = territory_sizes(&board, &moves);
    println!("{}\n{}", first, second);
}

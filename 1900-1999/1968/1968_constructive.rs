use std::io::{self, Read};

const BLOCK_SIDE: usize = 2;

fn reconstruct(photo: &[Vec<i32>]) -> Vec<Vec<String>> {
    let (rows, columns) = (photo.len(), photo[0].len());
    let mut counts = vec![vec![0; columns]; rows];
    for row in 0..rows {
        for column in 0..columns {
            let mut value = photo[row][column];
            if row > 0 {
                value -= counts[row - 1][column];
            }
            if column > 0 {
                value -= counts[row][column - 1];
            }
            if row > 0 && column > 0 {
                value -= counts[row - 1][column - 1];
            }
            counts[row][column] = value;
        }
    }
    let mut layers = Vec::new();
    for level in 0..rows.min(columns) / BLOCK_SIDE {
        let mut layer = Vec::new();
        for row in 0..rows / BLOCK_SIDE - level {
            let mut line = String::new();
            for column in 0..columns / BLOCK_SIDE - level {
                let (x, y) = (level + BLOCK_SIDE * row, level + BLOCK_SIDE * column);
                line.push(if counts[x][y] > (level / BLOCK_SIDE) as i32 {
                    'R'
                } else {
                    'W'
                });
            }
            layer.push(line);
        }
        layers.push(layer);
    }
    layers
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let rows: usize = words.next().unwrap().parse().unwrap();
    let columns: usize = words.next().unwrap().parse().unwrap();
    let photo: Vec<Vec<i32>> = (0..rows)
        .map(|_| {
            words
                .by_ref()
                .take(columns)
                .map(|word| word.parse().unwrap())
                .collect()
        })
        .collect();
    let layers = reconstruct(&photo);
    let output = layers
        .iter()
        .map(|layer| layer.join("\n"))
        .collect::<Vec<_>>()
        .join("\n\n");
    println!("{}", output);
}

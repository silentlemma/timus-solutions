use std::io::{self, Read};

const INFINITY: i32 = 1 << 20;

fn maximum_saved(matrix: &[u8], n: usize) -> i32 {
    let stride = n + 1;
    let mut row_price = vec![0; stride];
    let mut col_price = vec![0; stride];
    let mut owner = vec![0; stride];
    let mut previous = vec![0; stride];
    let mut unmatched = Vec::with_capacity(n);

    // Initial row potentials make every row maximum a tight edge.
    for (row, amounts) in matrix.chunks_exact(stride).enumerate().skip(1) {
        let largest = *amounts[1..].iter().max().unwrap();
        row_price[row] = -i32::from(largest);
        let free = (1..=n).find(|&col| owner[col] == 0 && amounts[col] == largest);
        if let Some(col) = free {
            owner[col] = row;
        } else {
            unmatched.push(row);
        }
    }

    let mut slack = vec![INFINITY; stride];
    let mut remaining = vec![0; n];
    let mut visited = Vec::with_capacity(n);
    for row in unmatched {
        owner[0] = row;
        let (mut col, mut left) = (0, n);
        visited.clear();
        slack.fill(INFINITY);
        for (index, entry) in remaining.iter_mut().enumerate() {
            *entry = index + 1;
        }

        loop {
            visited.push(col);
            let active_row = owner[col];
            let amounts = &matrix[active_row * stride..(active_row + 1) * stride];
            let (mut delta, mut best) = (INFINITY, 0);
            for (index, &j) in remaining[..left].iter().enumerate() {
                let reduced = -i32::from(amounts[j]) - row_price[active_row] - col_price[j];
                if reduced < slack[j] {
                    slack[j] = reduced;
                    previous[j] = col;
                }
                if slack[j] < delta
                    || (slack[j] == delta && owner[j] == 0 && owner[remaining[best]] != 0)
                {
                    delta = slack[j];
                    best = index;
                }
            }
            if delta != 0 {
                for &j in &visited {
                    row_price[owner[j]] += delta;
                    col_price[j] -= delta;
                }
                for &j in &remaining[..left] {
                    slack[j] -= delta;
                }
            }
            col = remaining[best];
            if owner[col] == 0 {
                break;
            }
            left -= 1;
            remaining[best] = remaining[left];
        }

        while col != 0 {
            let prior = previous[col];
            owner[col] = owner[prior];
            col = prior;
        }
    }

    (1..=n)
        .map(|col| i32::from(matrix[owner[col] * stride + col]))
        .sum()
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let stride = n + 1;
    let mut matrix = vec![0u8; stride * stride];
    let mut total = 0;
    for row in matrix.chunks_exact_mut(stride).skip(1) {
        for cell in &mut row[1..] {
            *cell = tokens.next().unwrap().parse().unwrap();
            total += i32::from(*cell);
        }
    }
    println!("{}", total - maximum_saved(&matrix, n));
    Ok(())
}

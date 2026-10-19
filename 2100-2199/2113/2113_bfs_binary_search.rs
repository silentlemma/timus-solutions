use std::io::{self, Read};

const MAX_HEIGHT: i32 = 100_000;
const INF: i32 = i32::MAX;

fn can_escape(
    heights: &[i32],
    flood: &[i32],
    stride: usize,
    start: usize,
    jump: i32,
    distance: &mut [i32],
    queue: &mut [usize],
) -> bool {
    distance.fill(-1);
    distance[start] = 0;
    queue[0] = start;
    let mut head = 0;
    let mut tail = 1;
    while head < tail {
        let cell = queue[head];
        head += 1;
        if flood[cell] == INF {
            return true;
        }
        let arrival = distance[cell] + 1;
        for next in [cell - stride, cell - 1, cell + 1, cell + stride] {
            if distance[next] == -1
                && arrival < flood[next]
                && heights[next] - heights[cell] <= jump
            {
                distance[next] = arrival;
                queue[tail] = next;
                tail += 1;
            }
        }
    }
    false
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let rows = values.next().unwrap();
    let columns = values.next().unwrap();
    let stride = columns + 2;
    let size = (rows + 2) * stride;
    let mut heights = vec![0; size];
    let mut flood = vec![0; size];
    let mut distance = vec![-1; size];
    let mut queue = vec![0; rows * columns];
    for row in 1..=rows {
        for column in 1..=columns {
            let cell = row * stride + column;
            heights[cell] = values.next().unwrap() as i32;
            flood[cell] = INF;
        }
    }
    let rabbit_row = values.next().unwrap();
    let rabbit_column = values.next().unwrap();
    let start = rabbit_row * stride + rabbit_column;
    let water_row = values.next().unwrap();
    let water_column = values.next().unwrap();
    let water = water_row * stride + water_column;
    flood[water] = 0;
    queue[0] = water;
    let mut head = 0;
    let mut tail = 1;
    while head < tail {
        let cell = queue[head];
        head += 1;
        for next in [cell - stride, cell - 1, cell + 1, cell + stride] {
            if flood[next] == INF && heights[next] <= heights[cell] {
                flood[next] = flood[cell] + 1;
                queue[tail] = next;
                tail += 1;
            }
        }
    }
    if !can_escape(
        &heights,
        &flood,
        stride,
        start,
        MAX_HEIGHT,
        &mut distance,
        &mut queue,
    ) {
        println!("{}", -1);
        return;
    }
    let mut low = 0;
    let mut high = MAX_HEIGHT;
    while low < high {
        let middle = low + (high - low) / 2;
        if can_escape(
            &heights,
            &flood,
            stride,
            start,
            middle,
            &mut distance,
            &mut queue,
        ) {
            high = middle;
        } else {
            low = middle + 1;
        }
    }
    println!("{}", low);
}

use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

// results of a position for the first player
const UNKNOWN: u8 = 0;
const WIN: u8 = 1;
const LOSE: u8 = 2;
const DRAW: u8 = 3;
const INF: u16 = u16::MAX;
const SIDES: usize = 4;
const CELL: usize = 3;
const MOVES: usize = 10;
const PASS: usize = 4;
const SUICIDE: usize = 9;
const NONE: usize = usize::MAX;
// a rocket state: 0 still loaded, 1 fired out of the maze, w + 2 destroyed wall w
const LOADED: usize = 0;
const FIRED: usize = 1;
const WALL_BASE: usize = 2;
// at most this many places move into a place: a step from each side, with or
// without the chest picked up on the way, and a pass
const MAX_PREDS: usize = 2 * SIDES + 1;
const SAW_WIN: u8 = 1;
const SAW_LOSE: u8 = 2;
const SAW_DRAW: u8 = 4;
const DIRECTION: &[u8] = b"8624"; // north, east, south, west as on a keypad
const WALL_CHAR: &[u8] = b"-|-|";

#[derive(Clone, Copy)]
struct Move {
    inside: bool, // to a place of the same rocket states
    to: usize,
    result: u8,
    dist: u16,
}

const MISSING: Move = Move {
    inside: false,
    to: 0,
    result: UNKNOWN,
    dist: 0,
};

fn win_for(turn: usize) -> u8 {
    if turn == 0 {
        WIN
    } else {
        LOSE
    }
}

fn lose_for(turn: usize) -> u8 {
    WIN + LOSE - win_for(turn)
}

fn saw(r: u8) -> u8 {
    match r {
        WIN => SAW_WIN,
        LOSE => SAW_LOSE,
        DRAW => SAW_DRAW,
        _ => 0,
    }
}

struct Game {
    cells: usize,
    states: usize,
    places: usize,
    side: Vec<[usize; SIDES]>,
    step: Vec<[usize; SIDES]>,
    chest: usize,
    // a place: both cells, who holds the chest (0 nobody, 1 or 2) and whose turn
    cell1: Vec<usize>,
    cell2: Vec<usize>,
    holder: Vec<usize>,
    turn_of: Vec<usize>,
    valid: Vec<usize>,
    result_all: Vec<u8>, // by rocket states and place
    dist_all: Vec<u16>,
}

impl Game {
    fn place_id(&self, c1: usize, c2: usize, h: usize, turn: usize) -> usize {
        ((c1 * self.cells + c2) * CELL + h) * 2 + turn
    }

    fn slot(&self, s1: usize, s2: usize, place: usize) -> usize {
        (s1 * self.states + s2) * self.places + place
    }

    fn wall_stands(w: usize, s1: usize, s2: usize) -> bool {
        w != NONE && s1 != w + WALL_BASE && s2 != w + WALL_BASE
    }

    fn can_pass(&self, from: usize, d: usize, s1: usize, s2: usize) -> bool {
        let to = self.step[from][d];
        to != NONE
            && !Game::wall_stands(self.side[from][d], s1, s2)
            && !Game::wall_stands(self.side[to][(d + 2) % SIDES], s1, s2)
    }

    // the move with a code (M8 M6 M2 M4 M5 S8 S6 S2 S4 S5) from a place
    fn move_from(&self, s1: usize, s2: usize, place: usize, code: usize) -> Move {
        let (turn, h) = (self.turn_of[place], self.holder[place]);
        let (cur, other) = if turn == 1 {
            (self.cell2[place], self.cell1[place])
        } else {
            (self.cell1[place], self.cell2[place])
        };
        let outcome = |result| Move {
            inside: false,
            to: 0,
            result,
            dist: 0,
        };
        if code < PASS {
            let (d, next) = (code, self.step[cur][code]);
            if next == NONE {
                // out of the maze, only with the chest
                return if h == turn + 1 && !Game::wall_stands(self.side[cur][d], s1, s2) {
                    outcome(win_for(turn))
                } else {
                    MISSING
                };
            }
            if next == other || !self.can_pass(cur, d, s1, s2) {
                return MISSING;
            }
            let nh = if h == 0 && next == self.chest {
                turn + 1
            } else {
                h
            };
            let to = if turn == 0 {
                self.place_id(next, self.cell2[place], nh, 1)
            } else {
                self.place_id(self.cell1[place], next, nh, 0)
            };
            return Move {
                inside: true,
                to,
                result: UNKNOWN,
                dist: 0,
            };
        }
        if code == PASS {
            return Move {
                inside: true,
                to: place ^ 1,
                result: UNKNOWN,
                dist: 0,
            };
        }
        if (if turn == 0 { s1 } else { s2 }) != LOADED {
            return MISSING;
        }
        if code == SUICIDE {
            return outcome(lose_for(turn));
        }
        // the flight of the rocket
        let (d, mut pos) = (code - PASS - 1, cur);
        let state = loop {
            if Game::wall_stands(self.side[pos][d], s1, s2) {
                break self.side[pos][d] + WALL_BASE;
            }
            let next = self.step[pos][d];
            if next == NONE {
                break FIRED;
            }
            let back = self.side[next][(d + 2) % SIDES];
            if Game::wall_stands(back, s1, s2) {
                break back + WALL_BASE;
            }
            pos = next;
            if pos == other {
                return outcome(win_for(turn));
            }
        };
        let at = if turn == 0 {
            self.slot(state, s2, place ^ 1)
        } else {
            self.slot(s1, state, place ^ 1)
        };
        Move {
            inside: false,
            to: place ^ 1,
            result: self.result_all[at],
            dist: self.dist_all[at],
        }
    }
}

// buffers of one rocket state, reused
struct Work {
    moves: Vec<Move>,
    move_count: Vec<usize>,
    preds: Vec<usize>,
    pred_count: Vec<usize>,
    res: Vec<u8>,
    seen: Vec<u8>,
    rest: Vec<u32>,
    needed: Vec<u32>,
    got: Vec<u32>,
    most: Vec<u32>,
    dist: Vec<u32>,
    order: Vec<usize>,
}

impl Work {
    fn settle(&mut self, place: usize, turn: usize) {
        if self.res[place] != UNKNOWN {
            return;
        }
        let first = turn == 0;
        let mine = if first { SAW_WIN } else { SAW_LOSE };
        self.res[place] = if self.seen[place] & mine != 0 {
            win_for(turn)
        } else if self.rest[place] == 0 {
            if self.seen[place] & SAW_DRAW != 0 {
                DRAW
            } else {
                lose_for(turn)
            }
        } else {
            return;
        };
        self.order.push(place);
    }
}

fn solve(g: &mut Game, w: &mut Work, s1: usize, s2: usize) {
    for &place in &g.valid {
        w.move_count[place] = 0;
        w.pred_count[place] = 0;
        w.res[place] = UNKNOWN;
        w.seen[place] = 0;
        w.rest[place] = 0;
    }
    for &place in &g.valid {
        for code in 0..MOVES {
            let m = g.move_from(s1, s2, place, code);
            if !m.inside && m.result == UNKNOWN {
                continue;
            }
            w.moves[place * MOVES + w.move_count[place]] = m;
            w.move_count[place] += 1;
            if m.inside {
                w.preds[m.to * MAX_PREDS + w.pred_count[m.to]] = place;
                w.pred_count[m.to] += 1;
                w.rest[place] += 1;
            } else {
                w.seen[place] |= saw(m.result);
            }
        }
    }
    // the result by backward induction: a player wins as soon as one move
    // wins for her, loses when every move loses, and a cycle is a draw
    w.order.clear();
    for &place in &g.valid {
        w.settle(place, g.turn_of[place]);
    }
    let mut head = 0;
    while head < w.order.len() {
        let u = w.order[head];
        head += 1;
        for k in u * MAX_PREDS..u * MAX_PREDS + w.pred_count[u] {
            let p = w.preds[k];
            if w.res[p] == UNKNOWN {
                w.rest[p] -= 1;
                w.seen[p] |= saw(w.res[u]);
                w.settle(p, g.turn_of[p]);
            }
        }
    }
    for &place in &g.valid {
        if w.res[place] == UNKNOWN {
            w.res[place] = DRAW;
        }
        w.dist[place] = INF as u32;
    }
    // the number of turns: the first player takes the fewest, the second the
    // most, among the moves that keep the result
    for kind in [WIN, LOSE] {
        let mut queue = BinaryHeap::new();
        for &place in &g.valid {
            w.needed[place] = 0;
            w.got[place] = 0;
            w.most[place] = 0;
            if w.res[place] != kind {
                continue;
            }
            for k in place * MOVES..place * MOVES + w.move_count[place] {
                let m = w.moves[k];
                if (m.inside && w.res[m.to] == kind) || (!m.inside && m.result == kind) {
                    w.needed[place] += 1;
                    if !m.inside && m.dist < INF {
                        queue.push(Reverse((m.dist as u32 + 1, place)));
                    }
                }
            }
        }
        while let Some(Reverse((d, place))) = queue.pop() {
            let done;
            if g.turn_of[place] == 0 {
                done = d < w.dist[place] && w.dist[place] == INF as u32;
                w.dist[place] = w.dist[place].min(d);
            } else {
                w.got[place] += 1;
                w.most[place] = w.most[place].max(d);
                done = w.got[place] == w.needed[place] && w.most[place] < w.dist[place];
                if done {
                    w.dist[place] = w.most[place];
                }
            }
            if done {
                for k in place * MAX_PREDS..place * MAX_PREDS + w.pred_count[place] {
                    let p = w.preds[k];
                    if w.res[p] == kind {
                        queue.push(Reverse((w.dist[place] + 1, p)));
                    }
                }
            }
        }
    }
    for &place in &g.valid {
        let at = g.slot(s1, s2, place);
        g.result_all[at] = w.res[place];
        g.dist_all[at] = if w.res[place] == DRAW {
            INF
        } else {
            w.dist[place] as u16
        };
    }
}

fn strength(r: u8) -> u8 {
    match r {
        WIN => 2,
        DRAW => 1,
        _ => 0,
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut lines = text.lines();
    let n: usize = lines.next().unwrap().trim().parse().unwrap();
    let cells = n * n;
    let board: Vec<Vec<u8>> = (0..CELL * n)
        .map(|_| {
            let mut row = lines.next().unwrap_or("").as_bytes().to_vec();
            row.resize(CELL * n, b' ');
            row
        })
        .collect();
    let mut side = vec![[NONE; SIDES]; cells];
    let mut step = vec![[NONE; SIDES]; cells];
    let (mut start1, mut start2, mut chest, mut walls) = (0, 0, 0, 0);
    let moves_r: [isize; SIDES] = [-1, 0, 1, 0];
    let moves_c: [isize; SIDES] = [0, 1, 0, -1];
    for r in 0..n {
        for c in 0..n {
            let cell = r * n + c;
            match board[CELL * r + 1][CELL * c + 1] {
                b'1' => start1 = cell,
                b'2' => start2 = cell,
                b'*' => chest = cell,
                _ => {}
            }
            // the side characters of a cell: north, east, south, west
            let at = [
                board[CELL * r][CELL * c + 1],
                board[CELL * r + 1][CELL * c + 2],
                board[CELL * r + 2][CELL * c + 1],
                board[CELL * r + 1][CELL * c],
            ];
            for d in 0..SIDES {
                if at[d] == WALL_CHAR[d] {
                    side[cell][d] = walls;
                    walls += 1;
                }
                let (nr, nc) = (r as isize + moves_r[d], c as isize + moves_c[d]);
                if 0 <= nr && nr < n as isize && 0 <= nc && nc < n as isize {
                    step[cell][d] = nr as usize * n + nc as usize;
                }
            }
        }
    }
    let states = walls + WALL_BASE;
    let places = cells * cells * CELL * 2;
    let mut g = Game {
        cells,
        states,
        places,
        side,
        step,
        chest,
        cell1: vec![0; places],
        cell2: vec![0; places],
        holder: vec![0; places],
        turn_of: vec![0; places],
        valid: Vec::new(),
        result_all: vec![UNKNOWN; states * states * places],
        dist_all: vec![INF; states * states * places],
    };
    for a in 0..cells {
        for b in 0..cells {
            for h in 0..CELL {
                for turn in 0..2 {
                    let place = g.place_id(a, b, h, turn);
                    g.cell1[place] = a;
                    g.cell2[place] = b;
                    g.holder[place] = h;
                    g.turn_of[place] = turn;
                    if a != b {
                        g.valid.push(place);
                    }
                }
            }
        }
    }
    let mut w = Work {
        moves: vec![MISSING; places * MOVES],
        move_count: vec![0; places],
        preds: vec![0; places * MAX_PREDS],
        pred_count: vec![0; places],
        res: vec![UNKNOWN; places],
        seen: vec![0; places],
        rest: vec![0; places],
        needed: vec![0; places],
        got: vec![0; places],
        most: vec![0; places],
        dist: vec![0; places],
        order: Vec::with_capacity(places),
    };
    // a shot only uses a rocket up, so states with fewer rockets come first
    for left in 0..=2 {
        for s1 in 0..states {
            for s2 in 0..states {
                let count = (s1 == LOADED) as usize + (s2 == LOADED) as usize;
                if count == left && !(s1 >= WALL_BASE && s1 == s2) {
                    solve(&mut g, &mut w, s1, s2);
                }
            }
        }
    }
    let place = g.place_id(start1, start2, 0, 0);
    let result = g.result_all[g.slot(LOADED, LOADED, place)];
    if result == DRAW {
        println!("Draw");
        return;
    }
    // the first move: the best result, then the fewest turns, then the order of codes
    let (mut best, mut best_result, mut best_dist) = (NONE, UNKNOWN, INF as u32);
    for code in 0..MOVES {
        let m = g.move_from(LOADED, LOADED, place, code);
        if !m.inside && m.result == UNKNOWN {
            continue;
        }
        // a move leads to a table entry or ends the game at once (distance 0)
        let (mut r, mut later) = (m.result, m.dist);
        if m.inside {
            let at = g.slot(LOADED, LOADED, m.to);
            r = g.result_all[at];
            later = g.dist_all[at];
        }
        let d = if r == DRAW {
            0
        } else if later == INF {
            INF as u32
        } else {
            later as u32 + 1
        };
        if best == NONE
            || strength(r) > strength(best_result)
            || (strength(r) == strength(best_result) && r != DRAW && d < best_dist)
        {
            best = code;
            best_result = r;
            best_dist = d;
        }
    }
    let word = if result == WIN { "Win" } else { "Lose" };
    println!("{} {}", word, g.dist_all[g.slot(LOADED, LOADED, place)]);
    let kind = if best <= PASS { 'M' } else { 'S' };
    let dir = if best == PASS || best == SUICIDE {
        b'5'
    } else {
        DIRECTION[best % (PASS + 1)]
    };
    println!("{}{}", kind, dir as char);
}

use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read, Write};

type Bitboard = u64;

const BOARD_WIDTH: usize = 8;
const CELL_COUNT: usize = 64;
const DIRECTIONS: usize = 4;
const MAX_BOXES: usize = 36;
const MAX_SUBSET: usize = 4;
const MATCHING_SIZE: usize = MAX_BOXES + 1;
const UNREACHABLE: i32 = 1_000_000;
const ESTIMATE_WEIGHT: i32 = 20;
const PLAYER_SHIFT: usize = 56;
const BOX_BITS: Bitboard = (1 << PLAYER_SHIFT) - 1;
const INITIAL_SLOT_BITS: usize = 16;
const INITIAL_SLOTS: usize = 1 << INITIAL_SLOT_BITS;
const HASH_MULTIPLIER: Bitboard = 0x9E37_79B9_7F4A_7C15;
const HASH_SHIFT: usize = 20;
const LETTER_CASE: u8 = b'a' - b'A';
const NO_PARENT: i32 = -1;
const STEP: [i32; DIRECTIONS] = [-(BOARD_WIDTH as i32), BOARD_WIDTH as i32, -1, 1];
const LETTERS: &[u8; DIRECTIONS] = b"udlr";

fn bit(cell: usize) -> Bitboard {
    1 << cell
}

fn lowest(mask: Bitboard) -> usize {
    mask.trailing_zeros() as usize
}

fn contains(mask: Bitboard, cell: i32) -> bool {
    mask.wrapping_shr(cell as u32) & 1 != 0
}

// The walls around the floor keep shifted bits from wrapping onto floor cells.
fn shift(mask: Bitboard, direction: usize) -> Bitboard {
    match direction {
        0 => mask >> BOARD_WIDTH,
        1 => mask << BOARD_WIDTH,
        2 => mask >> 1,
        _ => mask << 1,
    }
}

fn reach(mut seed: Bitboard, free: Bitboard) -> Bitboard {
    loop {
        let grown =
            (seed | seed << BOARD_WIDTH | seed >> BOARD_WIDTH | seed << 1 | seed >> 1) & free;
        if grown == seed {
            return seed;
        }
        seed = grown;
    }
}

struct KeySet {
    slots: Vec<Bitboard>,
    used: usize,
}

impl KeySet {
    fn new() -> Self {
        Self {
            slots: vec![0; INITIAL_SLOTS],
            used: 0,
        }
    }

    fn insert(&mut self, key: Bitboard) -> bool {
        if 2 * (self.used + 1) > self.slots.len() {
            let capacity = self.slots.len() * 2;
            let old = std::mem::replace(&mut self.slots, vec![0; capacity]);
            self.used = 0;
            for old_key in old {
                if old_key != 0 {
                    self.insert(old_key);
                }
            }
        }
        let mask = self.slots.len() - 1;
        let mut index = (key.wrapping_mul(HASH_MULTIPLIER) >> HASH_SHIFT) as usize & mask;
        while self.slots[index] != 0 {
            if self.slots[index] == key {
                return false;
            }
            index = (index + 1) & mask;
        }
        self.slots[index] = key;
        self.used += 1;
        true
    }
}

struct Board {
    floor: Bitboard,
    goals: Bitboard,
    start_boxes: Bitboard,
    start_player: usize,
    live: Bitboard,
    push_distance: [[i32; CELL_COUNT]; MAX_BOXES],
    live_index: [usize; CELL_COUNT],
    binomial: [[usize; MAX_SUBSET + 1]; MAX_BOXES + 1],
    solvable_from: [Vec<Bitboard>; MAX_SUBSET + 1],
    table_boxes: Vec<Bitboard>,
    table_areas: Vec<Bitboard>,
}

impl Board {
    fn read(input: &str) -> Self {
        let mut board = Self {
            floor: 0,
            goals: 0,
            start_boxes: 0,
            start_player: 0,
            live: 0,
            push_distance: [[UNREACHABLE; CELL_COUNT]; MAX_BOXES],
            live_index: [0; CELL_COUNT],
            binomial: [[0; MAX_SUBSET + 1]; MAX_BOXES + 1],
            solvable_from: std::array::from_fn(|_| Vec::new()),
            table_boxes: Vec::new(),
            table_areas: Vec::new(),
        };
        let mut row = 0;
        for line in input.split('\n') {
            let line = line.strip_suffix('\r').unwrap_or(line);
            if line.is_empty() {
                continue;
            }
            for (column, tile) in line.bytes().take(BOARD_WIDTH).enumerate() {
                let cell = row * BOARD_WIDTH + column;
                if tile != b'#' {
                    board.floor |= bit(cell);
                }
                if matches!(tile, b'.' | b'*' | b'+') {
                    board.goals |= bit(cell);
                }
                if matches!(tile, b'$' | b'*') {
                    board.start_boxes |= bit(cell);
                }
                if matches!(tile, b'@' | b'+') {
                    board.start_player = cell;
                }
            }
            row += 1;
        }
        board.floor = reach(bit(board.start_player), board.floor);
        board.goals &= board.floor;
        board.start_boxes &= board.floor;
        board
    }

    // Remove boxes movable along either axis; the remaining boxes are frozen.
    fn frozen_boxes(&self, mut boxes: Bitboard) -> Bitboard {
        loop {
            let empty = self.floor & !boxes;
            let empty_live = empty & self.live;
            let mut movable = 0;
            for direction in 0..DIRECTIONS {
                movable |= boxes & shift(empty, direction) & shift(empty_live, direction ^ 1);
            }
            if movable == 0 {
                return boxes;
            }
            boxes &= !movable;
        }
    }

    // Remove pushable boxes while growing the player's reachable area.
    fn stuck_boxes(&self, mut boxes: Bitboard, mut area: Bitboard) -> Bitboard {
        loop {
            let empty_live = self.floor & !boxes & self.live;
            let mut movable = 0;
            for direction in 0..DIRECTIONS {
                movable |= boxes & shift(area, direction) & shift(empty_live, direction ^ 1);
            }
            if movable == 0 {
                return boxes;
            }
            boxes &= !movable;
            area = reach(area, self.floor & !boxes);
        }
    }

    // Restrict pushes to a corral only when every relaxed push is available
    // now and goes inward, and the corral still needs work.
    fn corral_boxes(&self, boxes: Bitboard, area: Bitboard) -> Bitboard {
        let mut unseen = self.floor & !(boxes | area);
        let fixed = self.frozen_boxes(boxes);
        while unseen != 0 {
            let corral = reach(unseen & unseen.wrapping_neg(), self.floor & !(boxes | area));
            unseen &= !corral;
            let border =
                boxes & (corral << 1 | corral >> 1 | corral << BOARD_WIDTH | corral >> BOARD_WIDTH);
            if (border & !self.goals) | (corral & self.goals) == 0 {
                continue;
            }
            let reduced = border | fixed;
            let relaxed = reach(area, self.floor & !reduced);
            let mut inward = true;
            let mut pushes = 0;
            for direction in 0..DIRECTIONS {
                if !inward {
                    break;
                }
                let possible = border
                    & shift(relaxed, direction)
                    & shift(self.floor & !reduced & self.live, direction ^ 1);
                let actual = border
                    & shift(area, direction)
                    & shift(self.floor & !boxes & self.live, direction ^ 1);
                if possible != actual || shift(possible, direction) & !corral != 0 {
                    inward = false;
                }
                pushes += possible.count_ones();
            }
            if inward && pushes != 0 {
                return border;
            }
        }
        boxes
    }

    // Hungarian matching gives the minimum total push distance to distinct goals.
    fn matching(&self, mut boxes: Bitboard) -> i32 {
        let mut cells = [0; MATCHING_SIZE];
        let mut count = 0;
        while boxes != 0 {
            count += 1;
            cells[count] = lowest(boxes);
            boxes &= boxes - 1;
        }
        let mut box_potential = [0; MATCHING_SIZE];
        let mut goal_potential = [0; MATCHING_SIZE];
        let mut matched = [0; MATCHING_SIZE];
        let mut previous = [0; MATCHING_SIZE];
        for box_index in 1..=count {
            matched[0] = box_index;
            let mut goal = 0;
            let mut slack = [UNREACHABLE; MATCHING_SIZE];
            let mut visited = [false; MATCHING_SIZE];
            loop {
                visited[goal] = true;
                let current = matched[goal];
                let mut delta = UNREACHABLE;
                let mut next = 0;
                for candidate in 1..=count {
                    if !visited[candidate] {
                        let reduced = self.push_distance[candidate - 1][cells[current]]
                            - box_potential[current]
                            - goal_potential[candidate];
                        if reduced < slack[candidate] {
                            slack[candidate] = reduced;
                            previous[candidate] = goal;
                        }
                        if slack[candidate] < delta {
                            delta = slack[candidate];
                            next = candidate;
                        }
                    }
                }
                if delta >= UNREACHABLE / 2 {
                    return -1;
                }
                for candidate in 0..=count {
                    if visited[candidate] {
                        box_potential[matched[candidate]] += delta;
                        goal_potential[candidate] -= delta;
                    } else {
                        slack[candidate] -= delta;
                    }
                }
                goal = next;
                if matched[goal] == 0 {
                    break;
                }
            }
            loop {
                let next = previous[goal];
                matched[goal] = matched[next];
                goal = next;
                if goal == 0 {
                    break;
                }
            }
        }
        let mut total = 0;
        for goal in 1..=count {
            let distance = self.push_distance[goal - 1][cells[matched[goal]]];
            if distance >= UNREACHABLE {
                return -1;
            }
            total += distance;
        }
        total
    }

    fn subset_rank(&self, mut boxes: Bitboard) -> usize {
        let mut rank = 0;
        let mut position = 1;
        while boxes != 0 {
            rank += self.binomial[self.live_index[lowest(boxes)]][position];
            position += 1;
            boxes &= boxes - 1;
        }
        rank
    }

    fn add_to_table(&mut self, size: usize, boxes: Bitboard, seed: Bitboard) {
        let area = reach(seed, self.floor & !boxes);
        let rank = self.subset_rank(boxes);
        let cells = &mut self.solvable_from[size][rank];
        if *cells & area != 0 {
            return;
        }
        *cells |= area;
        self.table_boxes.push(boxes);
        self.table_areas.push(area);
    }

    fn add_goal_subsets(
        &mut self,
        size: usize,
        goal_cells: &[usize],
        from: usize,
        left: usize,
        boxes: Bitboard,
    ) {
        if left == 0 {
            let mut free = self.floor & !boxes;
            while free != 0 {
                let area = reach(free & free.wrapping_neg(), self.floor & !boxes);
                self.add_to_table(size, boxes, area);
                free &= !area;
            }
            return;
        }
        for index in from..goal_cells.len() {
            self.add_goal_subsets(
                size,
                goal_cells,
                index + 1,
                left - 1,
                boxes | bit(goal_cells[index]),
            );
        }
    }

    // Pull from every solved subset, recording all solvable player areas.
    fn build_table(&mut self, size: usize, live_count: usize) {
        self.solvable_from[size] = vec![0; self.binomial[live_count][size]];
        self.table_boxes.clear();
        self.table_areas.clear();
        let mut goal_cells = Vec::new();
        let mut rest = self.goals;
        while rest != 0 {
            goal_cells.push(lowest(rest));
            rest &= rest - 1;
        }
        self.add_goal_subsets(size, &goal_cells, 0, size, 0);
        let mut head = 0;
        while head < self.table_boxes.len() {
            let boxes = self.table_boxes[head];
            let area = self.table_areas[head];
            head += 1;
            let mut rest = boxes;
            while rest != 0 {
                let cell = lowest(rest);
                for step in STEP {
                    let to = cell as i32 - step;
                    let back = to - step;
                    if contains(area, to)
                        && contains(self.floor & !boxes, back)
                        && contains(self.live, to)
                    {
                        self.add_to_table(
                            size,
                            boxes ^ bit(cell) ^ bit(to as usize),
                            bit(back as usize),
                        );
                    }
                }
                rest &= rest - 1;
            }
        }
    }

    fn subsets_solvable(
        &self,
        size: usize,
        cells: &[usize],
        from: usize,
        left: usize,
        subset: Bitboard,
        area: Bitboard,
    ) -> bool {
        if left == 0 {
            return self.solvable_from[size][self.subset_rank(subset)] & area != 0;
        }
        for index in from..cells.len() {
            if !self.subsets_solvable(
                size,
                cells,
                index + 1,
                left - 1,
                subset | bit(cells[index]),
                area,
            ) {
                return false;
            }
        }
        true
    }

    fn prepare(&mut self) {
        let mut rest = self.goals;
        let mut goal = 0;
        while rest != 0 {
            let mut queue = [0; CELL_COUNT];
            let mut head = 0;
            let mut tail = 1;
            let start = lowest(rest);
            self.push_distance[goal][start] = 0;
            queue[0] = start;
            while head < tail {
                let cell = queue[head];
                head += 1;
                for step in STEP {
                    let from = cell as i32 - step;
                    let player = from - step;
                    if contains(self.floor, from)
                        && contains(self.floor, player)
                        && self.push_distance[goal][from as usize] == UNREACHABLE
                    {
                        self.push_distance[goal][from as usize] =
                            self.push_distance[goal][cell] + 1;
                        queue[tail] = from as usize;
                        tail += 1;
                    }
                }
            }
            for cell in 0..CELL_COUNT {
                if self.push_distance[goal][cell] < UNREACHABLE {
                    self.live |= bit(cell);
                }
            }
            goal += 1;
            rest &= rest - 1;
        }
        let mut live_count = 0;
        for cell in 0..CELL_COUNT {
            if self.live >> cell & 1 != 0 {
                self.live_index[cell] = live_count;
                live_count += 1;
            }
        }
        for count in 0..=MAX_BOXES {
            for size in 0..=MAX_SUBSET {
                self.binomial[count][size] = if size == 0 {
                    1
                } else if count == 0 {
                    0
                } else {
                    self.binomial[count - 1][size - 1] + self.binomial[count - 1][size]
                };
            }
        }
        for size in 2..=MAX_SUBSET {
            self.build_table(size, live_count);
        }
    }

    fn walk(&self, boxes: Bitboard, from: usize, to: usize) -> Vec<u8> {
        let mut previous = [NO_PARENT; CELL_COUNT];
        let mut direction = [0; CELL_COUNT];
        let mut queue = [0; CELL_COUNT];
        let mut head = 0;
        let mut tail = 1;
        previous[from] = from as i32;
        queue[0] = from;
        while head < tail && previous[to] < 0 {
            let cell = queue[head];
            head += 1;
            for next_direction in 0..DIRECTIONS {
                let next = cell as i32 + STEP[next_direction];
                if contains(self.floor & !boxes, next) && previous[next as usize] < 0 {
                    previous[next as usize] = cell as i32;
                    direction[next as usize] = next_direction;
                    queue[tail] = next as usize;
                    tail += 1;
                }
            }
        }
        let mut steps = Vec::new();
        let mut cell = to;
        while cell != from {
            steps.push(LETTERS[direction[cell]]);
            cell = previous[cell] as usize;
        }
        steps.reverse();
        steps
    }
}

// Separate primitive arrays avoid per-node padding and pointer-sized indexes.
struct Search {
    keys: Vec<Bitboard>,
    parents: Vec<i32>,
    moves: Vec<u8>,
    pushes: Vec<i32>,
    seen: KeySet,
    open: BinaryHeap<Reverse<(i32, u32)>>,
}

impl Search {
    fn new() -> Self {
        Self {
            keys: Vec::new(),
            parents: Vec::new(),
            moves: Vec::new(),
            pushes: Vec::new(),
            seen: KeySet::new(),
            open: BinaryHeap::new(),
        }
    }

    fn add(
        &mut self,
        board: &Board,
        boxes: Bitboard,
        player: usize,
        parent: i32,
        movement: usize,
        pushes: i32,
    ) {
        let area = reach(bit(player), board.floor & !boxes);
        let key = boxes | (lowest(area) as Bitboard) << PLAYER_SHIFT;
        if !self.seen.insert(key) {
            return;
        }
        let mut alive = board.frozen_boxes(boxes) & !board.goals == 0
            && board.stuck_boxes(boxes, area) & !board.goals == 0;
        if parent >= 0 {
            let moved = (movement / DIRECTIONS) as i32 + STEP[movement % DIRECTIONS];
            let mut cells = [0; MAX_BOXES];
            let mut count = 0;
            let mut rest = boxes & !bit(moved as usize);
            while rest != 0 {
                cells[count] = lowest(rest);
                count += 1;
                rest &= rest - 1;
            }
            for size in 2..=MAX_SUBSET {
                if !alive {
                    break;
                }
                if count + 1 >= size {
                    alive = board.subsets_solvable(
                        size,
                        &cells[..count],
                        0,
                        size - 1,
                        bit(moved as usize),
                        area,
                    );
                }
            }
        }
        let estimate = if alive { board.matching(boxes) } else { -1 };
        if estimate < 0 {
            return;
        }
        let id = self.keys.len() as u32;
        self.keys.push(key);
        self.parents.push(parent);
        self.moves.push(movement as u8);
        self.pushes.push(pushes);
        self.open
            .push(Reverse((pushes + ESTIMATE_WEIGHT * estimate, id)));
    }

    fn solve(&mut self, board: &Board) -> Vec<u8> {
        self.add(
            board,
            board.start_boxes,
            board.start_player,
            NO_PARENT,
            0,
            0,
        );
        let mut solved = NO_PARENT;
        while let Some(Reverse((_, id))) = self.open.pop() {
            let index = id as usize;
            let boxes = self.keys[index] & BOX_BITS;
            if boxes == board.goals {
                solved = id as i32;
                break;
            }
            let area = reach(
                bit((self.keys[index] >> PLAYER_SHIFT) as usize),
                board.floor & !boxes,
            );
            let empty_live = board.floor & !boxes & board.live;
            let allowed = board.corral_boxes(boxes, area);
            for direction in 0..DIRECTIONS {
                let mut possible =
                    allowed & shift(area, direction) & shift(empty_live, direction ^ 1);
                while possible != 0 {
                    let cell = lowest(possible);
                    self.add(
                        board,
                        boxes ^ bit(cell) ^ bit((cell as i32 + STEP[direction]) as usize),
                        cell,
                        id as i32,
                        cell * DIRECTIONS + direction,
                        self.pushes[index] + 1,
                    );
                    possible &= possible - 1;
                }
            }
        }
        let mut moves = Vec::new();
        while solved > 0 {
            moves.push(self.moves[solved as usize]);
            solved = self.parents[solved as usize];
        }
        moves.reverse();
        let mut plan = Vec::new();
        let mut boxes = board.start_boxes;
        let mut player = board.start_player;
        for movement in moves {
            let cell = movement as usize / DIRECTIONS;
            let direction = movement as usize % DIRECTIONS;
            plan.extend(board.walk(boxes, player, (cell as i32 - STEP[direction]) as usize));
            plan.push(LETTERS[direction] - LETTER_CASE);
            boxes ^= bit(cell) ^ bit((cell as i32 + STEP[direction]) as usize);
            player = cell;
        }
        plan
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut board = Board::read(&input);
    let mut plan = if board.start_boxes == board.goals {
        Vec::new()
    } else {
        board.prepare();
        Search::new().solve(&board)
    };
    plan.push(b'\n');
    io::stdout().lock().write_all(&plan).unwrap();
}

package main

import (
	"bufio"
	"math/bits"
	"os"
	"runtime/debug"
)

const (
	boardWidth     = 8
	cellCount      = 64
	directions     = 4
	maxBoxes       = 36
	maxSubset      = 4
	tripleSize     = 3
	unreachable    = 1000000
	estimateWeight = 20
	playerShift    = 56
	boxBits        = uint64(1)<<playerShift - 1
	initialBits    = 16
	initialSlots   = 1 << initialBits
	hashMultiplier = uint64(0x9E3779B97F4A7C15)
	hashShift      = 20
	reclaimBits    = 20
	reclaimSlots   = 1 << reclaimBits
	priorityShift  = 32
	letterCase     = 'a' - 'A'
	letters        = "udlr"
)

var (
	step                                     = [directions]int{-boardWidth, boardWidth, -1, 1}
	floorCells, goals, startBoxes, liveCells uint64
	startPlayer, goalCount                   int
	pushDistance                             [maxBoxes][cellCount]int
	liveIndex                                [cellCount]int
	liveCount                                int
	binomial                                 [maxBoxes + 1][maxSubset + 1]int
	solvableFrom                             [maxSubset + 1][]uint64
	tableQueue                               []uint64
	slots                                    = []*[initialSlots]uint64{new([initialSlots]uint64)}
	usedSlots                                int
	nodeKeys                                 []uint64
	nodeParents                              []int32
	nodeMoves                                []uint8
	nodePushes                               []int32
	open                                     []uint64
)

func bit(cell int) uint64    { return uint64(1) << uint(cell) }
func lowest(mask uint64) int { return bits.TrailingZeros64(mask) }

// The walls keep shifted bits from wrapping onto floor cells.
func shift(mask uint64, direction int) uint64 {
	switch direction {
	case 0:
		return mask >> boardWidth
	case 1:
		return mask << boardWidth
	case 2:
		return mask >> 1
	default:
		return mask << 1
	}
}

func reach(seed, free uint64) uint64 {
	for {
		grown := (seed | seed<<boardWidth | seed>>boardWidth | seed<<1 | seed>>1) & free
		if grown == seed {
			return seed
		}
		seed = grown
	}
}

// Remove boxes movable along either axis; what remains is frozen.
func frozenBoxes(boxes uint64) uint64 {
	for {
		empty := floorCells &^ boxes
		emptyLive := empty & liveCells
		var movable uint64
		for direction := 0; direction < directions; direction++ {
			movable |= boxes & shift(empty, direction) & shift(emptyLive, direction^1)
		}
		if movable == 0 {
			return boxes
		}
		boxes &^= movable
	}
}

// Removing pushable boxes lets the player's area grow after each round.
func stuckBoxes(boxes, area uint64) uint64 {
	for {
		emptyLive := floorCells &^ boxes & liveCells
		var movable uint64
		for direction := 0; direction < directions; direction++ {
			movable |= boxes & shift(area, direction) & shift(emptyLive, direction^1)
		}
		if movable == 0 {
			return boxes
		}
		boxes &^= movable
		area = reach(area, floorCells&^boxes)
	}
}

// Restrict pushes to a corral when all its possible border pushes go inward
// and are already available to the player.
func corralBoxes(boxes, area uint64) uint64 {
	unseen := floorCells &^ (boxes | area)
	fixed := frozenBoxes(boxes)
	for unseen != 0 {
		corral := reach(unseen&-unseen, floorCells&^(boxes|area))
		unseen &^= corral
		border := boxes & (corral<<1 | corral>>1 | corral<<boardWidth | corral>>boardWidth)
		if (border&^goals)|(corral&goals) == 0 {
			continue
		}
		reduced := border | fixed
		relaxed := reach(area, floorCells&^reduced)
		inward, pushes := true, 0
		for direction := 0; direction < directions && inward; direction++ {
			possible := border & shift(relaxed, direction) &
				shift(floorCells&^reduced&liveCells, direction^1)
			actual := border & shift(area, direction) &
				shift(floorCells&^boxes&liveCells, direction^1)
			if possible != actual || shift(possible, direction)&^corral != 0 {
				inward = false
			}
			pushes += bits.OnesCount64(possible)
		}
		if inward && pushes != 0 {
			return border
		}
	}
	return boxes
}

// Hungarian matching gives the minimum total distance to distinct goals.
func matching(boxes uint64) int {
	var cells, boxPotential, goalPotential, matched, previous [maxBoxes + 1]int
	count := 0
	for ; boxes != 0; boxes &= boxes - 1 {
		count++
		cells[count] = lowest(boxes)
	}
	for box := 1; box <= count; box++ {
		matched[0] = box
		goal := 0
		var slack [maxBoxes + 1]int
		var visited [maxBoxes + 1]bool
		for index := 0; index <= count; index++ {
			slack[index] = unreachable
		}
		for {
			visited[goal] = true
			current, delta, next := matched[goal], unreachable, 0
			for candidate := 1; candidate <= count; candidate++ {
				if !visited[candidate] {
					reduced := pushDistance[candidate-1][cells[current]] -
						boxPotential[current] - goalPotential[candidate]
					if reduced < slack[candidate] {
						slack[candidate], previous[candidate] = reduced, goal
					}
					if slack[candidate] < delta {
						delta, next = slack[candidate], candidate
					}
				}
			}
			if delta >= unreachable/2 {
				return -1
			}
			for candidate := 0; candidate <= count; candidate++ {
				if visited[candidate] {
					boxPotential[matched[candidate]] += delta
					goalPotential[candidate] -= delta
				} else {
					slack[candidate] -= delta
				}
			}
			goal = next
			if matched[goal] == 0 {
				break
			}
		}
		for {
			next := previous[goal]
			matched[goal] = matched[next]
			goal = next
			if goal == 0 {
				break
			}
		}
	}
	total := 0
	for goal := 1; goal <= count; goal++ {
		distance := pushDistance[goal-1][cells[matched[goal]]]
		if distance >= unreachable {
			return -1
		}
		total += distance
	}
	return total
}

func subsetRank(boxes uint64) int {
	rank, position := 0, 1
	for ; boxes != 0; boxes &= boxes - 1 {
		rank += binomial[liveIndex[lowest(boxes)]][position]
		position++
	}
	return rank
}

func addToTable(size int, boxes, seed uint64) {
	area := reach(seed, floorCells&^boxes)
	cells := &solvableFrom[size][subsetRank(boxes)]
	if *cells&area != 0 {
		return
	}
	*cells |= area
	tableQueue = append(tableQueue, boxes, area)
}

func addGoalSubsets(size int, goalCells []int, from, left int, boxes uint64) {
	if left == 0 {
		for free := floorCells &^ boxes; free != 0; {
			area := reach(free&-free, floorCells&^boxes)
			addToTable(size, boxes, area)
			free &^= area
		}
		return
	}
	for index := from; index < len(goalCells); index++ {
		addGoalSubsets(size, goalCells, index+1, left-1, boxes|bit(goalCells[index]))
	}
}

// Pull each goal subset backwards, recording every solvable player area.
func buildTable(size int) {
	solvableFrom[size] = make([]uint64, binomial[liveCount][size])
	tableQueue = tableQueue[:0]
	var goalCells [maxBoxes]int
	count := 0
	for rest := goals; rest != 0; rest &= rest - 1 {
		goalCells[count] = lowest(rest)
		count++
	}
	addGoalSubsets(size, goalCells[:count], 0, size, 0)
	for head := 0; head < len(tableQueue); head += 2 {
		boxes, area := tableQueue[head], tableQueue[head+1]
		for rest := boxes; rest != 0; rest &= rest - 1 {
			box := lowest(rest)
			for direction := 0; direction < directions; direction++ {
				to := box - step[direction]
				back := to - step[direction]
				if area>>uint(to)&1 != 0 && (floorCells&^boxes)>>uint(back)&1 != 0 &&
					liveCells>>uint(to)&1 != 0 {
					addToTable(size, boxes^bit(box)^bit(to), bit(back))
				}
			}
		}
	}
}

// Enumerate the same ordered combinations, inserting the moved box in each
// combinatorial rank without rebuilding and scanning its bit mask.
func subsetsSolvable(size int, cells []int, moved int, area uint64) bool {
	movedIndex := liveIndex[moved]
	var contributions [maxSubset][maxBoxes]int
	var before [maxBoxes]int
	for index, cell := range cells {
		live := liveIndex[cell]
		offset := 1
		if live < movedIndex {
			before[index] = 1
			offset = 0
		}
		for position := 1; position < size; position++ {
			contributions[position][index] = binomial[live][position+offset]
		}
	}
	table := solvableFrom[size]
	for first := 0; first < len(cells); first++ {
		firstRank := contributions[1][first]
		firstPosition := 1 + before[first]
		if size == 2 {
			if table[firstRank+binomial[movedIndex][firstPosition]]&area == 0 {
				return false
			}
			continue
		}
		for second := first + 1; second < len(cells); second++ {
			secondRank := firstRank + contributions[2][second]
			secondPosition := firstPosition + before[second]
			if size == tripleSize {
				if table[secondRank+binomial[movedIndex][secondPosition]]&area == 0 {
					return false
				}
				continue
			}
			for third := second + 1; third < len(cells); third++ {
				rank := secondRank + contributions[tripleSize][third]
				position := secondPosition + before[third]
				if table[rank+binomial[movedIndex][position]]&area == 0 {
					return false
				}
			}
		}
	}
	return true
}

func growSlots() {
	old := slots
	slots = make([]*[initialSlots]uint64, 2*len(old))
	for index := range slots {
		slots[index] = new([initialSlots]uint64)
	}
	usedSlots = 0
	for _, block := range old {
		for _, oldKey := range block {
			if oldKey != 0 {
				insertKey(oldKey)
			}
		}
	}
}

// Fixed-size blocks let the allocator reuse retired tables after growth.
// Probing still uses one power-of-two address space with zero as the empty key.
func insertKey(key uint64) bool {
	if 2*(usedSlots+1) > len(slots)*initialSlots {
		if 2*len(slots)*initialSlots >= reclaimSlots {
			debug.FreeOSMemory()
		}
		growSlots()
		// Reclaim obsolete table blocks before further search allocations.
		if len(slots)*initialSlots >= reclaimSlots {
			debug.FreeOSMemory()
		}
	}
	mask := uint64(len(slots)*initialSlots - 1)
	index := key * hashMultiplier >> hashShift & mask
	for {
		cell := &slots[index>>initialBits][index&(initialSlots-1)]
		if *cell == 0 {
			*cell = key
			usedSlots++
			return true
		}
		if *cell == key {
			return false
		}
		index = (index + 1) & mask
	}
}

// Packed priorities compare score first, then insertion ID.
func pushOpen(priority uint64) {
	index := len(open)
	open = append(open, priority)
	for index > 0 {
		parent := (index - 1) / 2
		if open[parent] <= priority {
			break
		}
		open[index] = open[parent]
		index = parent
	}
	open[index] = priority
}

func popOpen() int {
	id := int(uint32(open[0]))
	last := open[len(open)-1]
	open = open[:len(open)-1]
	if len(open) == 0 {
		return id
	}
	index := 0
	for child := 1; child < len(open); child = 2*index + 1 {
		if child+1 < len(open) && open[child+1] < open[child] {
			child++
		}
		if last <= open[child] {
			break
		}
		open[index] = open[child]
		index = child
	}
	open[index] = last
	return id
}

func addNode(boxes uint64, player, parent, move, pushes int) {
	area := reach(bit(player), floorCells&^boxes)
	key := boxes | uint64(lowest(area))<<playerShift
	if !insertKey(key) {
		return
	}
	alive := frozenBoxes(boxes)&^goals == 0 && stuckBoxes(boxes, area)&^goals == 0
	if parent >= 0 {
		moved := move/directions + step[move%directions]
		var cells [maxBoxes]int
		count := 0
		for rest := boxes &^ bit(moved); rest != 0; rest &= rest - 1 {
			cells[count] = lowest(rest)
			count++
		}
		for size := 2; size <= maxSubset && alive; size++ {
			if count+1 >= size {
				alive = subsetsSolvable(size, cells[:count], moved, area)
			}
		}
	}
	estimate := -1
	if alive {
		estimate = matching(boxes)
	}
	if estimate < 0 {
		return
	}
	id := len(nodeKeys)
	nodeKeys = append(nodeKeys, key)
	nodeParents = append(nodeParents, int32(parent))
	nodeMoves = append(nodeMoves, uint8(move))
	nodePushes = append(nodePushes, int32(pushes))
	pushOpen(uint64(pushes+estimateWeight*estimate)<<priorityShift | uint64(id))
}

func walk(plan []byte, boxes uint64, from, to int) []byte {
	var previous, direction, queue [cellCount]int
	for cell := range previous {
		previous[cell] = -1
	}
	previous[from] = from
	queue[0] = from
	head, tail := 0, 1
	for head < tail && previous[to] < 0 {
		cell := queue[head]
		head++
		for candidate := 0; candidate < directions; candidate++ {
			next := cell + step[candidate]
			if (floorCells&^boxes)>>uint(next)&1 != 0 && previous[next] < 0 {
				previous[next], direction[next], queue[tail] = cell, candidate, next
				tail++
			}
		}
	}
	begin := len(plan)
	for cell := to; cell != from; cell = previous[cell] {
		plan = append(plan, letters[direction[cell]])
	}
	for left, right := begin, len(plan)-1; left < right; left, right = left+1, right-1 {
		plan[left], plan[right] = plan[right], plan[left]
	}
	return plan
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	row := 0
	for scanner.Scan() {
		line := scanner.Bytes()
		if len(line) == 0 {
			continue
		}
		for column := 0; column < len(line) && column < boardWidth; column++ {
			tile, cell := line[column], row*boardWidth+column
			if tile != '#' {
				floorCells |= bit(cell)
			}
			if tile == '.' || tile == '*' || tile == '+' {
				goals |= bit(cell)
			}
			if tile == '$' || tile == '*' {
				startBoxes |= bit(cell)
			}
			if tile == '@' || tile == '+' {
				startPlayer = cell
			}
		}
		row++
	}
	floorCells = reach(bit(startPlayer), floorCells)
	goals &= floorCells
	startBoxes &= floorCells
	if startBoxes == goals {
		os.Stdout.Write([]byte{'\n'})
		return
	}
	// Pull from each goal to find lone-box distances and live cells.
	for rest := goals; rest != 0; rest &= rest - 1 {
		goal := goalCount
		goalCount++
		var queue [cellCount]int
		head, tail := 0, 1
		for cell := range pushDistance[goal] {
			pushDistance[goal][cell] = unreachable
		}
		pushDistance[goal][lowest(rest)] = 0
		queue[0] = lowest(rest)
		for head < tail {
			cell := queue[head]
			head++
			for direction := 0; direction < directions; direction++ {
				from := cell - step[direction]
				player := from - step[direction]
				if floorCells>>uint(from)&1 != 0 && floorCells>>uint(player)&1 != 0 &&
					pushDistance[goal][from] == unreachable {
					pushDistance[goal][from] = pushDistance[goal][cell] + 1
					queue[tail] = from
					tail++
				}
			}
		}
		for cell := 0; cell < cellCount; cell++ {
			if pushDistance[goal][cell] < unreachable {
				liveCells |= bit(cell)
			}
		}
	}
	for cell := 0; cell < cellCount; cell++ {
		if liveCells>>uint(cell)&1 != 0 {
			liveIndex[cell] = liveCount
			liveCount++
		}
	}
	for count := 0; count <= maxBoxes; count++ {
		for size := 0; size <= maxSubset; size++ {
			if size == 0 {
				binomial[count][size] = 1
			} else if count != 0 {
				binomial[count][size] = binomial[count-1][size-1] + binomial[count-1][size]
			}
		}
	}
	for size := 2; size <= maxSubset; size++ {
		buildTable(size)
	}
	tableQueue = nil
	addNode(startBoxes, startPlayer, -1, 0, 0)
	solved := -1
	for len(open) != 0 {
		id := popOpen()
		boxes := nodeKeys[id] & boxBits
		if boxes == goals {
			solved = id
			break
		}
		area := reach(bit(int(nodeKeys[id]>>playerShift)), floorCells&^boxes)
		emptyLive := floorCells &^ boxes & liveCells
		allowed := corralBoxes(boxes, area)
		for direction := 0; direction < directions; direction++ {
			can := allowed & shift(area, direction) & shift(emptyLive, direction^1)
			for ; can != 0; can &= can - 1 {
				box := lowest(can)
				addNode(boxes^bit(box)^bit(box+step[direction]), box, id,
					box*directions+direction, int(nodePushes[id])+1)
			}
		}
	}
	var moves []uint8
	for id := solved; id > 0; id = int(nodeParents[id]) {
		moves = append(moves, nodeMoves[id])
	}
	var plan []byte
	boxes, player := startBoxes, startPlayer
	for index := len(moves) - 1; index >= 0; index-- {
		move := int(moves[index])
		box, direction := move/directions, move%directions
		plan = walk(plan, boxes, player, box-step[direction])
		plan = append(plan, letters[direction]-letterCase)
		boxes ^= bit(box) ^ bit(box+step[direction])
		player = box
	}
	os.Stdout.Write(append(plan, '\n'))
}

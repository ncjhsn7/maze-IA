const NxN = 6;
let NFOODS = NxN / 2;
let grid = new Array(NxN);

function Spot(x, y) {
    this.x = x;
    this.y = y;
    this.f = 0;
    this.g = 0;
    this.h = 0;
    this.neighbors = [];
    this.previous = null;
    this.wall = false;

    if (Math.random(1) < 0.3) {
        this.wall = true;
    }

    this.addNeighbors = (grid) => {
        if (this.x < NxN - 1) {
            this.neighbors.push(grid[this.x + 1][this.y]);
        }

        if (this.x > 0) {
            this.neighbors.push(grid[this.x - 1][this.y]);
        }

        if (this.y < NxN - 1) {
            this.neighbors.push(grid[this.x][this.y + 1]);
        }

        if (this.y > 0) {
            this.neighbors.push(grid[this.x][this.y - 1]);
        }

        if (this.x > 0 && this.y > 0) {
            this.neighbors.push(grid[this.x - 1][this.y - 1]);
        }

        if (this.x < NxN - 1 && this.y > 0) {
            this.neighbors.push(grid[this.x + 1][this.y - 1]);
        }

        if (this.x > 0 && this.y < NxN - 1) {
            this.neighbors.push(grid[this.x - 1][this.y + 1]);
        }

        if (this.x < NxN - 1 && this.y < NxN - 1) {
            this.neighbors.push(grid[this.x + 1][this.y + 1]);
        }
    }
}

function remove(arr, element) {
    for (let i = arr.length - 1; i >= 0; i--) {
        if (arr[i] == element) {
            arr.splice(i, 1);
        }
    }
}

function heuristic(a, b) {
    //return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    return Math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2);
}

function printGrid(grid, current, foods) {
    for (let i = 0; i < NxN; i++) {
        for (let j = 0; j < NxN; j++) {
            let cell = !grid[i][j].wall ? ' . ' : ' x ';

            if (foods.includes(grid[i][j])) {
                cell = ' C ';
            }

            if (grid[i][j] == current) {
                cell = ' L ';
            }

            process.stdout.write(cell);
        }
        console.log();
    }
    console.log();
}

function getCloserDot(current, foods) {
    if (foods.length == 0) {
        return current;
    }

    let near = foods[0];
    foods.forEach(food => {
        if (heuristic(current, food) < heuristic(current, near)) {
            near = food;
        }
    });
    return near;
}

function getPath(current) {
    path = [];
    let temp = current;
    path.push(temp);

    while (temp.previous) {
        path.push(temp.previous);
        temp = temp.previous;
    }

    for (let i = 0; i < NxN; i++) {
        for (let j = 0; j < NxN; j++) {
            let cell = !grid[i][j].wall ? ' . ' : ' x ';

            if (grid[i][j] == current) {
                cell = ' L ';
            }

            if (path.includes(grid[i][j])) {
                cell = ' o ';
            }
            process.stdout.write(cell);
        }
        console.log();
    }

    return path;
}

function generateGrid() {
    let grid = [];
    for (let i = 0; i < NxN; i++) {
        grid[i] = new Array(NxN);
    }

    for (let i = 0; i < NxN; i++) {
        for (let j = 0; j < NxN; j++) {
            grid[i][j] = new Spot(i, j);
        }
    }


    for (let i = 0; i < NxN; i++) {
        for (let j = 0; j < NxN; j++) {
            grid[i][j].addNeighbors(grid);
        }
    }

    return grid;
}

function generateFoods(grid, nFoods) {
    let foods = [];
    while (foods.length < nFoods) {
        for (let i = 0; i < grid.length; i++) {
            for (let j = 0; j < grid.length; j++) {
                if (Math.random(1) < 0.2 && grid[i][j].x > 0 && grid[i][j].y > 0 && foods.length < nFoods) {
                    foods.push(grid[i][j]);
                }
            }
        }
    }

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid.length; j++) {
            if (foods.includes(grid[i][j])) {
                grid[i][j].wall = false;
            }
        }
    }
    return foods;
}

grid = generateGrid();
let foods = generateFoods(grid, NxN / 2);

for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid.length; j++) {
        if (foods.includes(grid[i][j])) {
            grid[i][j].wall = false;
        }
    }
}

let start = grid[0][0];
let end = getCloserDot(start, foods);
start.wall = false;

let openSet = [];
let closedSet = [];
let path = [];
openSet.push(start);

printGrid(grid, start, foods);

while (openSet.length > 0) {
    let best = 0;

    for (let i = 0; i < openSet.length; i++) {
        if (openSet[i].f < openSet[best].f) {
            best = i;
        }
    }

    let current = openSet[best];

    if (current == end) {
        remove(foods, current);
        end = getCloserDot(current, foods);
        path = getPath(current, grid);
        openSet = [];
        console.log();
    }

    remove(openSet, current);
    closedSet.push(current);

    var neighbors = current.neighbors;

    for (let i = 0; i < neighbors.length; i++) {
        let neighbor = neighbors[i];

        if (!closedSet.includes(neighbor) && !neighbor.wall) {
            let tryG = current.g + 1;
            let newPath = false;

            if (!openSet.includes(neighbor) && tryG > neighbor.g) {
                neighbor.g = tryG;
                openSet.push(neighbor);
                newPath = true;
            }

            if (newPath) {
                neighbor.h = heuristic(neighbor, end);
                neighbor.f = neighbor.g + neighbor.h;
                neighbor.previous = current;
            }
        }

    }
}
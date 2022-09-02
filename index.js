const NxN = 10;
let grid = new Array(NxN);

function Spot(x,y){
    this.x = x;
    this.y = y;
    this.f = 0;
    this.g = 0;
    this.h = 0;
    this.neighbors = [];
    this.previous = null;
    this.wall = false;

    if(Math.random(1) < 0.2){
        this.wall = true;
    }

    this.addNeighbors = (grid) => {
        if(this.x < NxN - 1){
            this.neighbors.push(grid[this.x + 1][this.y]);
        }

        if(this.x > 0){
            this.neighbors.push(grid[this.x - 1][this.y]);
        }

        if(this.y < NxN - 1){
            this.neighbors.push(grid[this.x][this.y + 1]);
        }

        if(this.y > 0){
            this.neighbors.push(grid[this.x][this.y - 1]);
        }

        if(this.x > 0 && this.y > 0){
            this.neighbors.push(grid[this.x - 1][this.y - 1]);
        }

        if(this.x < NxN - 1 && this.y > 0){
            this.neighbors.push(grid[this.x + 1][this.y - 1]);
        }

        if(this.x > 0 && this.y < NxN - 1){
            this.neighbors.push(grid[this.x - 1][this.y + 1]);
        }

        if(this.x < NxN - 1 && this.y < NxN - 1){
            this.neighbors.push(grid[this.x + 1][this.y + 1]);
        }
    }
}

function remove(arr, element){
    for (let i = arr.length-1; i >= 0; i--) {
        if(arr[i] == element){
            arr.splice(i,1);
        }        
    }
}

function heuristic(a,b){
    //return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
    return Math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
}

function printGrid(grid, end){
    for(let i = 0; i < NxN; i++){
        for(let j = 0; j < NxN; j++){
            let cell = !grid[i][j].wall ? ' - ' : ' x ';
            if(grid[i][j] == end){
                cell = ' !';
            }
            process.stdout.write(cell);
        }
        console.log();
    }
}

for(let i = 0; i < NxN; i++){
    grid[i] = new Array(NxN);
}

for(let i = 0; i < NxN; i++){
    for(let j = 0; j < NxN; j++){
        grid[i][j] = new Spot(i,j);
    }
}

for(let i = 0; i < NxN; i++){
    for(let j = 0; j < NxN; j++){
        grid[i][j].addNeighbors(grid);
    }
}

let start = grid[0][0];
let end = grid[NxN - 1][NxN - 1]; //verificar se existe comida e recalcular 'end'
start.wall = false;
end.wall = false;
let openSet = [];
let closedSet = [];
let path = [];

openSet.push(start);
printGrid(grid,end, start);

while(openSet.length > 0){
    let best = 0;
    for (let i = 0; i < openSet.length; i++) {
        if(openSet[i].f < openSet[best].f){
            best = i;
        }
    }
    let current = openSet[best];
    
    if(current == end){
        path = [];
        let temp = current;
        path.push(temp);
        while(temp.previous){
            path.push(temp.previous);
            temp = temp.previous;
        }
        path.reverse().forEach(element =>{
            let x = String(element.x);
            let y = String(element.y);
            process.stdout.write(`${x}${y} `);
        })
    }
    
    remove(openSet, current);    
    closedSet.push(current);

    var neighbors = current.neighbors;

    for (let i = 0; i < neighbors.length; i++) {
        let neighbor = neighbors[i];

        if(!closedSet.includes(neighbor) && !neighbor.wall){
            let tempG = current.g + 1;
            let newPath = false;
            if(!openSet.includes(neighbor) && tempG > neighbor.g){
                neighbor.g = tempG;
                openSet.push(neighbor);
                newPath = true;
            }

            if(newPath){
                neighbor.h = heuristic(neighbor, end);    
                neighbor.f = neighbor.g + neighbor.h;
                neighbor.previous = current;
            }
        }

    }
}
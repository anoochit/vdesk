import layoutData from '../assets/default-layout-1.json';

const { cols, rows, tiles, furniture } = layoutData;
export const TILE_SIZE = 32;

// Build collision grid
const grid: boolean[][] = [];
for (let y = 0; y < rows; y++) {
  const row: boolean[] = [];
  for (let x = 0; x < cols; x++) {
    // 255 is a wall
    const isWall = tiles[y * cols + x] === 255;
    row.push(isWall);
  }
  grid.push(row);
}

// Mark furniture as blocked
// More accurate sizes for furniture (width, height in tiles)
furniture.forEach((f) => {
  const c = Math.floor(f.col);
  const r = Math.floor(f.row);
  
  if (f.type.includes('CHAIR') || f.type.includes('SOFA') || f.type.includes('BENCH')) {
    return; // Don't block seating completely so agents can sit
  }

  let width = 1;
  let height = 1;

  if (f.type.includes('DESK')) {
    width = 3;
    height = 2;
  } else if (f.type.includes('PC')) {
    width = 1;
    height = 2;
  } else if (f.type.includes('DOUBLE_BOOKSHELF')) {
    width = 2;
    height = 2;
  } else if (f.type.includes('PAINTING') || f.type.includes('WHITEBOARD') || f.type.includes('CLOCK')) {
    // Wall items, don't block the floor
    return;
  } else if (f.type.includes('COFFEE_TABLE')) {
    width = 2;
    height = 1;
  }

  for (let dy = 0; dy < height; dy++) {
    for (let dx = 0; dx < width; dx++) {
      const blockR = r + dy;
      const blockC = c + dx;
      if (blockR >= 0 && blockR < rows && blockC >= 0 && blockC < cols) {
        grid[blockR][blockC] = true;
      }
    }
  }
});

interface Node {
  x: number;
  y: number;
  g: number;
  h: number;
  f: number;
  parent: Node | null;
}

export function findPath(startX: number, startY: number, targetX: number, targetY: number): {x: number, y: number}[] {
  const startCol = Math.floor(startX / TILE_SIZE);
  const startRow = Math.floor(startY / TILE_SIZE);
  const targetCol = Math.floor(targetX / TILE_SIZE);
  const targetRow = Math.floor(targetY / TILE_SIZE);

  if (targetRow < 0 || targetRow >= rows || targetCol < 0 || targetCol >= cols || grid[targetRow][targetCol]) {
    // Target is blocked, try to find nearest walkable or just return straight line (fallback)
    return [{ x: targetX, y: targetY }];
  }

  const openList: Node[] = [];
  const closedList: boolean[][] = Array.from({ length: rows }, () => Array(cols).fill(false));

  const startNode: Node = { x: startCol, y: startRow, g: 0, h: 0, f: 0, parent: null };
  openList.push(startNode);

  const dx = [0, 1, 0, -1, 1, 1, -1, -1];
  const dy = [-1, 0, 1, 0, -1, 1, 1, -1];

  while (openList.length > 0) {
    // Get node with lowest f
    let lowestIndex = 0;
    for (let i = 1; i < openList.length; i++) {
      if (openList[i].f < openList[lowestIndex].f) {
        lowestIndex = i;
      }
    }

    const currentNode = openList[lowestIndex];
    openList.splice(lowestIndex, 1);

    if (currentNode.x === targetCol && currentNode.y === targetRow) {
      // Reconstruct path
      let curr: Node | null = currentNode;
      const path: {x: number, y: number}[] = [];
      while (curr) {
        path.push({
          x: curr.x * TILE_SIZE + TILE_SIZE / 2, // center of tile
          y: curr.y * TILE_SIZE + TILE_SIZE / 2
        });
        curr = curr.parent;
      }
      path.reverse();
      // Replace last point with exact target, first with start (optional)
      if (path.length > 0) {
        path[path.length - 1] = { x: targetX, y: targetY };
        path.shift(); // remove start node tile center since we are already there
      }
      return path;
    }

    closedList[currentNode.y][currentNode.x] = true;

    for (let i = 0; i < 8; i++) {
      const nx = currentNode.x + dx[i];
      const ny = currentNode.y + dy[i];

      if (nx >= 0 && nx < cols && ny >= 0 && ny < rows && !grid[ny][nx] && !closedList[ny][nx]) {
        // Diagonal check: don't cut corners through walls
        if (i >= 4) {
          if (grid[currentNode.y][nx] || grid[ny][currentNode.x]) {
            continue;
          }
        }

        const gCost = currentNode.g + (i < 4 ? 1 : 1.414);
        let inOpen = false;
        for (const n of openList) {
          if (n.x === nx && n.y === ny) {
            inOpen = true;
            if (gCost < n.g) {
              n.g = gCost;
              n.f = n.g + n.h;
              n.parent = currentNode;
            }
            break;
          }
        }

        if (!inOpen) {
          const hCost = Math.hypot(targetCol - nx, targetRow - ny);
          openList.push({
            x: nx,
            y: ny,
            g: gCost,
            h: hCost,
            f: gCost + hCost,
            parent: currentNode
          });
        }
      }
    }
  }

  // No path found, fallback to straight line
  return [{ x: targetX, y: targetY }];
}

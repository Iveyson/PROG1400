from tile_type import TileType
from position import Position


class TileMap:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0
    def in_bounds(self, pos: Position) -> bool:
        return 0 <= pos.row < self.rows and 0 <= pos.col < self.cols
    
    def get_tile(self, pos: Position) -> TileType:
        if not self.in_bounds(pos):
            return TileType.WALL
        return self.grid[pos.row][pos.col]
    def is_walkable(self, pos: Position) -> bool:
        tile = self.get_tile(pos)
        return tile != TileType.WALL
if __name__ == "__main__":
    grid = [
        [TileType.WALL, TileType.WALL, TileType.WALL],
        [TileType.WALL, TileType.PATH, TileType.WALL],
        [TileType.WALL, TileType.WALL, TileType.WALL],
    ]

    world = TileMap(grid)

    print(world.is_walkable(Position(1, 1)))  # True
    print(world.is_walkable(Position(0, 0)))  # False
    print(world.is_walkable(Position(5, 5)))  # False
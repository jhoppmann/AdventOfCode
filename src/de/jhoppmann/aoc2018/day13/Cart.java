package de.jhoppmann.aoc2018.day13;

import java.util.Objects;

/**
 * @author jhoppman
 */
public class Cart implements Comparable<Cart> {
	static int ids = 0;
	int posX;
	int posY;
	Direction direction;
	int turnCycle = 0;

	@Override
	public boolean equals(Object o) {
		if (this == o) {
			return true;
		}
		if (o == null || getClass() != o.getClass()) {
			return false;
		}
		Cart cart = (Cart) o;
		return id == cart.id;
	}

	@Override
	public int hashCode() {
		return Objects.hash(id);
	}

	public int getId() {
		return id;
	}

	public int getX() {return posX;}

	public int getY() {return posY;}

	final int id;

	@Override
	public int compareTo(Cart o) {
		if (o.posY != posY) {
			return Integer.compare(posY, o.posY);
		} else {
			return Integer.compare(posX, o.posX);
		}
	}

	public enum Direction {
		UP,
		DOWN,
		LEFT,
		RIGHT
	}

	public boolean crashed(Cart other) {
		return other.posX == posX && other.posY == posY;
	}

	public Cart(int posX, int posY, Direction direction) {
		this.direction = direction;
		this.posX = posX;
		this.posY = posY;
		this.id = ids++;
	}

	@Override
	public String toString() {
		return posX + ", " + posY + " - " + direction.toString();
	}

	public void drive(char[][] tracks) {
		switch (direction) {

			case UP: posY--;
				break;
			case DOWN: posY++;
				break;
			case LEFT: posX--;
				break;
			case RIGHT: posX++;
				break;
		}
		char current = tracks[posY][posX];
		if (current == '+') {
			turnAtIntersection();
		}
		else if (current == '\\' || current== '/') {
			turnAtCurve(current);
		}
	}

	private void turnAtCurve(char curve) {
		switch (direction) {

			case UP: if (curve == '\\') {
				direction = Direction.LEFT;
			} else {
				direction = Direction.RIGHT;
			}
				break;
			case DOWN: if (curve == '\\') {
				direction = Direction.RIGHT;
			} else {
				direction = Direction.LEFT;
			}
				break;
			case LEFT: if (curve == '\\') {
				direction = Direction.UP;
			} else {
				direction = Direction.DOWN;
			}
				break;
			case RIGHT: if (curve == '\\') {
				direction = Direction.DOWN;
			} else {
				direction = Direction.UP;
			}
				break;
		}
	}

	private void turnAtIntersection() {
		if (direction == Direction.UP) {
			switch (turnCycle) {
				case 0: direction = Direction.LEFT;
						break;
				case 2: direction = Direction.RIGHT;
				break;
			}
		} else if (direction == Direction.DOWN) {
			switch (turnCycle) {
				case 0: direction = Direction.RIGHT;
					break;
				case 2: direction = Direction.LEFT;
					break;
			}
		} else if (direction == Direction.RIGHT) {
			switch (turnCycle) {
				case 0: direction = Direction.UP;
					break;
				case 2: direction = Direction.DOWN;
					break;
			}
		} else if (direction == Direction.LEFT) {
			switch (turnCycle) {
				case 0: direction = Direction.DOWN;
					break;
				case 2: direction = Direction.UP;
					break;
			}
		}

		turnCycle = (turnCycle+1)%3;
	}
}

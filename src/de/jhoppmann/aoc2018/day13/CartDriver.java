package de.jhoppmann.aoc2018.day13;

import java.util.*;

/**
 * @author jhoppman
 */
public class CartDriver {

	private static List<Cart> carts;
	static char[][] tracks = Input.loadInput();

	public static void main(String[] args) {
		carts = new ArrayList<>();
		driveCarts();

		removeCrashingCarts();
	}

	private static void removeCrashingCarts() {
		carts.clear();
		findCarts();
		Set<Cart> removedCarts = new HashSet<>();
		while (carts.size() - removedCarts.size() > 1) {
			Collections.sort(carts);
			for (Cart cart : carts) {
				if (!removedCarts.contains(cart)) {
					cart.drive(tracks);
					removeCollidedCarts(removedCarts);
				}
			}
		}
		for (Cart cart: carts) {
			if (!removedCarts.contains(cart)) {
				System.out.println(cart.toString());
			}
		}

	}

	private static void removeCollidedCarts(Set<Cart> crashedCarts) {
		for (Cart cart : carts) {
			for (Cart cart2 : carts) {
				if ( cart.getId() != cart2.getId() && cart.crashed(cart2) && !crashedCarts.contains(cart2) && !crashedCarts.contains(cart)) {
					crashedCarts.add(cart);
					crashedCarts.add(cart2);
				}
			}
		}
	}

	private static void driveCarts() {
		carts.clear();
		findCarts();
		boolean crashed = false;
		while (!crashed) {
			Collections.sort(carts);
			for (Cart cart : carts) {
				cart.drive(tracks);
				if (collided()) {
					crashed = true;
					System.out.println(cart.getX() + ", " + cart.getY());
					break;
				}
			}
		}
	}

	private static boolean collided() {
		for (Cart cart : carts) {
			for (Cart cart2 : carts) {
				if ( cart.getId() != cart2.getId() && cart.crashed(cart2)) {
					return true;
				}
			}
		}
		return false;
	}

	private static void findCarts() {
		for (int y = 0; y < tracks.length; y++) {
			for (int x = 0; x < tracks[y].length; x++) {
				char character = tracks[y][x];

				switch (character) {
					case '^': carts.add(new Cart(x, y, Cart.Direction.UP));
						break;
					case '>': carts.add(new Cart(x, y, Cart.Direction.RIGHT));
						break;
					case '<': carts.add(new Cart(x, y, Cart.Direction.LEFT));
						break;
					case 'v': carts.add(new Cart(x, y, Cart.Direction.DOWN));
						break;
				}
			}
		}
	}
}

package de.jhoppmann.aoc2018.day10;

import de.jhoppmann.aoc2018.day10.Input.Light;

import java.util.Date;
import java.util.List;

/**
 * @author jhoppman
 */
public class LightPathCalculator {

	public static void main(String[] args) {

		List<Light> lights = Input.getLights();
		System.out.println(new Date().getTime());
		int ySize = getYSize(lights);
		int counter = 0;
		while (ySize > 20 ) {
			lights.forEach(Light::move);
			ySize =getYSize(lights);
			counter++;
		}
		System.out.println(new Date().getTime());
		while (getYSize(lights) <= 20) {
			boolean[][] stars = new boolean[getXSize(lights) + 1][getYSize(lights) + 1];

			for (Light light : lights) {
				int x =0, y = 0;
				try {
					x = light.getX() - getMinX(lights);
					y = light.getY() - getMinY(lights);
					stars[x][y] = true;
				} catch (IndexOutOfBoundsException e) {
					System.out.println("[" + x + "][" + y + "]: " +light + ", " + getMinX(lights) + ", " + getMinY(lights));
				}
			}
			for (boolean[] outer : stars) {
				StringBuilder line = new StringBuilder();
				for (boolean inner : outer) {
					if (inner) {
						line.append("*");
					}
					else {
						line.append(" ");
					}
				}
				System.out.println(line.toString());
			}
			System.out.println(counter + "--------------------------------------");


			lights.forEach(Light::move);
			counter++;
		System.out.println(new Date().getTime());
		}
	}

	private static int getXSize(List<Light> lights) {
		return getMaxX(lights) - getMinX(lights);
	}

	private static int getMaxX(List<Light> lights) {
		return lights.stream().mapToInt(Light::getX).max().orElse(0);
	}

	private static int getMinX(List<Light> lights) {
		return lights.stream().mapToInt(Light::getX).min().orElse(0);
	}

	private static int getYSize(List<Light> lights) {
		return getMaxY(lights) - getMinY(lights);

	}

	private static int getMaxY(List<Light> lights) {
		return lights.stream().mapToInt(Light::getY).max().orElse(0);
	}

	private static int getMinY(List<Light> lights) {
		return lights.stream().mapToInt(Light::getY).min().orElse(0);
	}
}

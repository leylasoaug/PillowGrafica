from PIL import Image, ImageDraw
from math import radians, tan


def find_base(height):
    angle_in_radians = radians(30) # 30 degrees in radians
    base = 2 * height * tan(angle_in_radians)
    return base


def midpoint(p1, p2):
    return ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)

def draw_sierpinski_triangle(draw, depth, p1, p2, p3):
    if depth == 0:
        draw.polygon([p1, p2, p3], fill="#A0B0C0", outline="#A0B0C0")
    else:
        # Find the midpoints of the sides of the triangle
        mid1 = midpoint(p1, p2)
        mid2 = midpoint(p2, p3)
        mid3 = midpoint(p1, p3)

        # Recursively draw three subtriangles
        draw_sierpinski_triangle(draw, depth-1, p1, mid1, mid3)
        draw_sierpinski_triangle(draw, depth-1, p2, mid1, mid2)
        draw_sierpinski_triangle(draw, depth-1, p3, mid2, mid3)

def main():
    # Create an image
    height = 1080
    width = int(find_base(height))
    image = Image.new("RGB", (width, height), "#4A5459")
    draw = ImageDraw.Draw(image)

    # Determine the vertices of the starting triangle
    base = int(find_base(height))
    p1 = (width - base // 2, 0)
    p2 = (width - base, height)
    p3 = (width, height)

    # Draw the Sierpinski triangle
    draw_sierpinski_triangle(draw, depth=7, p1=p1, p2=p2, p3=p3)

    # Save the image
    image.save("sierpinski_triangle.png")

if __name__ == "__main__":
    main()

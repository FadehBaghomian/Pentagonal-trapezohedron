import turtle
import math

# Setup the screen and turtle
screen = turtle.Screen()
screen.bgcolor("light blue")  # Set background to light blue
screen.title("Spinning Pentagonal Trapezohedron")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Define vertices of a pentagonal trapezohedron
vertices = [
    [0, 0, 100],  # Top vertex
    [math.cos(2 * math.pi / 5) * 100, math.sin(2 * math.pi / 5) * 100, 50],
    [math.cos(4 * math.pi / 5) * 100, math.sin(4 * math.pi / 5) * 100, 50],
    [math.cos(6 * math.pi / 5) * 100, math.sin(6 * math.pi / 5) * 100, 50],
    [math.cos(8 * math.pi / 5) * 100, math.sin(8 * math.pi / 5) * 100, 50],
    [math.cos(10 * math.pi / 5) * 100, math.sin(10 * math.pi / 5) * 100, 50],
    [math.cos(2 * math.pi / 5) * 100, math.sin(2 * math.pi / 5) * 100, -50],
    [math.cos(4 * math.pi / 5) * 100, math.sin(4 * math.pi / 5) * 100, -50],
    [math.cos(6 * math.pi / 5) * 100, math.sin(6 * math.pi / 5) * 100, -50],
    [math.cos(8 * math.pi / 5) * 100, math.sin(8 * math.pi / 5) * 100, -50],
    [math.cos(10 * math.pi / 5) * 100, math.sin(10 * math.pi / 5) * 100, -50],
    [0, 0, -100]  # Bottom vertex
]

# Define faces connecting the vertices
faces = [
    [0, 1, 2], [0, 2, 3], [0, 3, 4], [0, 4, 5], [0, 5, 1],
    [6, 7, 11], [7, 8, 11], [8, 9, 11], [9, 10, 11], [10, 6, 11],
    [1, 2, 7, 6], [2, 3, 8, 7], [3, 4, 9, 8], [4, 5, 10, 9], [5, 1, 6, 10]
]

# Define colors for each face
colors = [
    "red", "green", "blue", "yellow", "cyan",
    "magenta", "orange", "purple", "lime", "pink",
    "brown", "gray", "violet", "navy", "gold"
]


# Rotate around X-axis
def rotateX(point, angle):
    rad = math.radians(angle)
    cosA = math.cos(rad)
    sinA = math.sin(rad)
    y = point[1] * cosA - point[2] * sinA
    z = point[1] * sinA + point[2] * cosA
    return [point[0], y, z]


# Rotate around Y-axis
def rotateY(point, angle):
    rad = math.radians(angle)
    cosA = math.cos(rad)
    sinA = math.sin(rad)
    x = point[0] * cosA + point[2] * sinA
    z = -point[0] * sinA + point[2] * cosA
    return [x, point[1], z]


# Rotate around Z-axis
def rotateZ(point, angle):
    rad = math.radians(angle)
    cosA = math.cos(rad)
    sinA = math.sin(rad)
    x = point[0] * cosA - point[1] * sinA
    y = point[0] * sinA + point[1] * cosA
    return [x, y, point[2]]


# Project 3D point to 2D
def project(point):
    distance = 300
    factor = distance / (distance - point[2])
    x = point[0] * factor
    y = point[1] * factor
    return [x, y]


# Draw the polyhedron
def draw_polyhedron():
    t.clear()
    # Rotate the polyhedron
    rotated_vertices = [rotateX(rotateY(rotateZ(v, angleZ), angleY), angleX) for v in vertices]
    projected_vertices = [project(v) for v in rotated_vertices]

    # Calculate the average Z value for each face
    face_depths = []
    for i, face in enumerate(faces):
        z_sum = sum(rotated_vertices[vertex][2] for vertex in face)
        face_depths.append((z_sum / len(face), i))

    # Sort faces by depth (farthest first)
    face_depths.sort(reverse=True)

    # Draw faces with different colors
    for depth, i in face_depths:
        face = faces[i]
        t.penup()
        t.goto(projected_vertices[face[0]][0], projected_vertices[face[0]][1])
        t.pendown()
        t.begin_fill()
        t.color(colors[i % len(colors)])
        for vertex in face:
            t.goto(projected_vertices[vertex][0], projected_vertices[vertex][1])
        t.goto(projected_vertices[face[0]][0], projected_vertices[face[0]][1])
        t.end_fill()

    screen.update()


# Initial rotation angles
angleX = 0
angleY = 0
angleZ = 0


# Animation loop
def animate():
    global angleX, angleY, angleZ
    angleX += 2
    angleY += 3
    angleZ += 1
    draw_polyhedron()
    screen.ontimer(animate, 50)


# Initialize animation
screen.tracer(0)
animate()
screen.mainloop()
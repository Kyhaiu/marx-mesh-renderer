from matplotlib import pyplot as plt
from models.vertex import Vertex
from objects.test import pyramid
from utils.pipeline import normalize_by_homogeneous_coordinate, transformSRCtoSRT, transformSRUtoSRC, projectionMatrix


def main():
    vertexes = pyramid.vertexes_object
    faces = pyramid.face_objects
    half_edges = pyramid.half_edges

    # for he in half_edges:
    #     print(he)

    # # for vertex in vertexes:
    # #     print(vertex)

    vrp = Vertex(50, 15, 30)
    p = Vertex(20, 6, 15)

    mSRUtoSRC = transformSRUtoSRC(vrp, p)

    print("First Step - Transform the SRU to SRC")

    pyramid.apply_transformation(mSRUtoSRC)

    # vertexes = pyramid.getVertexesObject()

    # for vertex in vertexes:
    #     print(vertex)

    print("\n\nSecond Step - Obtain the projection matrix")

    mJp = projectionMatrix(vrp, p, d=17)

    pyramid.apply_transformation(mJp)

    # vertexes = pyramid.getVertexesObject()

    # for vertex in vertexes:
    #     print(vertex)

    print("\n\nThird Step - Divide by homogeneous coordinate")

    for vertex in vertexes:
        normalize_by_homogeneous_coordinate(vertex)
        # print(vertex)

    print("\n\nFourth Step - Transform the SRC to SRT")

    u = [0, 320]
    v = [0, 240]
    y = [-8, 8]
    x = [-5, 5]

    mSRCtoSRT = transformSRCtoSRT(x, y, u, v)

    pyramid.apply_transformation(mSRCtoSRT)

    vertexes = pyramid.vertexes_object

    for vertex in vertexes:
        print(vertex)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the vertices
    x = [v.x for v in vertexes]
    y = [v.y for v in vertexes]
    z = [v.z for v in vertexes]
    ax.scatter(x, y, z, c='red', marker='o')

    for he in half_edges:
        start = he.origin
        end = he.twin.origin
        ax.plot([start.x, end.x], [start.y, end.y],
                [start.z, end.z], c='black')

    # Set plot limits
    ax.set_xlim(u[0], u[1])
    ax.set_ylim(v[0], v[1])
    ax.set_zlim(-30, 30)

    # Set axis labels
    ax.set_xlabel('Z')
    ax.set_ylabel('X')
    ax.set_zlabel('Y')

    # Show the plot
    plt.show()


main()

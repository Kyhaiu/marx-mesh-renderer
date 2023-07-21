import cv2
import os
import numpy as np

# Path to the folder containing character images
folder_path = "./utils/stand_alone/individual_characters"

# Path to the folder to save the output
output_path = "./objects"

# padding to add to the character image
padding = 10
file_output = ""


# Iterate through the images in the folder
for image_file in os.listdir(folder_path):
    file_output = ""
    # Load the character image
    image_path = os.path.join(folder_path, image_file)
    image = cv2.imread(image_path)
    print("reading image: ", image_path)

    # Add padding to the image
    image = cv2.copyMakeBorder(
        image, padding, padding, padding, padding, cv2.BORDER_CONSTANT, value=(
            0, 0, 255)
    )

    print("image shape: ", image.shape)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to convert it to a binary image
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Apply cornerHarris to detect corners
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray, blockSize=3, ksize=3, k=0.04)

    # Threshold the Harris response and obtain potential corners
    threshold = 0.01 * dst.max()
    corner_locations = np.where(dst > threshold)
    # Swap x and y coordinates
    corners = np.column_stack((corner_locations[1], corner_locations[0]))

    # Convert corners to float32
    corners = corners.astype(np.float32)

    print("corners extracted: ", corners.shape[0])

    # Refine corner points
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.1)
    corners_refined = cv2.cornerSubPix(
        gray, corners, (5, 5), (-1, -1), criteria)

    corners_list = []
    found = False

    print("corners refined: ", corners_refined.shape[0])

    # add the vertices
    # due to the way the corners are detected, some values are extremely close to each other
    # so we need to remove the duplicates
    for corner in corners_refined:
        x, y = corner.ravel()
        # cv2.circle(image, (int(x), int(y)), 1, 255, -1)
        for corner2 in corners_list:
            x2, y2, z2 = corner2
            if (abs(int(x) - int(x2)) == 0 and abs(int(y) - int(y2)) == 0) or \
               (abs(int(x) - int(x2)) == 1 and abs(int(y) - int(y2)) == 0) or \
               (abs(int(x) - int(x2)) == 0 and abs(int(y) - int(y2)) == 1) or \
               (abs(int(x) - int(x2)) == 1 and abs(int(y) - int(y2)) == 1):
                found = True
                break
            else:
                continue

        if not found:
            # normalize the values between -1 and 1
            corners_list.append([int(x), int(y), -0.5])
        else:
            found = False

    print("removed duplicates: ", len(corners_refined) - len(corners_list))
    print("making the object 3D")

    corners_list_3d = corners_list.copy()

    # duplicate the vertices and add the z=0.5 vertices
    # this is to make the object 3D
    for corner in corners_list:
        x, y, z = corner
        # corners_list.append([x, y, 0.5])
        corners_list_3d.append([x, y, 0.5])

    print("object 3D: ", len(corners_list_3d))

    print("finding the max and min x and y values")

    # find the maximum x, y values
    max_x = 0
    max_y = 0
    for corner in corners_list_3d:
        x, y, z = corner
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    # find the minimum x, y values
    min_x = max_x
    min_y = max_y
    for corner in corners_list_3d:
        x, y, z = corner
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y

    print("max x: ", max_x)
    print("max y: ", max_y)
    print("min x: ", min_x)
    print("min y: ", min_y)

    print("normalizing the vertices")

    # normalize the vertices between 0 and 1
    for i, corner in enumerate(corners_list_3d):
        x, y, z = corner
        x = (x - min_x) / (max_x - min_x)
        y = (y - min_y) / (max_y - min_y)

        if z == -0.5:
            corners_list_3d[i] = [x+1, y+1, -0.5]
        else:
            corners_list_3d[i] = [x-1, y, z]

        # corners_list_3d[i] = [x, y, z]

        # x, y, z = corner
        # x = (x - min_x) / (max_x - min_x) * 2 - 1
        # y = (y - min_y) / (max_y - min_y) * 2 - 1

        # if z == -0.5:
        #     corners_list_3d[i] = [x, y, 0.5]
        # else:
        #     corners_list_3d[i] = [x, y, z]

    print("writing the file")

    model_name = image_file.replace('.jpg', '').replace('char_', '')
    file_output += f"from models.vertex import Vertex\n"
    file_output += f"from models.object import Object\n"
    file_output += f"\n"
    file_output += f"# The model of {model_name}\n"

    # rotate the vertices
    # corners_list = np.flip(corners_list, 0)

    for i, corner in enumerate(corners_list_3d):
        file_output += f"VERTEX_{i+1} = Vertex(x={corner[0]}, y={corner[1]}, z={corner[2]}, id={i})\n"
        # print(f"v {corner[0]} {corner[1]} 0")

    file_output += f"\n"

    for i, corner in enumerate(corners_list_3d):
        file_output += f"# v {corner[0]} {corner[1]} {corner[2]}\n"

    f = open(os.path.join(output_path, 'char_'+model_name + ".py"), "w")
    f.write(file_output)
    f.close()

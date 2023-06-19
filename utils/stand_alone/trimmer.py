import cv2
import numpy as np


def main():
    # import the image an turn into binary
    image = cv2.imread("./utils/stand_alone/urss-font.jpg")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    char_images = []
    for contour in contours:
        """
          This is suboptimal, but it works for now.

          In some cases, the character image is separated into two(or more) contours.
          in this scenario, we need to merge the contours into one, and then
          extract the character image from the original image.

          But the focus of this stand alone module for now is to extract the
          individual character(A-Z 0-9) images from the original image. 
        """
        x, y, w, h = cv2.boundingRect(contour)
        # print(f"X: {x}, Y: {y}, W: {w}, H: {h}")
        char_image = image[y:y+h, x:x+w]
        char_images.append(char_image)

    for i, char_image in enumerate(char_images):
        # Save each character image
        cv2.imwrite(
            f"./utils/stand_alone/individual_characters/char_{i}.jpg", char_image)
        # cv2.imshow("Character", char_image)  # Display each character image
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

import cv2
import numpy as np
import json  # We will use JSON to save the points
import os

# ======================================================
# --- 1. CONFIGURATION ---
# ======================================================

IMAGE_PATH = 'image.jpeg'  # Make sure this matches your image name
POINTS_FILE_PATH = 'points.json'  # The file where points will be saved

# ======================================================
# --- 2. GLOBAL VARIABLES ---
# ======================================================

clicked_points = []
clone = None
selection_order = [
    "Reference Top (Notebook)",
    "Reference Base (Notebook)",
    "Unknown Top (Bottle)",
    "Unknown Base (Bottle)"
]


# ======================================================
# --- 3. MOUSE CLICK HANDLER ---
# ======================================================

def click_and_mark(event, x, y, flags, param):
    """Mouse callback function"""
    global clone

    if event == cv2.EVENT_LBUTTONDOWN and len(clicked_points) < 4:
        coords = (x, y)
        clicked_points.append(coords)

        num = len(clicked_points)

        # Draw feedback on the image
        cv2.circle(clone, coords, 5, (0, 255, 0), -1)
        cv2.putText(clone, str(num), (x + 10, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("Image", clone)

        # Give console feedback
        if num < 4:
            print(f"Clicked {selection_order[num - 1]}. Next: {selection_order[num]}")
        else:
            print("✅ All 4 points selected! Press 's' to save or 'r' to reset.")


# ======================================================
# --- 4. MAIN SCRIPT EXECUTION ---
# ======================================================

img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"Image not found at '{IMAGE_PATH}'.")

clone = img.copy()
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", click_and_mark)

print("--- Point Selector Tool ---")
print(f"Click #1: {selection_order[0]}")
print("\nPress 'r' to reset points.")
print("Press 's' to save and quit.")
print("Press 'q' to quit without saving.")

while True:
    cv2.imshow("Image", clone)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('r'):
        clone = img.copy()
        clicked_points.clear()
        print("\nPoints reset!")
        print(f"Click #1: {selection_order[0]}")

    elif key == ord('q'):
        print("\nQuitting without saving.")
        break

    elif key == ord('s'):
        if len(clicked_points) == 4:
            # Save the points in a structured way
            data = {
                "ref_top": clicked_points[0],
                "ref_base": clicked_points[1],
                "obj_top": clicked_points[2],
                "obj_base": clicked_points[3]
            }

            with open(POINTS_FILE_PATH, 'w') as f:
                json.dump(data, f, indent=4)

            print(f"\n✅ Points saved successfully to {POINTS_FILE_PATH}")
            break
        else:
            print("\nError: Please select all 4 points before saving.")

cv2.destroyAllWindows()
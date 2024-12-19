import math

def calculate_angle_from_nose_to_shoulders(landmark_0, landmark_11, landmark_12, display_image):
    # Access x, y attributes directly
    x0, y0 = int(landmark_0.x * display_image.shape[1]), int(landmark_0.y * display_image.shape[0])
    x11, y11 = int(landmark_11.x * display_image.shape[1]), int(landmark_11.y * display_image.shape[0])
    x12, y12 = int(landmark_12.x * display_image.shape[1]), int(landmark_12.y * display_image.shape[0])

    # Calculate the vectors from the nose to the left and right shoulder
    vector_left = (x11 - x0, y11 - y0)  # From nose to left shoulder
    vector_right = (x12 - x0, y12 - y0)  # From nose to right shoulder

    # Calculate the dot product of the vectors
    dot_product_left = vector_left[0] * vector_right[0] + vector_left[1] * vector_right[1]

    # Calculate the magnitudes (lengths) of the vectors
    magnitude_left = math.sqrt(vector_left[0]**2 + vector_left[1]**2)
    magnitude_right = math.sqrt(vector_right[0]**2 + vector_right[1]**2)

    # Compute the cosine of the angle between the vectors
    cos_angle = dot_product_left / (magnitude_left * magnitude_right)

    # To prevent potential floating-point errors that make the cosine slightly out of range [-1, 1]
    cos_angle = max(-1.0, min(1.0, cos_angle))

    # Calculate the angle in radians and convert it to degrees
    angle_radians = math.acos(cos_angle)
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees, (x0, y0), (x11, y11), (x12, y12)


import math

def calculate_angle_at_left_shoulder(landmark_0, landmark_11, landmark_12, display_image):
    # Access x, y attributes directly
    x0, y0 = int(landmark_0.x * display_image.shape[1]), int(landmark_0.y * display_image.shape[0])
    x11, y11 = int(landmark_11.x * display_image.shape[1]), int(landmark_11.y * display_image.shape[0])
    x12, y12 = int(landmark_12.x * display_image.shape[1]), int(landmark_12.y * display_image.shape[0])

    # Calculate the vectors from the left shoulder (landmark 11) to the nose (landmark 0), and to the right shoulder (landmark 12)
    vector_left_to_nose = (x0 - x11, y0 - y11)  # Vector from left shoulder to nose
    vector_left_to_right_shoulder = (x12 - x11, y12 - y11)  # Vector from left shoulder to right shoulder

    # Calculate the dot product of the vectors
    dot_product = vector_left_to_nose[0] * vector_left_to_right_shoulder[0] + vector_left_to_nose[1] * vector_left_to_right_shoulder[1]

    # Calculate the magnitudes (lengths) of the vectors
    magnitude_left_to_nose = math.sqrt(vector_left_to_nose[0]**2 + vector_left_to_nose[1]**2)
    magnitude_left_to_right_shoulder = math.sqrt(vector_left_to_right_shoulder[0]**2 + vector_left_to_right_shoulder[1]**2)

    # Compute the cosine of the angle between the vectors
    cos_angle = dot_product / (magnitude_left_to_nose * magnitude_left_to_right_shoulder)

    # To prevent potential floating-point errors that make the cosine slightly out of range [-1, 1]
    cos_angle = max(-1.0, min(1.0, cos_angle))

    # Calculate the angle in radians and then convert to degrees
    angle_radians = math.acos(cos_angle)
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees, (x11, y11), (x0, y0), (x12, y12)

def calculate_angle_at_right_shoulder(landmark_0, landmark_11, landmark_12, display_image):
    # Access x, y attributes directly
    x0, y0 = int(landmark_0.x * display_image.shape[1]), int(landmark_0.y * display_image.shape[0])
    x11, y11 = int(landmark_11.x * display_image.shape[1]), int(landmark_11.y * display_image.shape[0])
    x12, y12 = int(landmark_12.x * display_image.shape[1]), int(landmark_12.y * display_image.shape[0])

    # Calculate the vectors from the right shoulder (landmark 12) to the nose (landmark 0), and to the left shoulder (landmark 11)
    vector_right_to_nose = (x0 - x12, y0 - y12)  # Vector from right shoulder to nose
    vector_right_to_left_shoulder = (x11 - x12, y11 - y12)  # Vector from right shoulder to left shoulder

    # Calculate the dot product of the vectors
    dot_product = vector_right_to_nose[0] * vector_right_to_left_shoulder[0] + vector_right_to_nose[1] * vector_right_to_left_shoulder[1]

    # Calculate the magnitudes (lengths) of the vectors
    magnitude_right_to_nose = math.sqrt(vector_right_to_nose[0]**2 + vector_right_to_nose[1]**2)
    magnitude_right_to_left_shoulder = math.sqrt(vector_right_to_left_shoulder[0]**2 + vector_right_to_left_shoulder[1]**2)

    # Compute the cosine of the angle between the vectors
    cos_angle = dot_product / (magnitude_right_to_nose * magnitude_right_to_left_shoulder)

    # To prevent potential floating-point errors that make the cosine slightly out of range [-1, 1]
    cos_angle = max(-1.0, min(1.0, cos_angle))

    # Calculate the angle in radians and then convert to degrees
    angle_radians = math.acos(cos_angle)
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees, (x12, y12), (x0, y0), (x11, y11)


from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings 
from PIL import Image
import numpy as np
import tensorflow as tf
import cv2
import os
import base64
from io import BytesIO

MODEL_PATH = "../models1/malaria-detection-model.h5"

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to get heatmap
def get_heatmap(image):
    img_array = preprocess_image(image)
    last_conv_layer = model.layers[-5].output  # Get the output of the last convolutional layer
    heatmap_model = tf.keras.models.Model(inputs=model.inputs, outputs=last_conv_layer)
    heatmap = heatmap_model.predict(img_array)[0]
    heatmap = np.mean(heatmap, axis=-1)
    heatmap = np.maximum(heatmap, 0)
    heatmap /= np.max(heatmap)
    return heatmap

# Function to overlay heatmap on the image
def overlay_heatmap(image, heatmap):
    # Resize heatmap to match image dimensions
    heatmap = cv2.resize(heatmap, (image.width, image.height))
    # Create a binary mask where heatmap values are above a certain threshold
    threshold = 0.5  # Adjust threshold as needed
    heatmap_binary = (heatmap > threshold).astype(np.uint8)
    # Apply the binary mask to the original image
    overlaid_image = np.copy(np.array(image))
    overlaid_image[heatmap_binary == 1] = [255, 0, 0]  # Highlight areas in red
    
    # Convert the overlaid image to PIL Image format
    overlaid_image_pil = Image.fromarray(overlaid_image)
    
    # Convert the PIL Image to base64-encoded string
    overlaid_image_base64 = image_to_base64(overlaid_image_pil)

    return overlaid_image_base64


# Django view
def malaria_classification(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        try:
            # Load the image
            image = Image.open(uploaded_file)
            # Preprocess the image
            processed_image = preprocess_image(image)
            # Predict
            prediction = model.predict(processed_image)[0]
            if prediction[0] > 0.2:
                prediction_text = "Infected"
            else:
                prediction_text = "Uninfected"

            # Get heatmap
            heatmap = get_heatmap(image)
            # Overlay heatmap on the original image
            overlay = overlay_heatmap(image, heatmap)

            # Convert images to base64-encoded strings
            image_base64 = image_to_base64(image)

            # Pass results to the template
            return render(request, 'malaria_classification/result.html', 
                          {'prediction': prediction_text, 'image': image_base64, 'overlay': overlay})

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render(request, 'malaria_classification/error.html', {'error_message': error_message})

    return render(request, 'malaria_classification/upload.html')

# Function to convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

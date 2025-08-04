from PIL import Image
import random

def detect_ingredients(image: Image.Image):
    # Dummy ingredient detection — randomly picks 3 ingredients
    ingredients = ["cheese", "chicken", "tomato", "lettuce", "beef", "bun", "avocado"]
    return random.sample(ingredients, 3)

def nutrition_analysis(ingredients):
    notes = {
        "cheese": "High in calcium, but limit saturated fats.",
        "chicken": "Lean protein; good for muscle repair.",
        "tomato": "Loaded with antioxidants like lycopene.",
        "lettuce": "Hydrating and low-calorie.",
        "beef": "Rich in protein and iron, eat moderately.",
        "bun": "Choose whole grain to reduce refined carbs.",
        "avocado": "Heart-healthy fats and fiber."
    }
    return "\n".join([f"{item.capitalize()}: {notes[item]}" for item in ingredients])

def analyze_image(image):
    detected = detect_ingredients(image)
    nutrition = nutrition_analysis(detected)
    return image, ", ".join(detected), nutrition

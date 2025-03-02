import numpy as np
import joblib

model = joblib.load("model/fitness_model.pkl")


def get_user_input():
    print("\nPlease enter your fitness details below:\n")
    
    age = int(input("Age: "))
    duration = int(input("Workout Duration (minutes): "))
    steps = int(input("Steps Taken: "))
    sleep = float(input("Sleep Hours: "))
    water = float(input("Water Intake (liters): "))
    calories = int(input("Daily Calories Intake: "))
    
    gender = input("Gender (male/female): ").strip().lower()
    male = 1 if gender == "male" else 0  
    
    activity = input("Enter your activity (cycling, running, strength, swimming, hiit): ").strip().lower()
    cycling = 1 if activity == "cycling" else 0  

    intensity = input("Workout Intensity (low/medium/high): ").strip().lower()
    low_intensity = 1 if intensity == "low" else 0  

    post_workout = input("How do you feel post-workout? (Neutral/Tired/Energetic): ").strip().lower()
    fatigued = 1 if post_workout == "tired" else 0  

    BMI = float(input("BMI: "))

    user_data = np.array([[age, duration, steps, sleep, water, calories, male, cycling, low_intensity, fatigued, BMI]])
    
    return user_data

def predict_fitness(user_data):
    predictions = ["Low fitness performance", "High fitness performance"]
    
    prediction = model.predict(user_data)
    
    return predictions[prediction[0]]

user_input = get_user_input()
result = predict_fitness(user_input)

print(f"\n Your Fitness Performance: {result}")






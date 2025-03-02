# Fitness Performance Tracker (K-Means Clustering)

## 🚀 Overview
This project uses **K-Means clustering** to classify fitness performance into **low (1) and high (0)** categories based on a Kaggle dataset.  
The goal is to analyze which features impact performance and provide insights.

## 📊 Dataset & Features
- **Source:** fitness.csv file in the 
- **Key Features Used:** Heart Rate, Steps, Workout Duration, etc.
- **Features with Low Impact:** VO2 Max, Calories Burned

## 🧠 Machine Learning Approach
- Used **K-Means Clustering** to group users based on fitness levels.
- Used SVC training model that proved to be one of the better choices for model selection.
- Validated clusters using **Elbow Method & Silhouette Score**.

## 📈 Results & Insights
- Found that **steps,workout intensity,water & calories intake,age,BMI...** had more impact than other features.
- Identified key differences between **high & low performance** groups.





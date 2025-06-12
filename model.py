import warnings 
import pandas as pd 
import pickle 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv("C:/Users/Garvu/Desktop/projects/ML/health_data.csv")  # Make sure to replace 'your_dataset.csv' with the actual file name

# Suppress warnings
warnings.filterwarnings(action='ignore') 

# Specify the actual names of your categorical columns for one-hot encoding
categorical_columns = ['categorical_column1', 'categorical_column2']  # Replace with actual column names

# Verify column names
missing_columns = [col for col in categorical_columns if col not in df.columns]
if missing_columns:
    raise ValueError(f"The following categorical columns are not present in the dataset: {missing_columns}")

# One-hot encode categorical columns
df = pd.get_dummies(df, columns=categorical_columns)

# Separate features and target variable
y = df['cardio'] 
X = df.drop(["smoke", "id", "alco", "cardio", "Unnamed: 0"], axis=1) 

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, shuffle=True, random_state=1) 

# Initialize and train the model
model = GradientBoostingClassifier() 
model.fit(X_train, y_train) 

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the model to disk
pickle.dump(model, open("model.pkl", "wb"))

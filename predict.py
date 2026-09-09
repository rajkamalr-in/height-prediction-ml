import os
import joblib
import numpy as np

def run_interactive_inference():
    model_path = "model.joblib"

    # Check if trained model artifact exists
    if not os.path.exists(model_path):
        print(f"❌ Error: '{model_path}' not found! Run 'python train.py' first to train the model.")
        return

    # Load pre-trained model
    model = joblib.load(model_path)
    print("✅ Pre-trained model loaded successfully!\n")
    print("==================================================")
    print("   HEIGHT PREDICTION CLI (Simple Linear Regression)")
    print("==================================================")
    print("Type 'exit' or 'q' anytime to quit.\n")

    while True:
        user_input = input("Enter weight in kg (e.g., 56): ").strip()

        if user_input.lower() in ['exit', 'q']:
            print("Exiting program. Goodbye!")
            break

        try:
            # Convert user input to float
            weight = float(user_input)

            if weight <= 0:
                print("⚠️ Please enter a positive weight value.\n")
                continue

            # Reshape input into 2D array expected by scikit-learn: [[weight]]
            input_data = np.array([[weight]])

            # Predict height
            predicted_height = model.predict(input_data)[0]

            print(f"➡️  Predicted Height for {weight} kg: {predicted_height:.2f} cm\n")

        except ValueError:
            print("❌ Invalid input! Please enter a numerical value (e.g., 56 or 72.5).\n")

if __name__ == "__main__":
    run_interactive_inference()
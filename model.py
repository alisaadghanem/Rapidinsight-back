import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import logging


class DiabetesModel:
    def __init__(self, dataset_path):
        self.df = pd.read_csv(dataset_path)
        self.features = self.df.drop("class", axis=1)
        self.target = self.df["class"]
        self.scaler = StandardScaler()
        self.scaler.fit(self.features)
        # Train the SVM model during initialization
        self.model = self._train_model()

    def _train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(
            self.features, self.target, test_size=0.2, random_state=42
        )
        X_train_scaled = self.scaler.transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        model = SVC(kernel="linear", C=1.0)
        logging.info("SVM model created. starting the training...")
        model.fit(X_train_scaled, y_train)
        # log the results and the score of the model
        logging.info(
            f"Training score: {model.score(X_train_scaled, y_train)}"
            f"Test score: {model.score(X_test_scaled, y_test)}"
        )
        return model

    def predict(self, input_data):
        # convert data from dict to features
        input_data = pd.DataFrame([input_data])
        # Preprocess input_data as needed (scaling, etc.)
        scaled_input = self.scaler.transform(input_data)
        prediction = self.model.predict(scaled_input)
        return prediction

# Movie Recommendation System - README

This project implements a movie recommendation system using FastAPI and a web client. The recommendation system is based on clustering and association learning techniques.

## Project Structure

The project is organized as follows:

```bash
final-project/
├── api/
│ ├── pickle/
│ ├── api_test.py
│ └── main.py
├── client/
│ ├── static/
│ │ ├── script.js
│ │ └── styles.css
│ └── index.html
├── dataset/
│ ├── netflix_titles.csv
│ └── titles.csv
├── models/
│ ├── association_learning.py
│ └── k_means.py
├── notebooks/
│ ├── mock_data_generator/
│ ├── mock_user_data.csv
│ └── preprocessing.ipynb
├── .gitignore
├── Dockerfile
└── requirements.txt
```

- `api/`: Contains the FastAPI application code and the serialized pickle model.
- `client/`: Contains the web client code, including JavaScript and CSS files.
- `dataset/`: Contains the dataset files used for training the model.
- `models/`: Contains the machine learning models used for recommendation.
- `notebooks/`: Contains Jupyter notebooks for data preprocessing and generating mock data.
- `.gitignore`: Specifies files and directories to be ignored by version control.
- `Dockerfile`: Defines the Docker image configuration for containerizing the application.
- `requirements.txt`: Lists the Python dependencies for the project.

## How to Run the Project

To run the project, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.

2. Preprocess the dataset and generate the required files by running the `preprocessing.ipynb` notebook in the `notebooks/` directory. Note: Don't forget to unzip preprocessed.csv.zip and titles.pkl.zip to move directly.

3. Train the recommendation model using the processed dataset by running the appropriate scripts in the `models/` directory.

4. Start the FastAPI server by running `python api/main.py`.

5. Open the web client by opening the `client/index.html` file in a web browser.

6. Enter a username in the input field and click the "Get Movies" button to receive movie recommendations.

### Running with Docker

To run the project using Docker, follow these additional steps:

1. Build the Docker image by running `docker build -t movie-recommendation-system .` in the root directory of the project. Make sure you have Docker installed.

2. Once the image is built, run the Docker container by executing `docker run -p 8000:8000 movie-recommendation-system`.

3. Open a web browser and navigate to `http://localhost:8000` to access the web client.

Note: Make sure to update the necessary configuration settings, such as CORS origins, in the `main.py` file and the web client code as per your requirements.

Feel free to modify and customize the project structure and files to suit your specific needs.

That's it! You should now have the project set up and ready to run.
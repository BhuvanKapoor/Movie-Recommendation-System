# Movie Recommendation System

This project implements a movie recommendation system using cosine similarity and TF-IDF vectorization. Given a movie title as input, the system recommends similar movies based on their descriptions, genres, keywords, taglines, cast, and director.

## Dataset

The dataset used in this project is `movies.csv`, which contains information about various movies, including their titles, genres, keywords, taglines, cast, and directors.

## Implementation

1. **Data Preparation**: The relevant features from the dataset (`genres`, `keywords`, `tagline`, `cast`, `director`) are selected and combined into a single feature called `combined_features`.

2. **Vectorization**: The `combined_features` are converted into numerical feature vectors using TF-IDF vectorization (`TfidfVectorizer` from scikit-learn).

3. **Similarity Calculation**: The cosine similarity between all pairs of movie feature vectors is calculated using `cosine_similarity` from scikit-learn.

4. **User Input**: The user is prompted to enter a movie title.

5. **Finding Close Match**: If the user's input doesn't exactly match a movie title in the dataset, the closest match is found using `difflib.get_close_matches`.

6. **Retrieving Similar Movies**: The index of the user's input movie (or its closest match) is used to retrieve its corresponding similarity scores with all other movies. These scores are then sorted in descending order.

7. **Recommendations**: The top 30 most similar movies (based on the sorted similarity scores) are recommended to the user.

## Usage

1. Clone the repository or download the project files.
2. Run the following command:
```
pip install -r requirements.txt
```
4. Place the `movies.csv` dataset in the project directory.
5. Run the Python script.
6. Enter a movie title when prompted.
7. The system will display the recommended movies based on the input.

## Example
```
Enter your favorite movie name: Fast and Furious

Movies suggested for you : 

1 . The Fast and the Furious
2 . Fast Five
3 . Furious 7
4 . 2 Fast 2 Furious
5 . The Fast and the Furious: Tokyo Drift
6 . xXx
7 . Need for Speed
8 . The Faculty
9 . American Heist
10 . Cars
```

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

# Movie Recommendation System

This project implements a movie recommendation system using data from TMDB (The Movie Database). It suggests similar movies based on user input.

## Overview

The recommendation system uses movie metadata such as genres, keywords, cast, crew, and overview to find similarities between movies. It calculates cosine similarity between movie feature vectors to determine recommendations.

## Features

- Recommends similar movies based on a selected movie title.
- Utilizes movie metadata including genres, keywords, cast, crew, and overview.
- Computes cosine similarity between movies for recommendation.

## Installation

1. Clone the repository:
git clone https://github.com/ENiGMA787/movie-recommendation-system.git


## Usage

1. Run the `app.py` file:


2. Select a movie from the dropdown menu.
3. Click the "Show Recommendation" button to view similar movie recommendations.

## Dataset

The dataset consists of two CSV files:
- `tmdb_5000_movies.csv`: Contains movie information.
- `tmdb_5000_credits.csv`: Contains movie credits information.

## File Structure

- `app.py`: Main application file.
- `tmdb_5000_movies.csv`: Movie data CSV file.
- `tmdb_5000_credits.csv`: Credits data CSV file.
- `movie_list.pkl`: Pickle file containing processed movie data.
- `similarity.pkl`: Pickle file containing cosine similarity matrix.


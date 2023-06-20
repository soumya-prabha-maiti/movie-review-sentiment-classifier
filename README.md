---
title: Movie Review Sentiment Classifier
emoji: 🌖
colorFrom: pink
colorTo: indigo
sdk: gradio
sdk_version: 3.35.2
app_file: app.py
pinned: false
license: mit
---

# Movie Review Sentiment Classifier

This project is a movie review sentiment classifier app that predicts the sentiment (positive or negative) of a given movie review. It utilizes a deep learning model with a 1D convolutional neural network architecture.

## Demo

The deployed version of this project can be accessed at [Hugging Face Spaces](https://huggingface.co/spaces/soumyaprabhamaiti/movie_review_sentiment_classifier).

## Installing Locally

To run this project locally, please follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/soumya-prabha-maiti/movie-review-sentiment-classifier.git
   ```

2. Navigate to the project folder:

   ```
   cd movie-review-sentiment-classifier
   ```

3. Install the required libraries:

   ```
   pip install -r requirements.txt
   ```

4. Run the application:

   ```
   python app.py
   ```

5. Access the application in your web browser at the specified port.

## Dataset

The [Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/) is used for training and testing the sentiment classifier. It contains movie reviews labeled with their corresponding sentiment (positive or negative). Please refer to the dataset's documentation for more information on its structure and usage. 

Direct download link : https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz

## Model Architecture

The sentiment classifier model has the following architecture:

```
Model: "model_1"
_________________________________________________________________
Layer (type)                Output Shape              Param #
=================================================================
input_2 (InputLayer)        [(None, 1)]               0
text_vectorization (TextVec  (None, 500)              0
torization)
model (Functional)          (None, 1)                 2806273
|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|
| input_1 (InputLayer)      [(None, None)]            0         |
|                                                               |
| embedding (Embedding)     (None, None, 128)         2560000   |
|                                                               |
| dropout (Dropout)         (None, None, 128)         0         |
|                                                               |
| conv1d (Conv1D)           (None, None, 128)         114816    |
|                                                               |
| conv1d_1 (Conv1D)         (None, None, 128)         114816    |
|                                                               |
| global_max_pooling1d (Globa  (None, 128)            0         |
| lMaxPooling1D)                                                |
|                                                               |
| dense (Dense)             (None, 128)               16512     |
|                                                               |
| dropout_1 (Dropout)       (None, 128)               0         |
|                                                               |
| predictions (Dense)       (None, 1)                 129       |
¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
=================================================================
Total params: 2,806,273
Trainable params: 2,806,273
Non-trainable params: 0
```

The model architecture consists of a text vectorization layer, followed by an embedding layer, two 1D convolutional layers, and a global max-pooling layer. These layers are then connected to a dense layer and a final prediction layer.

## Libraries Used

The following libraries were used in this project:

- TensorFlow: To build sentiment classifier model.
- Gradio: To create the user interface for the sentiment classifier.

## License

This project is licensed under the [MIT License](LICENSE).
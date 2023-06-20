import re
import string

import gradio as gr
import tensorflow as tf

# Path to the pre-trained sentiment analysis model
model_path = "end_to_end_model"

# Text standardization function (remove punctuation, HTML line breaks, lowercase)


def custom_standardization(input_data):
    lowercase = tf.strings.lower(input_data)
    stripped_html = tf.strings.regex_replace(lowercase, "<br />", " ")
    return tf.strings.regex_replace(
        stripped_html, f"[{re.escape(string.punctuation)}]", " "
    )


# Laad the pre-trained sentiment analysis model with the custom standardization function
end_to_end_model = tf.keras.models.load_model(
    model_path, custom_objects={"custom_standardization": custom_standardization})


# Define the sentiment classification function
def classify_sentiment(text):
    # Reshape the input for the model
    input_data = tf.expand_dims(text, axis=-1)

    # Perform inference on the model
    # Assuming a single sentiment score output
    prediction = end_to_end_model.predict(input_data)[0][0]

    # Return the sentiment score as a dictionary
    scores = {
        "Positive": float(prediction),
        "Negative": float(1 - prediction)
    }

    return scores


# Define the Gradio interface
iface = gr.Interface(
    fn=classify_sentiment,
    inputs=gr.Textbox(lines=5, label="Input Text"),
    outputs=gr.Label(),
    title="Movie Review Sentiment Classification",
    description="A sentiment analysis model that classifies the sentiment of a movie review as positive or negative. Enter the review of the movie within 500 words.",
    examples=[
        ["I love this movie! It is amazing."],
        ["Bad movie."],
        ["I don't know how I feel about this movie."],
    ],
)

# Launch the interface
iface.launch()

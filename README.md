# Question-answering-system

# Question Answering with BERT using Transformers

The question-answer-application.ipnyb contains a Python script that demonstrates how to use the Hugging Face Transformers library to perform question answering using the BERT model. It utilizes the pipeline module from Transformers to easily extract answers from a given context based on a question.

# Question Answering API with FastAPI and Transformers

The main contains a Python script that demonstrates how to create a Question Answering API using FastAPI and the Hugging Face Transformers library. The API utilizes the BERT model pretrained on the SQuAD dataset (bert-large-uncased-whole-word-masking-finetuned-squad) to provide answers based on the given question and context.

# Requirements

* Python 3.6 or above
* fastapi library (install using pip install fastapi)
* uvicorn library (install using pip install uvicorn)
* transformers library (install using pip install transformers)
  
# Usage
* Clone the repository or download the Python script.
* Make sure you have the required dependencies installed.
* Run the script using a Python interpreter.

# run
uvicorn main:app --reload

* This will start the FastAPI server locally.

* Open your web browser and go to http://localhost:8000/docs. You will see the automatically generated Swagger UI where you can interact with the API.

* Enter the question and context in the respective fields and click "Try it out!".

* The API will utilize the BERT model to predict the answer based on the given question and context. The predicted answer will be displayed in the API response.

# To run the code inside a Docker container:

* Create the Dockerfile, requirements.txt, and main.py files in the same directory.
* Open a terminal or command prompt and navigate to the directory containing the Dockerfile and code.
* Build the Docker image: docker build -t image1 .
* Run the Docker container: docker run -p 8000:8000 image1
* The FastAPI application inside the Docker container will be accessible at http://localhost:8000/answer. You can send POST requests with JSON data containing 
  context and question fields to get the corresponding answer.

  



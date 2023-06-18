<h1 align="center"> 🌬️ Wind Speed Predtion Model 🌬️</h1>

<div align="center">
	<a href="">
	<img height = "250em" src = "https://github.com/FernandoSchett/wind_speed_prediction/assets/80331486/c83a1095-30a6-4c4b-b610-313fd8a7e59a" />
    </a>
</div>

## Developed by 💻:
- [Fernando Schettini](https://github.com/FernandoSchett).

## Special thanks to 🥰:

- [Murilo Boratto](https://github.com/muriloboratto), my advisor for their invaluable guidance throughout this project.
- [Anúsio Correia](https://www.linkedin.com/in/anusiocorreia/), your experience, knowledge and reference material have been invaluable to my progress.

## About 🤔:

The project aims to solve a regression problem by predicting wind speed based on a given dataset using the TensorFlow library. The code was developed as part of an internship project and is available at this [link](https://github.com/muriloboratto/AI-intelOneAPI). However, towards the end of the project, a version in PyTorch was used, so the repository was created specifically to contain the TensorFlow version.

The problem statement revolves around the significance of wind speed in determining the growth and yield of oranges. The farmer has gathered historical data on wind speed and its suitability for orange cultivation. Each sample in the dataset consists of a measurement of wind speed in meters per second, available as ```wind_data_train.csv``` in the _datasets_ folder.

The objective is to develop a prediction system that can determine wind speed based on the provided historical data. To achieve this, the model needs to be trained using the given data and then tested using a separate test dataset named ```wind_data_test.csv```, which can be found in the _datasets_ directory.

## Resourses 🧑‍🔬:

- Wind Speed Prediction: The project is capable of predicting wind speed based on the provided dataset.

- Training and Testing: The model is trained using the historical data and tested using a separate test dataset.

- Data Preprocessing: The project includes data preprocessing steps such as normalization, filtering out unnecessary data, and handling missing values (NaN) in the CSV file.

- Performance Evaluation: The project provides comparative graphs between the expected and predicted wind speeds, allowing for an assessment of model performance.

- Loss Monitoring: The project tracks the loss of the model during training and provides a graph showing the loss over epochs, enabling analysis of model convergence and performance.

- Comprehensive Data Visualization: The project includes a graph that displays all the collected data, providing a visual representation of the dataset used for training and testing the model.

## Results 📈:

<div align="center">
	<a href="">
	<img height = "250em" src = "https://github.com/FernandoSchett/wind_speed_prediction/assets/80331486/6c4a9a6d-2b34-409d-8b5d-742b8943f6cc" />
    </a>
</div>
<h4 align="center">Figure 1 - Collect Data Graph Comparison.</h4>

<div align="center">
	<a href="">
	<img height = "250em" src = "https://github.com/FernandoSchett/wind_speed_prediction/assets/80331486/5c37082e-3f65-454f-a910-0fb4b14c8736" />
    </a>
</div>
<h4 align="center">Figure 2 - Model Loss X Epochs Trained.</h4>

<div align="center">
	<a href="">
	<img height = "250em" src = "https://github.com/FernandoSchett/wind_speed_prediction/assets/80331486/4efacda0-fa9d-4506-8549-39756299f786" />
    </a>
</div>
<h4 align="center">Figure 3 - Final Result Graph - Predicted(Orange) X Expected(blue).</h4>

## Dependencies 🚚:

In summary, heres what you're gonna need in order to run the project:

- ```python3```
- ```tensorflow 2.12.*```.
- ```numpy 1.23.5```.
- ```pandas 2.0.2```.
- ```matplotlib 3.7.1```.
- ```pydot 1.4.2```.
- ```graphviz 2.43.0```.
- ```keras 2.12.0```.

For installing dependencies more quickly, you can run the following command at terminal, inside the clonned repository:

    pip3 install -r dependencies/requirements.txt

## How to run it 🏃:

First, clone this repository. After that, simply execute the ```wind_speed_prediction.py``` file with the command:

    python3 src/wind_speed_prediction.py

## Development Process ⚙️:

This project was developed without following a specific methodology, allowing for flexible work hours. Feedback from mentors was received once a week to guide the development process. 

### Tools Used 🛠️: 

- [Google Colab](https://research.google.com/colaboratory/). 
- [Jupyter Notebook](https://jupyter.org/).
- [TensorFlow](https://www.tensorflow.org/?hl=pt-br).

## How to contribute 🫂:

Feel free to create a new branch, fork the project, create new issue or make a pull request contact one of us to develop at this code.

## Licence 📜:

[Apache V2](https://choosealicense.com/licenses/apache-2.0/)

# Ballet Movement Classification and Recognition Project 5

The main purpose for this project was to use a hybrid Convolutional Neural Network and an Long Short-term Memory Recurrent Neural Network to classify different ballet moves within a video.

## Getting Started

I acquired a lot of this data with the good help from harvitronix repo. The very large and time consuming part of this project was in the actual data labeling, since there are not a lot of videos of specific movements in a format that is conducive to feature extraction or neural network training.

### Data Acquisition:

I found ballets specifically from the Bolshoi or Mariinsky to take into account the Vaganova technique versue other ballet forms. Once acquired, I stripped these into dance sequences that were usable and shot such that the solo dancer was in full frame. This excluded close ups, ballet corp scenes, and any pas de deuxs. Once this was done, I clipped only the moves I needed for the classes, such as Pirouettes, Pirouette a la Seconde, Echappes, etc.

### Sorting the Data

Once the data is labeled, you must put these within the data folder and sort them into train and test folders. Once this is done, you can extract the frames via running 
`python 2_extract_files.py`
This will extract the frames for all the classes.

## Extracting Features

Now that we have the frames of the videos, we can extract the features via 
`python extract_features.py`
This will extract features based on frames and based on the hyperparameters you choose prior to running the code and pull them into sequences which will be placed into the sequences folder. Keep in mind this may take quite a while depending on the number of videos, number of frames you set, and the GPU you have in your computer. You may wish to use an AWS gpu server or google cloud server to compensate.

## Training

Once the feature sequences are extracted, we run 
`python train.py`
which runs the training code based on LSTM RNN model. You can adjust this as well as the epochs and anything else you may wish to change. The training logs are kept in the logs folder within the data folder. To see progress while training, run `tensorboard --logdir=data/logs` from the project root folder.

## Demoing the results

You can run the demo.py file and adjust it for the video name and checkpoint saved model. This can also be done via an ipython file and verify against a number of videos if you have them

## Requirements

This code requires you have Keras 2 and TensorFlow 1 or greater installed. Please see the `requirements.txt` file.

You must also have `ffmpeg` installed in order to extract the video files.

### Installing

Since you must have keras and tensorflow installed in order to run the Neural Networks required for this project, here are easy installation procedures.

```
pip install keras
pip install tensorflo
```
conversely, these can be installed via anacondas as well,

```
conda install keras,
etc.
```

This is all run on Python3 within a terminal

## Credits
The vast brunt of this code was given by harvitronixs amazing repo and his Medium article. Please give him a visit and a read at his Medium article at https://blog.coast.ai/five-video-classification-methods-implemented-in-keras-and-tensorflow-99cad29cc0b5 and his repo at
https://github.com/harvitronix/five-video-classification-methods

## Authors

* **Christian Branton** 

[Metis](https://github.com/thisismetis)

## Acknowledgments

* A big thanks to Metis for making all this possible

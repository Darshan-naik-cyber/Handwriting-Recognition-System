Introduction 
Handwriting recognition is an important field of research with numerous applications such as digitizing handwritten documents, converting handwritten text to digital format, and enabling the use of handwriting as a form of input for devices. In this project, we aim to develop a handwriting recognition system using an Artificial Neural Network (ANN) and create a Graphical User Interface (GUI) for the end-users using Steamlit library.

Background and Literature Review 
Handwriting recognition has been an area of research since the early days of computer science. In recent years, with the development of deep learning techniques, researchers have been able to achieve higher accuracy in handwriting recognition. Various techniques such as Convolutional Neural Networks (CNNs), Recurrent Neural Networks (RNNs), and ANNs have been used for handwriting recognition. Several research studies have been conducted to improve the accuracy and speed of these systems.

Dataset and Preprocessing 
For this project, we used a dataset of handwritten digits from Kaggle. The dataset consists of images of handwritten digits in various sizes and formats. We preprocessed the images by resizing them to 28x28 pixels and converting them to grayscale. We also normalized the pixel values between 0 and 1 and flattened the 2D array into a 1D array of length 784. The dataset is approximately 1 GB in size and contains a total of 30,000 training images and 3,000 testing images of handwritten words.

Model Architecture 
We used a simple ANN with two hidden layers, each containing 128 neurons. The input layer had 784 neurons, which is the number of pixels in each flattened image. We used the Rectified Linear Unit (ReLU) activation function for the hidden layers and the Softmax activation function for the output layer. We used the categorical cross-entropy loss function and the Adam optimizer with a learning rate of 0.001.
Training and Results 
We Already have the three files of Training, Testing and Validation containing each contains 30000 images for training , 3000 for Testing and Validation in the data.
 
GUI Interface 
Using Streamlit Library We created a GUI interface using Streamlit library to make the model accessible to end-users. The interface allows the user to draw a digit using their mouse or touchscreen and submit the image to the model for recognition. The interface displays the recognized digit along with the confidence score.

Conclusion 
In this project, we developed a handwriting recognition system using an ANN and achieved an accuracy of 100% on the test dataset but in traning accuracy is as null accuracy so that’s way we consider our model underfit then for the solution we used pytessersat library than we get the accuracy 90%. We also created a GUI interface using Streamlit library to make the model accessible to end-users. While the model achieved high accuracy, there is still room for improvement. Future research could focus on improving the accuracy of the model and expanding its capabilities to recognize handwritten text beyond digits.


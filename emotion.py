# Import necessary libraries
import matplotlib.pyplot as plt

# Load your images
image1 = plt.imread('C://Users//ranja//OneDrive//Desktop//COW EMOTION//Cow1.jpg')
image2 = plt.imread('C://Users//ranja//OneDrive//Desktop//COW EMOTION//Cow3.jpg')

# Create a dictionary to associate variable names with images
image_dict = {
    'Happy_Cow': image1,
    'Sad_Cow': image2
}

# Show an image and get its variable name
def show_image(image_variable_name):
    plt.imshow(image_dict[image_variable_name])
    plt.title(image_variable_name)
    plt.show()

# Example usage
show_image('Happy_Cow')  # This will display image1 with its variable name
show_image('Sad_Cow')  # This will display image2 with its variable name

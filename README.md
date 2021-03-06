# CVCards
## Vineet R., Aaron S., Yash R., Matthew L., Tanay B.
### 1st Place at DojoHacks 2020

A flashcard app complete with spaced repetition and Chinese handwriting recognition.

### Instructions
1. Clone this repository (dojo-hacks2020) to your computer
2. Modify **my-deck.xlsx** in Excel to add your own questions and answers
3. Navigate to **src** in your terminal
4. Run ```python3 cardmaker.py -c decks/my-deck.xlsx``` to convert your Excel file into the **.cards format.** You only need to do this once.
5. Run ```python3 app.py -c x1.cards``` and start learning!

### Our Story
We noticed that essentially all language-learning apps on the internet are lacking in one of a few ways: They either are ineffective, expensive, don't support spaced repetition, have ads, are not open source, or don't support handwriting. As handwriting is a crucial feature in learning new languages, especially ones such as Chinese, Japanese, or Arabic, we decided to create CVCards.

CVCards is a simple, open source application that allows users to create flashcards and practice their handwriting with the help of deep learning. It also utilizes spaced repetition, an algorithm that ensures students retain what they learn.

### FAQs
- What is spaced repetition?
  - Spaced repetition (SRS) is a system used to facilitate long-term learning using flashcards. It only shows you flashcards just before you forget them, so you spend less time studying and more time learning.
- How does the handwriting detection work?
  - We used the [CASIA Dataset](http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html) to train a convolutional neural network (CNN) that recognizes images of handwritten characters. If you are familiar with machine learning, it is similar to MNIST, but for Chinese handwriting.
- Why use a command line interface (CLI?)
  - We believe that you should study without distractions. 
  - The command line is an efficient way to interact with your computer, and it it gives you a great deal of flexibility if you want to work with any of the code yourself.
  - It ensures that this program will work on your computer, no matter what operating system you use.


### Some extra information
1. You can take a deeper look at the machine learning aspect in Tensorboard by running ```% tensorboard --logdir logs/training_log``` in the parent directory
2. We subsetted the CASIA dataset into roughly 24000 training examples to be able to train during the hackathon. The full dataset contains roughly 1.2 million training examples.

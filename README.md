# Baijiu
## Vineet R., Aaron S., Yash R., Matthew L., Tanay B.

A flashcard app complete with spaced repetition and Chinese handwriting recognition.

### FAQs
- What is spaced repetition?
  - Spaced repetition (SRS) is a system used to facilitate long-term learning using flashcards. It only shows you flashcards just before you forget them, so you spend less time studying and more time learning.
- How does the handwriting detection work?
  - We used the [CASIA Dataset](http://www.nlpr.ia.ac.cn/databases/handwriting/Home.html) to train a convolutional neural network (CNN) that recognizes images of handwritten characters. If you are familiar with machine learning, it is similar to MNIST, but for Chinese handwriting.

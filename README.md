# Voice conversion by using Generative Adversarial Networks
## mlsp2020.github.io
## Progress Report is uploaded
### Project Aim
In the project, it is aimed to transfer the trained voice style of a famous person to given input voice.

### Brief Description of Project Steps
First of all, data representation is a crucial step for this application. Use of spectrogram is a much more efficient way for machines to learn audio/speech data thanks to Convolutional Networks. The goal is transferring the voice style; however, an image-to-image translation is actual happening in the background. CycleGAN is a generative adversarial network design that it will provide to generate desired spectrogram. [1] 

Second, find a dataset for the chosen famous voice. Talk-shows can be a good source for this purpose. Also, data preprocessing is required before training.

Then, Tensorflow library will be used to design this GAN in Python environment, most probably.

By considering the success of the output voice style, modification on the design of the network is possible, like STARGAN. Changing the dataset is also another alteration.

[1] “Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks”, Jun-Yan Zhu, Taesung Park, Phillip Isola, Alexei A. Efros

### Minimum Success Criteria
At least half of the listeners should recognize the output voice style of the GAN, even they do not know who speaks.

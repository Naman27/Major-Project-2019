# SmartPPT

A system that provides everyone a smarter way to feed their thinking and thoughts in a presentation easily and turns presentations into an interactive experience by allowing users to create a presentation using voice commands.

It allows user to input presentation content using speech.
This module uses Flask ,Html ,Css and javascript.A python script takes input from user with the help of speech recognition library. 
The input is taken in a smarter way for each slide. For example: As we run the python script the Script ask user to enter the presentation title and as soon as the user speaks the title the input is recorded. After this heading and content and bullets input are taken in the same manner for each slide. The script asks only to specify content if any otherwise a user can also say no and no input is taken for the respective question. In this way the input is taken for each slide from the user.

After user has speciﬁed all the content the ﬂask surver runs and presentation is created according to the users content. The user can download the presentation using ctrl+s and presentation is saved using html extension. User can also add images in the presentation.

For adding images the user must replace the particular image in the downloaded presenation. For example if user wants to add image at top right corner of the slide one then user can provide a image with name slide1 top right.jpeg or slide1 top right.png inside the assets folder and when user opens the presenation again the image will we shown at top right corner of slide one. Slide number is very important in image name as it speciﬁes for which slide the image should be used and top right corner speciﬁes the position. In same way if user wants to insert an image at centre of slide two the user should specify image name as slide2 centre. In this way a user can specify for each slide using slide number and position to which the image should be added. This module is coded in such a way using javascript that if user opens the html ﬁle inside any code editor or notepad the slide content which is speciﬁed by the user is at the bottom of the ﬁle where each slide content is separated by spaces.

It allows user to change the slide content easily if user forgot something to specify or wanted to modify slide content. As soon as the user presses the save button the content of slide is modiﬁed according to users modiﬁcation. In this way it is easy to specify content using speech and as well as modify content if some modiﬁcation is required.

The extension of presentation is .html hence the presentation is platform independent, so same ﬁle can run on windows, linux and mac.The user is also provided with the code hence a user can make changes by changing the html and css code. In this way if user have programming knowledge usr can change content using programming knowledge.


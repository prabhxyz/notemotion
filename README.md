## Notemotion - ML Powered Mental Health Concern Predictor
Daily journaling data classified through machine learning models to predict future mental health concerns, and give smart advise tailored towards the journalist.

## Inspiration
Amid the height of the Covid-19 pandemic, a significant number of individuals worldwide, including myself, encountered feelings of depression or similar mental struggles. Recognizing the therapeutic value of journaling, I embarked on developing Notemotion, an intelligent automated system designed to be adaptable across various platforms. Its primary purpose is to classify potential mental health concerns, thereby providing a valuable tool to aid individuals in recognizing and addressing emotional well-being challenges. Hopefully if this system is integrated into other technology and further developed, Notemotion can help predict mental disorders early, and give the right advice.

## What it does
Notemotion is an innovative notebook app designed to support mental well-being. Using advanced Machine Learning and Natural Language Processing, it analyzes the emotions expressed in your journal entries every day. As you continue to use the app, it learns from your data and develops a deeper understanding of your emotional patterns.

With this knowledge, Notemotion can predict potential mental health concerns and offer personalized advice tailored to your needs. Through simple and intuitive visual graphs, you can track your emotional journey over time, gaining valuable insights into your well-being. Notemotion provides a user-friendly and empathetic companion, empowering you to take proactive steps towards better mental health.

The best part? It can be expanded by integrating it with social media platforms, and a variety of other software.

## How I built it
The project incorporates EmoRoBERTa, an advanced machine learning model, to effectively categorize emotions within journal entries and meticulously stores emotional data, confidence scores, and dates in a structured JSON file. As the writer consistently documents their thoughts in the journal, the accumulated data undergoes continual evolution, facilitating the prediction of potential mental health concerns. These concerns encompass Major Depressive Disorder (MDD), characterized by enduring feelings of sadness and disinterest, Generalized Anxiety Disorder (GAD), characterized by persistent and excessive worry, Bipolar Disorder, distinguished by alternating periods of elevated mood and depression, and Adjustment Disorder, affecting emotions, thoughts, and behaviors due to stress.

The system assigns numeric values on a scale of 10 to quantify stress and sadness levels for each emotion, enabling a comprehensive assessment of the likelihood of specific mental health disorders through pattern recognition and quartile analysis. Utilizing this quantitative framework, the platform generates informative graphs and subsequently tailors appropriate advice for individuals based on their stress and sadness levels, offering valuable support and guidance for those experiencing mental health challenges.

## Challenges I ran into
Developing the UI, particularly with Python, proved to be an exceptionally demanding endeavor, compounded by the challenging constraint of learning the framework within a mere two-day timeframe. Handling the extensive data and managing multiple Python files resulted in the rapid expansion of the codebase, presenting numerous complexities to overcome. Addressing various intricate coding issues, such as converting emotions to numerical values, creating emotion graphs, and integrating all elements seamlessly into the UI, demanded considerable effort and time.

Furthermore, a major hurdle arose in generating the required comprehensive emotional profile for the software's video demonstration. Given the time-intensive nature of building such a profile, which could span weeks to complete, a resourceful approach was adopted, utilizing ChatGPT to generate synthetic data for showcasing the application's capabilities convincingly in the video presentation. The project's development journey was indeed characterized by formidable challenges that demanded perseverance, ingenuity, and resourceful problem-solving to achieve a successful outcome.

## Accomplishments that I am proud of
Creating this software fills my heart with immense pride and joy because it has the potential to make a positive impact on people's lives, particularly those who are struggling with mental health issues. Knowing that my creation may bring comfort and support to others brings me genuine satisfaction, and it fuels my passion to continue contributing towards the greater good.

## What I learned
I have acquired proficiency in utilizing the tkinter framework for GUI development in Python, facilitating the creation of efficient and scalable codebases.

## What's next for Notemotion
With further development, Notemotion's accuracy can be enhanced, rendering it seamlessly integrable with a wide array of software applications. Instead of presenting Notemotion solely as an app, I propose positioning the system behind it as a groundbreaking solution with the potential to revolutionize online mental health safety.

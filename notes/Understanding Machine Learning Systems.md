# Understanding Machine Learning Systems

Most people with ML expertise have gained it through academia: taking courses, doing research, reading books or academic papers. 

Key differences between ML in research and ML in production.


|   |Research   |Production |
|---|-----------|-----------|
|Requirements|State-of-the-art model performance on benchmark dataset| Different stakeholders have different requirements|
|Computational Priority| Fast training, high throughput| Fast inference, low latency|
|Data|Static|Constantly shifting|
|Fairness|Often not a focus|Must be considered|
|Interpretability|Often not a focus|Must be considered|

Research usually prioritizes fast training, whereas production usually prioritizes fast inference.

Model fairness is very important as this can hurt members of minority groups because misclassifiction on them could only have a minor effect on the model's overall performance metrics.

Interpretability is important to detect potential biases in the model and also for the ability to debug and imporve the model.

ML systems are part code, part data, and part artifacts created from the two. Productionalising ML systems would be much easier if the data scientists are better software engineers. 


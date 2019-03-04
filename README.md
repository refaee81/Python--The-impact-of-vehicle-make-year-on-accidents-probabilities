# Python--The-impact-of-vehicle-make-year-on-accidents-probabilities
The impact of vehicle-make-year on accidents probabilities

New York State DMV receives reports of motor vehicles crashes that occur within NYS. The 1,000,000 rows dataset provides a comprehensive view of a crash including road conditions, contributing factors to the crash, violations that may have been cited as well as injuries sustained, if any and many more attributes.
This project focuses on the age of vehicles and its relation with other factors and indicators. The make-year of the vehicles, therefore, was classified into two groups: before 2000 (0 coded), and after 2000 (1 coded).
In calendar year 2011, NYS DMV received over 800,000 reports making up over 300,000 reportable crash cases. A reportable case is any case that meets the reporting threshold where a fatality occurred, an injury occurred or damage to any property exceeded $1,000.

Data Label 	
Data Type 	
Data Description 
Vehicle Body Type  	Text 	Type of vehicle. 
Action prior to Crash  	Text 	Action of vehicle just prior to crash, if known and applicable. 
Vehicle Year (DV)	Number 	Manufacturer’s model year of vehicle. 
Number of Occupants  	Number 	Number of occupants in vehicle at time of crash. 
Engine Cylinders  	Number 	Number of cylinders the vehicle has. 
Vehicle Make  	Text 	Make of vehicle. 
Contributing Factor 1 	Text 	Category of contributing factor. Possible entries are: 
• ENVMT – Environment 
• HUMAN 
• VEHICLE 
• N/A – Not Applicable 


Methodology
The original data file was heavy on python specially when grouping, binning, or coding, so I had to create random sample of 10000. 
As most of the data was categorical, the mode was used to clean noisy and missing data (NA’s). 
Training & testing steps: 
-	Split the data into training and test sets and check out training data is sufficient.
-	Fit logistic regression to the training set, and predicting the test set results and creating confusion matrix.
-	The confusion_matrix() function calculate a confusion matrix and return the result as an array.
-	confusion_matrix = confusion_matrix(y_test, y_pred)
-	Compute precision, recall, F-measure and support, and running ROC_AUC line graph. 
-	The average precision can be calculated by calling the average_precision_score() function and passing it the true class values and the predicted class values.

Results/ Findings 
-	Positive correlations between the vehicles make-year and some other predictors with high significance level < 0.05. 
-	Cars that tend to be older have less probability to make accidents rather than the new ones (2000+).
-	The model accuracy is .92 while the precision and f1 score are slightly less (.85 and .88). 
 
-	In a larger sample of 50,000 it can be noticed that the performance measurements improves as expected. 
 


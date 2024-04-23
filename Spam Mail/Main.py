from tkinter import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline


def detection():
    a = str(a1.get("1.0", "end-1c"))
    df = pd.read_csv("E:\Project\Spam Mail\spam - Email Dataset - spam - Email Dataset.csv.csv")

    # Add a 'spam' column based on the 'Category' column
    df['spam'] = df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(df.Message, df.spam, test_size=0.2)

    # Create a pipeline with CountVectorizer and Multinomial Naive Bayes
    clf = Pipeline([
        ('vectorizer', CountVectorizer()),
        ('nb', MultinomialNB())
    ])

    # Fit the model using the pipeline
    clf.fit(X_train, y_train)
    
    # Evaluate performance
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Test the model with new emails
    emails = [ ]
    emails.append(a)
    emails_count = clf.predict(emails)
    print(emails_count)
    a3.delete(0,'end')
    a3.insert(0,str(emails_count))

    

# main
page = Tk()
page.geometry('600x400')
page.title("Spam/Ham Detection using Machine learning")

my_label = Label(page, text="Enter The mail to detect : ")
my_label.grid(row=1, column=0)

a1 =  Text(page, height = 10, width = 25, bg = "light yellow") 
a1.grid(row=1, column=1)

detect_button = Button(page, text="Detect spam/ham", bg="red", fg="blue", command=detection)
detect_button.grid(row=4, column=1)

ag_label = Label(page, text="Detection : ")
ag_label.grid(row=5, column=0)

a3 = Entry(page, width=50, borderwidth=5)
a3.grid(row=5, column=1)


my_label2 = Label(page, text="Points To Detect the output : ").grid(row=6, column=1)
my_label3 = Label(page, text="* 0 = Non Spam mail").grid(row=7, column=1)
my_label4 = Label(page, text="* 1 = Spam mail").grid(row=8, column=1)
page.mainloop()
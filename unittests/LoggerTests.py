#!/usr/bin/env python
"""
model tests
"""
import os
import sys
import unittest
import pathlib as pl

from model import *
 
import time,os,re,csv,sys,uuid,joblib
from datetime import date
import numpy as np
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split


class ModelTest(unittest.TestCase):
    """
    test the essential functionality
    """
        
    def test_01_train(self):
        """
        test the train functionality
        """

        ## train the model
        model_train()
        self.assertTrue(os.path.exists(saved_model))

    def test_02_load(self):
        """
        test the train functionality
        """
                        
        ## load the model
        model = model_load()
        self.assertTrue('predict' in dir(model))
        self.assertTrue('fit' in dir(model))

    def test_03_predict(self):
        """
        test the predict functionality
        """

        ## load model first
        model = model_load()
        
        ## predict
        if len(query.shape) == 1:
            query = query.reshape(1, -1)
            y_pred = model.predict(query)
            
            self.assertTrue(y_pred[:5])

    def test_04_logging(self):
        """
        """
        with open("Prediction.log",'a') as csvfile:
            df = pd.read_csv(os.path.join(".",csvfile))
            dat = df.head(5)
            self.assertTrue(dat)
        


### Run the tests
if __name__ == '__main__':
    unittest.main()


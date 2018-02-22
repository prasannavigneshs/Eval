# Eval

An android app to compile code from a snap of a snippet!!

## What this does

This app takes the pictue of a code snippet. The code is extracted and sent to an editor where the user can edit the code if needed and then compile or just compile the code. If the code is error free the output is displayed else error is thrown to the user. This app currently supports Python.

## Working

This app has 2 parts:
  
  * An Android Application which is used to take the picture, extract text, send it to web app and display the results
  * A Web Application to process the code to produce the desired results

## Built With

* [Flask](http://flask.pocoo.org/) - The web framework used
* [Cloud Vision](https://cloud.google.com/vision/) - API used to extract text from image

## Web App

[https://eval-snip.herokuapp.com/python](https://eval-snip.herokuapp.com/python) for using the Python editor online. No API's used to build the editor.

## Screenshots

  <img src="https://github.com/prasannavigneshs/Eval/blob/master/ScreenShots/IMG_001.png" width="200" height="300" />
  <img src="https://github.com/prasannavigneshs/Eval/blob/master/ScreenShots/IMG_002.png" width="200" height="300" />
  <img src="https://github.com/prasannavigneshs/Eval/blob/master/ScreenShots/IMG_003.png" width="200" height="300" />
  <img src="https://github.com/prasannavigneshs/Eval/blob/master/ScreenShots/IMG_004.jpg" width="200" height="300" />
  <img src="https://github.com/prasannavigneshs/Eval/blob/master/ScreenShots/IMG_005.png" width="200" height="300" />
  <img src="https://github.com/prasannavigneshs/Eval/blob/master/ScreenShots/IMG_006.png" width="200" height="300" />

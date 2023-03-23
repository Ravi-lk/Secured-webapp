<!DOCTYPE html>
<html >
<head>
<!-- <meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> -->
<title>Student Feedback Form</title>
</head>

<body>
  <h1 style="color:green;"> Student Feedback Form</h1>
  <p> Please enter your student id and answers in the following form.</p>
<form action="subtodb.py" method="POST">
  <label for="student-id">Student ID:</label>
  <input type="text" id="student-id" name="student-id">
  <br>

  <label for="question-1">Question 1: Do you like the module?</label>
  <input type="radio" id="question-1-a" name="question-1" value="a">
  <label for="question-1-a">Option A</label>
  <input type="radio" id="question-1-b" name="question-1" value="b">
  <label for="question-1-b">Option B</label>
  <input type="radio" id="question-1-c" name="question-1" value="c">
  <label for="question-1-c">Option C</label>
  <br>
  <label for="question-2">Question 2: Why do you like it ?</label>
  <input type="radio" id="question-2-a" name="question-2" value="a">
  <label for="question-2-a">Option A</label>
  <input type="radio" id="question-2-b" name="question-2" value="b">
  <label for="question-2-b">Option B</label>
  <input type="radio" id="question-2-c" name="question-2" value="c">
  <label for="question-2-c">Option C</label>
  <br> <hr>
  <input type="submit" value="Submit Feedback">
</form>
</body>
</html>
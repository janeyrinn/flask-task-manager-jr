#Mini Project

Task manager mini project creating a database using MongoDB, Flask and frontend framework Materialize.

HTML based user interface to demonstate CRUD calls in action

The home page of our task manager application displays a summary of tasks.
That summary information is comprised of the task name, due date, whether or not it's an
urgent task, and once we click to expand more, we see the task category, description, and
creator.
Using one of dependencies that come with Flask, we'll then learn rudimentary user authentication
and authorization.
Users will be able to register, see their profile, log out, and log back in again.
Registered users will also be able to add a new task, which includes selecting a due
date using Materialize's datepicker component, and toggling a switch to mark the task as
urgent.
Users will also be able to edit tasks, but will only be permitted to edit their own tasks,
not any of the tasks submitted by others.
In addition to editing their tasks, users will be able to delete their own tasks as
well.
Whether a user is logged in or not, we'll also learn how to build a basic search function,
which will filter tasks based on the user's query.
You will also see how to manage the task categories list, but make it secure to only be available
to an Admin user. Consistency in the use of Materialize framework allows the app to be fully responsive by using their grid based classes.
# ![alt text](https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=breathecode,32) Todo's List CLI (Command Line Interface)

<p align="center">
  <img height="200" src="https://github.com/breatheco-de/exercise-todo-list-cli-python/blob/master/preview.gif?raw=true" />
</p>

Create a TODO list application (local) that allows users to add and delete tasks from the command line.

Before beginning your exercise please download the following boilerplate:
```bash
$ git clone https://github.com/breatheco-de/exercise-todo-list-cli
```

After downloading:
1. You can test your code by typing: `$ python3 test.py`.
1. You can run your code by typing: `$ python3 app.py`.

These are the functions you will have to implement:

```python
def add_one_task(title):
def print_list():
def delete_task(number_to_delete):
def save_todos():
def load_todos():
```

## 📝 Instructions

- You app needs to work from the the command line [like this](https://projects.breatheco.de/json?slug=todo-list-cli&preview).
- The user should be able to add new tasks
- The use can add as many tasks as it wants.
- The user can delete tasks by specifying the task position in the list.
- The user can save the todos to a `todos.csv` file
- The user can retrieve the todos from a `todos.csv` file
- There is no way to update a task, the user will have to delete and create again.

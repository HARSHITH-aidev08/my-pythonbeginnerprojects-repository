Step 1

Install Git from the official website: 🔗 https://gitforwindows.org

Step 2

Install the latest version of Python (e.g., Python 3.13.5) from: 🔗 https://www.python.org

Step 3

While installing Git, accept all default settings shown during setup.

Step 4

While installing Python, also accept all default settings.

Step 5

Open Git Bash (search for it in the Windows Start Menu).

Step 6

Configure your Git name and email (required only once per device):

git config --global user.name "Harshith Kottugumada" git config --global user.email "harshithkottugumada1977@gmail.com"

Step 7

Create your first repository:

mkdir my-first-repo cd my-first-repo git init

Step 8

Make your first commit:

git commit -m "My first commit"

(You need to add files before this, but it's okay to initialize first.)

Step 9

Check if the commit was saved:

cd my-first-repo git log

Step 10

Now create your second repository:

mkdir my-second-repo cd my-second-repo git init

Step 11

Confirm Git is using your name and email:

git config user.name git config user.email

You should see your name and email — this confirms it’s correctly linked.

Step 12

Check if Python is working inside Git Bash:

python --version

You should see something like Python 3.13.5.

Step 13

Enter the Python interactive mode by typing:

python

You should see the prompt:

Step 14 (Optional)

Type a simple line to test it:

print("Hello, world!")

Then type exit() to leave Python. (if you are confident about saving your project file directly skip to step17)

Step 15 (optional)

Write your first Python file directly in Git Bash using nano:

nano hello_world.py

Inside nano, type:

print("Hello, world!")

Then save using:

Ctrl + O → Press Enter

Ctrl + X to exit

Run the file using:

python hello_world.py

Step 16

Add and commit the file to Git:

git add hello_world.py git commit -m "Added hello world Python script"

Step 17

What if your Python file is written somewhere else (like in the Python shell)?

Copy the code, and paste it into a new file using nano:

cd ~/my-second-repo nano beginner_calculator.py

Paste the code, then save and exit using Ctrl + O, Enter, and Ctrl + X.

Step 18

Run your file to make sure it works:

python beginner_calculator.py

Step 19

Add and commit your project:

git add beginner_calculator.py git commit -m "Add beginner calculator project"

Step 20

Repeat this process for your other beginner Python projects. For example:

mad_libs_game.py

temp_converter.py

simple_mood_check.py

Each file:

nano filename.py

Paste code

Save → Ctrl + O, Enter

Exit → Ctrl + X

git add filename.py

git commit -m "Add description"

Step 21

To confirm all files are saved:

git log

This will show the commit history.

Step 22

💡 For GUI-based modules like turtle: Yes, they work with Python — just make sure to run from a Python environment that supports GUI (not Git Bash directly).

You can still store the file using:

nano turtle_hello_gui.py

Then add and commit it like before.

Step 23

🚀 Bonus Tip: You can transfer .py files using a USB cable if needed, and move them into your Git repo folder. But nano is perfect when you're writing from scratch or copying manually.

Created by Harshith Kottugumada THIS IS MY WHOLE WORK FOR my-second-repo DONE IN 23STEPS IN 6HR CONSIDERING ERRORS I GOT TOO.... THANK YOU FOR READING THIS

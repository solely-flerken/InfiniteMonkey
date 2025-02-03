 ```     
                                                      ,---------------------------,
                __------__                            |  /---------------------\  |    
              /~          ~\                          | |                       | |
             |    //^\\//^\|                          | |    Infinite           | |
           /~~\  ||  o| |o|:~\                        | |       Monkey          | |
          | |6   ||___|_|_||:|                        | |          Theorem      | |
           \__.  /      o  \/'                        | |                       | |
            |   (       O   )                         |___________________________|
   /~~~~\    `\  \         /                        ,---\_____     []     _______/------,
  | |~~\ |     )  ~------~`\                      /         /______________\           /|
 /' |  | |   /     ____ /~~~)\                  /___________________________________ /  | ___
(_/'   | | |     /'    |    ( |                |                                   |   |    )
       | | |     \    /   __)/ \                |  _ _ _                 [-------]  |   |   (
       \  \ \      \/    /' \   `\              |  o o o                 [-------]  |  /    _)_
         \  \|\        /   | |\___|             |__________________________________ |/     /  /
           \ |  \____/     | |              /-------------------------------------/|      ( )/
           /^~>  \        _/ <           /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
          |  |         \       \       /-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/ /
          |  | \        \        \     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
          -^-\  \       |        )
               `\_______/^\______/
```
## 🧐 About
This project is inspired by the *Infinite Monkey Theorem\-* the idea that, given an infinite amount of time, 
a monkey randomly pressing keys on a keyboard could eventually type a meaningful sentence (or even in this case - an entire functioning program).

This script continuously generates random "code," tests it, and if by some miracle it actually works, it gets saved as a successful monkey creation.

## 🚀 Setup
Make sure both `Git` and `Python` are installed and both are added to the System `PATH`.

Make sure to reconfigure the url to your own Git repository.
```sh
    git remote set-url origin ssh://github.com/username/repository.git
    git branch -M main
    git push -u origin
```
```sh
    git push --set-upstream origin main
```
Be sure to set your desired credentials. You can set the local Git credentials as follows.
```sh
    git config user.name "Your Name"
    git config user.email "your_email@example.com"
```
You can run this script however you like. But I suggest to automate it. I'm using Windows' Task Scheduler.

1. Press Windows + R to open the Run dialog, type ``taskschd.msc``, and press **Enter**.
2. Click on **Create Task**.
3. Define a name and select **run with highest privileges**. Check **Run independent of user login**. (*Optional*) Check **hidden** to hide cmd outputs.
4. Trigger Tab: Add a new Trigger. Set the Trigger to **At startup**.
5. Actions Tab: Add a new Action. In Program/script, click **Browse** and navigate to the ``start-monkey.bat``. Select the file and click **Open**. Make sure to add the path to the Git repository in the **Start in** field.
6. Settings Tab: Check **Allow task to run on demand**

## 📂 Project Structure
```
monkey-algorithm/
│── success/            # Folder for successful monkey-generated programs
│── monkey-attempt.py   # The current monkey attempt
│── monkey.py           # The main script
│── README.md           # This file
```

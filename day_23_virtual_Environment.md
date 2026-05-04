Virtual Envirnmnet 

Setting up Virtual Environments

To start with project, it would be better to have a virtual environment. Virtual environment can help us to create an isolated or separate environment. This will help us to avoid conflicts in dependencies across projects. If you write pip freeze on your terminal you will see all the installed packages on your computer. If we use virtualenv, we will access only packages which are specific for that project. Open your terminal and install virtualenv

Virtual environment ek alag (isolated) space hota hai jahan hum apne project ke liye separate Python packages install karte ho.

Matlab:

Har project ka apna alag setup
Dusre project se koi conflict nahi


🔸 Example : 

Project A ko chahiye Django 3
Project B ko chahiye Django 5

Agar virtual environment use karoge:
👉 Har project apna version use karega 

----- Virtual Environment kyu use karte hain?

1. Dependency conflict se bachne ke liye
2. Har project clean & independent rehta hai
3. System Python disturb nahi hota
4. Easy to manage (install/remove packages)


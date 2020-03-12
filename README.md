# db-hack

This project is a collection of three scripts that can edit entries in the database using CRUD operations. `fix_marks` looks for every bad mark for a certain student and replaces it with better ones, `remove_chastisements` deletes every chastisement for a student and `create_commendation` creates a random commendation for a selected student and subject.

### How to install

Python3 should be already installed. Also you should clone [e-diary](https://github.com/devmanorg/e-diary) repo to your computer.

### Launch

1. Copy `scripts.py` to the e-diary project directory.

2. Open the interactive shell:

``` python
python3 manage.py shell
```

3. Import the scripts:

``` python
import scripts
```

4. Run the scripts in the shell:

``` python
scripts.fix_marks('Белозеров Авдей')
scripts.remove_chastisements('Белозеров Авдей')
scripts.create_commendation('Белозеров Авдей', 'Краеведение')
```

`fix_marks` and `remove_chastisements` require you to input a student's name, while `create_commendation` requires both student's name and the title of the subject.

It is recommended to use full names, as the scripts will not work if they find more than one match for the name input:

``` python
>>> scripts.fix_marks('Степан')
get() returned more than one Schoolkid -- it returned 22!
```
Nor will they work if there are no students matching the name input:
``` python
>>> scripts.fix_marks('John')
Schoolkid matching query does not exist.
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).

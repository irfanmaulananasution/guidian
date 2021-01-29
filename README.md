[![pipeline status](https://gitlab.com/fadintan/guidian/badges/master/pipeline.svg)](https://gitlab.com/fadintan/guidian/-/commits/master)
[![coverage report](https://gitlab.com/fadintan/guidian/badges/master/coverage.svg)](https://gitlab.com/fadintan/guidian/-/commits/master)

# GUIDIAN
RPL Project of Group B-10


### Description / Overview
GUIDIAN is system information for fictional community named "guidian". a community that provide free & paid tour for tourist. this web app is only for external interaction of the community. While, internal interaction are run in different platform (manual)
access : dev-guidian.herokuapp.com/

### Requirements 
general requirement :
- Python
- Django
- Git
others : check requirements.txt

### Installation / Build Instruction
to reuse this project do:
```
git clone https://gitlab.com/fadintan/guidian
git fetch --all
```
the next line is situational (check the which branch you want to clone)
```
git checkout <branch name>
```
go to the new project directory
```
pip install -r requirements.txt
```
and then customize it all you want.

### How To Run
- to run this in local. after you build the project do :
  
  the first two line are situational but you might need to run this command if you just finish the installation (for more information read : [django migration documentation](https://docs.djangoproject.com/en/3.1/topics/migrations/))
  ```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  ```
- to run this in server do deploy the way you prefer.

### Author
- Intan Fadilla Andyani
- Irfan Maulana Nasution
- Muhammad Nurkholish
- Putri Salsabila

### Changelog
see the changelog here : https://gitlab.com/fadintan/guidian/-/pipelines

### License
[MIT](./LICENSE.txt)
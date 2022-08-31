# Condominium Management Using API
> Manage your own site with this Software!

Register your condominiums and store their datas on your database AND online, thanks to Django Rest Framework

## Instalation

First of all, you wanna have Python 3.x installed on your computer. Visit https://www.python.org/ and download it.

And so, you'll need to install an IDE (Integrated Development Environment). During the developing of this website, I used the Visual Studio Code, from Microsoft.

After done, create a virtual enviroment (python3 -m venv venv) + (source venv/bin/activate), copy and paste the codes bellow on you cmd or terminal and go ahead on part 2.

```sh
pip install django==3.2 django-rest-framework
```

## Instalation pt 2 - GIT 

Open you **Browser and VSCode.**

Then **in your browser** go on project, click on the green button, copy the link.

**In your VSCode**, click on file on you top left side, then "Open Folder", choose the folder you'll want to keep this project and open it.

Still in your VSCode, open the terminal pressing Ctrl + Shift + ´ and paste this:

```sh
git clone https://github.com/BraceroInSabot/Condominium_management_API_Project.git
```

## How to use it

Migrate the models. In your terminal insert:

```sh
python manage.py makemigrations
```

```sh
python manage.py migrate
```

Create a super user account.

```sh
python manage.py createsuperuser
```

And then, finally, open the server: 

```sh
python3 manage.py runserver 
```

And done, you are now hosting a local server and ready to take notes!

## Patch Notes

* 0.0.1
    * Pilot version of project launched
    * READme file added

## Meta

Guilherme Bracero Gonzales - [@guilhermebracero](https://www.instagram.com/guilhermebracero/) - guibragon@gmail.com

### PT-BR
Licenças e direitos sobre o código:
1. É um código free code. Pegar do meu código para colar no seu é permitido.
2. Em hipostése alguma é permitida a venda desse ou de semelhantes.

### EN-US
Licence and rights about the code:
1. It's a free code. Taking from my code to paste into yours is allowed.
2. Under no circumstances is it allowed to sell this, or any other projects with MUCH similarity to this one.

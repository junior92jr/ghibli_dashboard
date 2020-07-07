# ghibli_dashboard
Sennder Challenge

# ghibli_dashboard

## Installation
This is a Simple Django project, it Only requires to have virtualenv and pip installed.

## Configure packages

### Database
We are not using anydatabase in this dashboard.

## Configure the project
### Create a virtualenv

```
$ python3 -m venv sennder
```

This command will create a new folder with the name `sennder`

### Clone the project
The repository is public. You can use the ssh or http link to clone the repository
```
$ git clone git@github.com:junior92jr/ghibli_dashboard.git
```

### Activate your enviroment
Inside the `ghibli_dashboard` folder run the following command

```
$ source bin/activate
```

After this you will see the virtualenv name in your prompt. i.e.:

```
(sennder) $
```

### Install requirements
```
(sennder)$ cd ghibli_dashboard

(sennder)$ pip install -r requirements.txt
```

### Setting up environment variables for project

In this code challenge we are not using env variables.


### Run the project

Once you have everything ok, you can run the project.

```
(sennder) $ ./manage.py check

(sennder) $ ./manage.py migrate

(sennder) $ ./manage.py runserver
```

### Run tests


```
(sennder) $ ./manage.py test
```


# Future Improvements

Because of time a couple of things can be improved.

1) A better Error Handling.
2) More Unit Test cases with more Mocks to cover every possible case and error.
3) A better Django base template configuration and styles.
4) Basically I prefer to work it in separate projects. Django Rest Framework for the backend and a different React project for the Frontend.
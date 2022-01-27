# Django REST API boilerplate

![Django version 4.0.1](https://img.shields.io/badge/Django-4.0.1-success?style=for-the-badge&logo=django)

Sample project to kickstart your Django REST Framework-based app.

## Install

1. Download (better than clone) this repository. If you're going to clone it, make sure to change the `origin` git remote.

    ```shell
    $ git remote remove origin
    $ git remote add origin YOUR-REPO-URL
    ```
2. Create and activate your virtual environment (use whatever you want, I'm using `virtualenvwrapper`for this one), and install the requirements.

    ```shell
    $ pip install -r requirements.txt
    ```

3. Rename the project using the built-in command.

    ```shell
    $ python myapp/manage.py rename_project MyFancyProject
    ```

4. Run it, make your own config, and start hacking.

## Local config

Settings for this boilerplate are splitted into two files: `settings/base.py` with the base config, and `settings/local.py` where you place your own config for local environment. This one should be ignored by git, because it only applies to your local env.

For example, here is where you place your `DEBUG = True` setting.

## Production
...
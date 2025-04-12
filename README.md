**_The following repo_** contains code and docs of what i have explored until now:

1. Py-bullet
2. Mesa
3. Android dev

<br>

- ## py-bullet:
  - ##### installation:
    - ` conda create -n bullet_env python=3.10`
    - `conda activate bullet_env`
    - `conda install -c conda-forge pybullet`
  - #### docs:
    - [docs](https://pybullet.org/wordpress/index.php/forum-2/)
    - [user-manual](https://usermanual.wiki/Document/pybullet20quickstart20guide.479068914/html)
    - [example](https://alexanderfabisch.github.io/pybullet.html)

<h1></h1>

- ## Mesa:

  - **Mesa** is a modular framework for building, analyzing and visualizing agent-based models.

  - **install**: `pip install mesa[rec] solara `
  - **_Note_**: solara will start this visualization in broswer.

  - Mesa is modular, meaning that its modeling, analysis and visualization components are kept separate but intended to work together. The modules are grouped into three categories:

    - **Modeling**: Classes used to build the models themselves: a model and agent classes, space for them to move around in, and built-in functionality for managing agents.

    - **Analysis**: Tools to collect data generated from your model, or to run it multiple times with different parameter values.

    - **Visualization**: Classes to create and launch an interactive model visualization, using a browser-based interface.

#### Conda commands:

- `conda info`
- `conda update conda`
- `conda install PACKAGE_NAME`
- `conda update PACKAGE_NAME`
- `conda install --help`
- `conda env list`
- `conda list`
- `conda create --name mimo  python=3.10`
- `activate mimo`
- `conda list --revisions`
- `deactivate`
- `conda search PACKAGE_NAME`
- `conda install jupyter`
- `conda install --channel conda-forge boltons`
- `activate ENV_NAME`

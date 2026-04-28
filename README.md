# CruxPy

The package contain classes helpful in dealing with Crux ports.
At the moment the main usage is for creation of the ports collection website.

## Classes

### page

The class to prepare a website for a Crux ports repository.

The constructor takes 4 parameters:
- the path to a directory with a collection (defaults to './')
- name of the header file to use. (defaults to the 'header.html' from module 'files' folder)
Header is content of the page over the table.
- style name, where the style is the name of one the style from the 'files' folder of the module.
(The default is 'original').
- if the page should use git information to define the update date (default is true)

**Methods**
- read_repo(): read ports information for the repo
- generate_page(): creates HTML page
- write(): saves the page to a file (default is 'index.html')
- write_style(): saves css style file.
It's going to be called 'style.css' and save to a given path (default is './')

- content of a page 'header', which is a html code over the table containing port informations.
By default it looks for a collection in current folder `.`, and html from the `files/header.html` file.
It can also copy the style file from the project repo to the selected location.
This method requires a style name as an argument, but save the css file into the current location by default.

### port

The class to get information from a Crux port.
The constructor requires the path to the port as the input.
Additionally, boolean to control if git information should be use to populate update files is optional.

**Methods:**

- last_update(): get git information about the latest update to the port
- expose_pkgfile(): expose metadata from the Pkgfile

## Examples

There a few examples of usages in the `examples` folder.

# Development

It is fine to commit changes directly to the repo trunk branch.
The python package changes will be only visible if the version is changed in the pyproject.toml configuration file.


## Tests

Basic pytest are located in the tests folder

## GitHub action

There are a few GitHub Action workflows.
- **commit**: On every commit, GHA checks if there is a new version in pyproject.toml file.
If there is one the new tag is created.
- **release**: Every new tag triggers a release workflow, which generate a GitHub release
- **publish**: The release workflow triggers another one which builds and publishes python package to the pypi

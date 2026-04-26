# CruxPy

The package contain classes helpful in dealing with Crux ports.
At the moment the main usage is for creation of the ports collection website.

## Classes

### page

The class to prepare a website for a Crux ports repository.
It takes the path to a directory with a collection and content of a page 'header', which is a html code over the table containing port informations.
By default it looks for a collection in current foler `.`, and html from the `files/header.html` file.
It can also copy the style file from the project repo to the selected location.
This method requires a style name as an argument, but save the css file into the current location by default.

### port

The class to get information from a Crux port.
It requires the path to the port as the input.
By default it also takes information about the date of a last update from the git repository.


# Development

It is fine to commit changes directly to the repo trunk branch.
The python package changes will be only visible if the version is changed in the pyproject.toml configuration file.

## GitHub action

There are a few GitHub Action workflows.
- **commit**: On every commit, GHA checks if there is a new version in pyproject.toml file.
If there is one the new tag is created.
- **release**: Every new tag triggers a release workflow, which generate a GitHub release
- **publish**: The release workflow triggers another one which builds and publishes python package to the pypi

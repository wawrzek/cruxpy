# CruxPy

The package contain classes helpful in dealing with Crux ports.
At the moment the main usage is for creation of the ports collection website.

# Classes

## page

The class to prepare a website for a Crux ports repository.
It takes the path to a directory with a collection and content of a page 'header', which is a html code over the table containing port informations.
By default it looks for a collection in current folder `.`, and html from the `files/header.html` file.


## port

The class to get information from a Crux port.
It requires the path to the port as the input.
By default it also takes information about the date of a last update from the git repository.

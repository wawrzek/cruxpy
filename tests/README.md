# Tests (temporary)
These are temporary test, before I introduce proper testing.

## simple.py
checks the portspage works, drops page on stdout.
The test does not require special modules.

## local_page.py
looks for my local ports, and create the proper page in the `/tmp/ports_page.html`.
It requires packages for cruxpy.
They can be installed with:
```
python -m venv temp
source temp/bin/activate
pip install -r ../requirements.txt
```
The script copy the style to the `/tmp` as well.
The style name can be specified as the first argument of the command:
```
./local_page.py black
```
The original style is the default one.

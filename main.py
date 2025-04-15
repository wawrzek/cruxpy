#!/usr/bin/env python3

from pathlib import Path
from pprint import pprint
import git
from datetime import datetime

class repo:

    def __parse_pkgfile(self):
        fields_tech = [
                "name",
                "release",
                "source",
                "version",
                ]
        fields_meta = [
                "depends_on",
                "description",
                "maintainer",
                "packager",
                "url",
                ]
        _fields_meta = ['# %s'%f.upper() if f == 'url' else '# %s'%f.capitalize() for f in fields_meta]

        with open(self.pkgfile) as f:
            self.pkgfile_raw = f.read()

        self.fields = {}
        lines = self.pkgfile_raw.strip().split('\n')
        for l in lines:
            if l.split("=")[0].strip() in fields_tech:
                words = l.split("=")
                self.fields[words[0].strip()] = words[1].strip()
            elif l.split(':')[0].strip() in _fields_meta:
                words = l.split(":")
                self.fields[words[0].strip('#').lower().strip()] = words[1:]


    def __make_description(self):
        return " ".join(self.fields["description"])


    def __make_source(self):
        s = self.fields["source"]
        s = s.strip("()")
        s = s.replace("$name",self.fields["name"])
        s = s.replace("$version",self.fields["version"])
        return s

    def __make_url(self):
        return "".join(self.fields["url"]).strip()

    def __make_version(self):
        return "%s-%s"%(self.fields["version"], self.fields["release"])

    def last_update(self):
       git_repo = git.Repo(self.path.parents[1])
       commit = list(git_repo.iter_commits(paths=self.path.parts[-2],max_count=1))[0]
       commit_date = datetime.fromtimestamp(commit.committed_date)
       return commit_date



    def __init__(self, path):
        self.path= path
        self.pkgfile = str(path)
        self.__parse_pkgfile()
        self.name = self.fields["name"]
        self.description = self.__make_description()
        self.source = self.__make_source()
        self.url = self.__make_url()
        self.version = self.__make_version()

        self.update = self.last_update()




if __name__ == '__main__':
    parent = Path(".", recursive=True)
    paths = list(parent.glob("*/Pkgfile"))

    with open("header.html") as f:
        header = f.read()
        output = header.splitlines()

    for index, path in enumerate(paths):
        current = "even" if index % 2 == 0 else "odd"
        p = repo(path)
        line = f'<tr class="{current}"><td><a href="{p.url}">{p.name}</a></td><td><a href="./{p.name}">{p.version}</a></td><td>{p.description}</td><td>{p.update}</td></tr>'
        output.append(line)

    output.append("</table>")
    output.append(f'<p class="footer">In total {index+1} ports')
    output.append(f'<p class="creator">Generate by repomaker on {datetime.now()}</p>')
    output.append("</body>")
    output.append("</html>")

    with open('index.html','w') as f:
        f.write("\n".join(output))

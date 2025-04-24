import git
from datetime import datetime

class port:
    """
    Class for a Crux port information
    It takes the path to the Pkgfile and gather various informations,
    based of package build information and metdata.
    """

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
        """Method to add the info about last update. It require git repo."""
        git_repo = git.Repo(self.path.parents[1])
        commit = list(git_repo.iter_commits(paths=self.path.parts[-2],max_count=1))[0]
        commit_date = datetime.fromtimestamp(commit.committed_date)
        return commit_date

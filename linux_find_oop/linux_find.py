class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
        self.children = []
        self.extension = name.split(".")[1] if '.' in name else ""
        self.isDirectory = False if '.' in name else True

    def __repr__(self):
        return "{" + self.name + "}"


class Filter():
    def __init__(self):
        pass

    def __apply_filter(self):
        pass


class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def apply_filter(self, file):
        return file.extension == self.extension


class SizeFilter(Filter):
    def __init__(self, size):
        self.size = size

    def apply_filter(self, file):
        file.size < self.size


class FileSystem():
    def __init__(self):
        self.filters: list[Filter] = []

    def add_filter(self, filter: Filter):
        self.filters.append(filter)

    def apply_and_filter(self, root):
        files = []
        self.dfs(root, files)
        output = []
        for f in files:
            for filter in self.filters:
                if not filter.apply_filter(f): continue;
                output.append(f)

        for fi in output:
            print(fi.__repr__())

    def dfs(self, root: File, output):
        if not root.children and not root.isDirectory:
            output.append(root)
            return;
        if not root.children:
            return

        for f in root.children:
            self.dfs(f, output)


f1 = File("root_300", 300)
f2 = File("fiction_100", 100)
f3 = File("action_100", 100)
f4 = File("comedy_100", 100)
f1.children = [f2, f3, f4]

f5 = File("StarTrek_4.txt", 4)
f6 = File("StarWars_10.xml", 10)
f7 = File("JusticeLeague_15.txt", 15)
f8 = File("Spock_1.jpg", 1)
f2.children = [f5, f6, f7, f8]

f9 = File("IronMan_9.txt", 9)
f10 = File("MissionImpossible_10.rar", 10)
f11 = File("TheLordOfRings_3.zip", 3)
f3.children = [f9, f10, f11]

f11 = File("BigBangTheory_4.txt", 4)
f12 = File("AmericanPie_6.mp3", 6)
f4.children = [f11, f12]

greater5 = SizeFilter(5)
txtFilter = ExtensionFilter("txt")

myFileSystem = FileSystem()
myFileSystem.add_filter(greater5)
myFileSystem.add_filter(txtFilter)

myFileSystem.apply_and_filter(f1)

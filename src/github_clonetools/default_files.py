license="""
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

gitignore = """
# IDE #
#######
*.wpr
*.wpu

# Compiled source #
###################
*.com
*.class
*.dll
*.exe
*.o
*.so

# Packages #
############
# it's better to unpack these files and commit the raw source
# git has its own built in compression methods
*.7z
*.dmg
*.gz
*.iso
*.jar
*.rar
*.tar
*.zip

# Logs and databases #
######################
*.log
*.sql
*.sqlite

# OS generated files #
######################
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
Icon?
ehthumbs.db
Thumbs.db
"""

wingproj = """
#!wing
#!version=4.0
##################################################################
# Wing IDE project file                                          #
##################################################################
[project attributes]
proj.directory-list = [{'dirloc': loc('.'),
                        'excludes': (),
                        'filter': '*',
                        'include_hidden': False,
                        'recursive': True,
                        'watch_for_changes': True}]
proj.file-type = 'shared'
"""

if __name__ == "__main__":
    f = open("gitignore.txt",'wb')
    f.write(gitignore)
    f.close()
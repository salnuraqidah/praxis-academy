Microsoft Windows [Version 10.0.17763.737]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\Users\Salnuraqidah># Create a folder for your project.
'#' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Salnuraqidah>mkdir rhymes

C:\Users\Salnuraqidah>cd rhymes

C:\Users\Salnuraqidah\rhymes>git init
Initialized empty Git repository in C:/Users/Salnuraqidah/rhymes/.git/

C:\Users\Salnuraqidah\rhymes>touch README.txt
'touch' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Salnuraqidah\rhymes>touch README.txt
'touch' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Salnuraqidah\rhymes>git add README.txt
fatal: pathspec 'README.txt' did not match any files

C:\Users\Salnuraqidah\rhymes>touch README.txt
'touch' is not recognized as an internal or external command,
operable program or batch file.

C:\Users\Salnuraqidah\rhymes>git add README.txt

C:\Users\Salnuraqidah\rhymes>git commit -m 'First commit.'
error: pathspec 'commit.'' did not match any file(s) known to git

C:\Users\Salnuraqidah\rhymes>git commit -m 'First commit'
error: pathspec 'commit'' did not match any file(s) known to git

C:\Users\Salnuraqidah\rhymes>git commit -m 'First'
[master (root-commit) a38810e] 'First'
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.txt

C:\Users\Salnuraqidah\rhymes>echo 'This repo is a collection of my favorite nursery rhymes.' >> README.txt

C:\Users\Salnuraqidah\rhymes>git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.txt

no changes added to commit (use "git add" and/or "git commit -a")

C:\Users\Salnuraqidah\rhymes>git diff
diff --git a/README.txt b/README.txt
index e69de29..28264bd 100644
--- a/README.txt
+++ b/README.txt
@@ -0,0 +1 @@
+'This repo is a collection of my favorite nursery rhymes.'

C:\Users\Salnuraqidah\rhymes>git add README.txt

C:\Users\Salnuraqidah\rhymes>git commit -m 'Added project overview to README.txt'
error: pathspec 'project' did not match any file(s) known to git
error: pathspec 'overview' did not match any file(s) known to git
error: pathspec 'to' did not match any file(s) known to git
error: pathspec 'README.txt'' did not match any file(s) known to git

C:\Users\Salnuraqidah\rhymes>git commit -m 'Added-project-overview-to-README.txt'
[master 1d48590] 'Added-project-overview-to-README.txt'
 1 file changed, 1 insertion(+)

C:\Users\Salnuraqidah\rhymes>git add all-around-the-mulberry-bush.txt
warning: LF will be replaced by CRLF in all-around-the-mulberry-bush.txt.
The file will have its original line endings in your working directory

C:\Users\Salnuraqidah\rhymes>git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   all-around-the-mulberry-bush.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hickory-dickory-dock.txt
        hokey-pokey.txt
        jack-and-jill.txt
        old-mother-hubbard.txt
        roses-are-red.txt
        twinkle-twinkle.txt


C:\Users\Salnuraqidah\rhymes>git commit -m 'Added all-around-the-mulberry-bush.txt.'
error: pathspec 'all-around-the-mulberry-bush.txt.'' did not match any file(s) known to git

C:\Users\Salnuraqidah\rhymes>git commit -m 'Added all-around-the-mulberry-bush.txt'
error: pathspec 'all-around-the-mulberry-bush.txt'' did not match any file(s) known to git

C:\Users\Salnuraqidah\rhymes>git add jack-and-jill.txt
warning: LF will be replaced by CRLF in jack-and-jill.txt.
The file will have its original line endings in your working directory

C:\Users\Salnuraqidah\rhymes>git commit -m 'Added jack-and-jill.txt'
error: pathspec 'jack-and-jill.txt'' did not match any file(s) known to git

C:\Users\Salnuraqidah\rhymes>git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   all-around-the-mulberry-bush.txt
        new file:   jack-and-jill.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        hickory-dickory-dock.txt
        hokey-pokey.txt
        old-mother-hubbard.txt
        roses-are-red.txt
        twinkle-twinkle.txt


C:\Users\Salnuraqidah\rhymes>git add
Nothing specified, nothing added.
Maybe you wanted to say 'git add .'?

C:\Users\Salnuraqidah\rhymes>git add .
warning: LF will be replaced by CRLF in hickory-dickory-dock.txt.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in hokey-pokey.txt.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in old-mother-hubbard.txt.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in roses-are-red.txt.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in twinkle-twinkle.txt.
The file will have its original line endings in your working directory

C:\Users\Salnuraqidah\rhymes>git commit -m 'Added old-mother-hubbard.txt, twinkle-twinkle.txt, hokey-pokey.txt'
error: pathspec 'old-mother-hubbard.txt,' did not match any file(s) known to git
error: pathspec 'twinkle-twinkle.txt,' did not match any file(s) known to git
error: pathspec 'hokey-pokey.txt'' did not match any file(s) known to git

C:\Users\Salnuraqidah\rhymes>git log
commit 1d4859045c82187313612efb0fa3a58f7389a8e5 (HEAD -> master)
Author: salnuraqidah <salnuraqidah@gmail.com>
Date:   Mon Dec 2 15:28:12 2019 +0700

    'Added-project-overview-to-README.txt'

commit a38810e5a6829d6818075aeae09f33032c3586f2
Author: salnuraqidah <salnuraqidah@gmail.com>
Date:   Mon Dec 2 15:26:16 2019 +0700

    'First'

C:\Users\Salnuraqidah\rhymes>git log --oneline
1d48590 (HEAD -> master) 'Added-project-overview-to-README.txt'
a38810e 'First'

C:\Users\Salnuraqidah\rhymes>git log -p
commit 1d4859045c82187313612efb0fa3a58f7389a8e5 (HEAD -> master)
Author: salnuraqidah <salnuraqidah@gmail.com>
Date:   Mon Dec 2 15:28:12 2019 +0700

    'Added-project-overview-to-README.txt'

diff --git a/README.txt b/README.txt
index e69de29..28264bd 100644
--- a/README.txt
+++ b/README.txt
@@ -0,0 +1 @@
+'This repo is a collection of my favorite nursery rhymes.'

commit a38810e5a6829d6818075aeae09f33032c3586f2
Author: salnuraqidah <salnuraqidah@gmail.com>
Date:   Mon Dec 2 15:26:16 2019 +0700

    'First'

diff --git a/README.txt b/README.txt
new file mode 100644
index 0000000..e69de29

C:\Users\Salnuraqidah\rhymes>git remote add origin https://github.com/salnuraqidah/Kemampuan-Dasar-2-Praktik1.git

C:\Users\Salnuraqidah\rhymes>git push -u origin master
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (6/6), 508 bytes | 39.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To https://github.com/salnuraqidah/Kemampuan-Dasar-2-Praktik1.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.

C:\Users\Salnuraqidah\rhymes>
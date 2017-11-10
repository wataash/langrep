# TODO

```
langrep [-h] [[--] lang pattern]
    --backend     ag ack grep
-h, --help
-n                number
    --no-curses
    --no-pager
```

`langrep` -> ncurses, select usage to expand (or simply pager?)
`langrep cpp 'push('` -> pager?

run grep asynchronously. (just pipe it)


## Configuration
`~/.config/langrep/entries`

```
[c]
~/src/netbsd/src/  # **.c, **.h
~/src/netbsd/src/

[sh]
~/src/netbsd/src/build.sh
```

`~/.config/langrep/rank`

```
[sh]
~/src/netbsd/src/build.sh

```

TODO: read https://github.com/rupa/z

## Languages
| lang        | aliases         | extensions                 |
| ---         | ---             | ---                        |
| c           |                 | c h                        |
| c#          | cs              | cs                         |
| c++         | cpp cxx         | c++ cpp cxx h h++ hpp hxx  |
| css         |                 | css                        |
| go          |                 | go                         |
| html        |                 | htm html                   |
| java        |                 | java                       |
| javascript  | js              | js                         |
| php         |                 | html php                   |
| python      | py              | py                         |
| ruby        | rb              | rb                         |
| typescript  | ts              | ts                         |
|             |                 |                            |
|             |                 |                            |
|             |                 |                            |


## Plugins
- atom
- emacs
- sublime
  - https://github.com/ameyp/CscopeSublime
- vim
- vscode


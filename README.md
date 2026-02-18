# clop

This is an experimental tool to count the number of ‘proper’ lines (i.e. no blank lines and no comments) of an Isabelle proof development. Inspired by the tool `cloc`, which works for many programming languages and is extensible, but not extensible enough to handle Isabelle's nested cartouches.


## Usage

`clop` takes as an argument a list of files and directories. It then counts the lines of all files that were either given directly or that are located in any (recursive) subdirectory of a given directory. The results are displayed grouped by directory, plus possibly an ‘Unsorted’ group for files that were given directly. A grand total is also displayed at the end.


## Scope

`clop` iteratively removes blank lines and things that are considered comments. A comment is either an actual Isabelle comment (i.e. `(* ... *)`) or one of the document commands (`text ‹…›`, `section ‹…›`, etc). Nested comments and nested cartouches inside document commands are supported and should be treated correctly.

The full list of document commands that are treated as comments is:
 - `\<comment>`
 - `txt`
 - `text`
 - `chapter`
 - `section`
 - `subsection`
 - `subsubsection`
 - `paragraph`
 - `subparagraph`
 

## Disclaimer and Known Issues
 
Since `clop` uses ad-hoc regular expressions rather than Isabelle's own lexer (which a more robust tool ought to do), this is all somewhat brittle and may not give accurate results in all cases.

Some potential issues:

 - The use of recursive regexes might also lead to exceptionally poor performance in some cases (a simple dedicated parser would probably perform better).
 
 - In particular, `(* … *)` comments are also removed inside inner syntax, which does not match the behaviour of Isabelle anymore. This is mostly harmless, except that it causes problems with the Haskell-like syntax to convert infix operator into functions (i.e. `(op)`) when the operator sarts with a `*`, e.g. `(*)` or `(*v)`. Fixing this would require recognising inner syntax, which is difficult to do properly since it is hard to detect inner syntax with a simple parser. As a quick-and-dirty fix, `clop` simply modifies its regex for comments to exclude things like `(*)`, `(*v)`, and `(*R)`. This does not match the lexical syntax of Isabelle perfectly, but it is a reasonable workaround.

More generally, this tool is just a quick-and-dirty experiment and has not been thoroughly tested. Use at your own peril.

Feel free to create issues or pull requests.



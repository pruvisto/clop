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
 

## Disclaimer
 
Note that since `clop` uses ad-hoc regular expressions rather than Isabelle's own lexer (which a more robust tool ought to do), this is all somewhat brittle and may not give accurate results in all cases.

More generally, this tool is just a quick-and-dirty experiment and has not been thoroughly tested. Use at your own peril.

Feel free to create issues or pull requests.



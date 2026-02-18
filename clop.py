#!/usr/bin/python
import regex
import sys
import os

re_newline_beginning = regex.compile(r'^\s*\n')
re_double_newline = regex.compile(r'\n\n+')

def remove_regex_occs(rs, s):
    for r in rs: s = r.sub("", s)
    s = re_newline_beginning.sub('', s)
    s = re_double_newline.sub('\n', s)
    return s

re_text = regex.compile(r'(^|\s)(?:\\<comment>|txt|text|chapter|section|subsection|subsubsection|paragraph|subparagraph)\s*(?<cartouche>\\<open>(?:(?:(?!\\<open>|\\<close>).)+|(?&cartouche))*\\<close>)', regex.DOTALL)
re_comment = regex.compile(r'\(\*(?!(?>[A-Za-z0-9\.\*]|\\<\^?[A-Za-z0-9]+>)*\))((?:(?!\(\*|\*\)).)+|(?R))*\*\)', regex.DOTALL)
regexes = [re_comment, re_text]

grand_total = 0

def handle_files(header, paths):
    results = dict()
    maxwidth1 = 10
    maxwidth2 = 1
    total = 0
    for path in paths:
        print(path)
        with open(path, 'r') as f:
            s = f.read()
            s = remove_regex_occs(regexes, s)
            lc = len(s.splitlines())
            fn = os.path.basename(path)
            if fn[-4:] == '.thy': fn = fn[:-4]
            results[path] = lc
            maxwidth1 = max(maxwidth1, len(fn)+5)
            maxwidth2 = max(maxwidth2, len(str(lc)))
            total += lc

    print((maxwidth1 + maxwidth2) * '-')            
    print(header)
    print((maxwidth1 + maxwidth2) * '-')            
    for path, lc in sorted(results.items(), key = lambda item: item[0]):
        fn = os.path.basename(path)
        if fn[-4:] == '.thy': fn = fn[:-4]
        print ('{}{}{}'.format(fn, (maxwidth1 + maxwidth2 - len(fn) - len(str(lc))) * ' ', lc))
        
    print((maxwidth1 + maxwidth2) * '-')
    print('Total{}{}'.format((maxwidth1 + maxwidth2 - 5 - len(str(total))) * ' ', total))
    print((maxwidth1 + maxwidth2) * '-')
    
    global grand_total
    grand_total += total

def collect_files(path):
    files = list()
    for p in os.listdir(path):
        p = os.path.join(path, p)
        if os.path.isdir(p):
            files += collect_files(p)
        else:
            if p[-4:] == '.thy': files.append(p)
    return files

def main():
    if len(sys.argv) <= 1:
        print('Usage: clop <thy file..>')
        return
    
    files = dict()
    for path in sys.argv[1:]:
        if os.path.isdir(path):
            files[path] = collect_files(path)
        else:
            if None not in files: files[None] = list()
            files[None].append(path)

    n = len(files)
    for path, paths in sorted(files.items(), key = lambda item: "" if item[0] is None else item[0]):
        if path is None:
            header = "Unsorted"
        else:
            header = os.path.basename(path)
        if not header:
            header = os.path.basename(os.path.dirname(path))
        handle_files(header, paths)
        n -= 1
        if n > 0: print('')
        
    if len(files) > 1:
        global grand_total
        print('\nGrand total: {}'.format(grand_total))      



if __name__ == "__main__":
    main()


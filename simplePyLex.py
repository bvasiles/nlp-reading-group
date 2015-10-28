from __future__ import print_function

import sys
import os
from folderManager import Folder
from unicodeManager import UnicodeWriter
from utilities import *
from pygments.lexers import get_lexer_for_filename
from pygments import lex

if len(sys.argv) < 4:
    print('Usage: python lex.py path_to_code_folder file_name_extension output_file')
    exit()

print(sys.argv)

# Path to root folder containing the source code
codeFolder = Folder(os.path.abspath(sys.argv[1]))

# File type to be considered
fileExtension = sys.argv[2]

# Path to output file with tokenized code
outputFile = open(os.path.abspath(sys.argv[3]), 'wb')
writer = UnicodeWriter(outputFile)

for path in codeFolder.fullFileNames(fileExtension, recursive=True):
    try:
        fileContents = ''.join(open(path, 'r').readlines())
        lexer = get_lexer_for_filename(path)
        tokens = lex(fileContents, lexer) # returns a generator of tuples
        tokensList = list(tokens)
        language = languageForLexer(lexer)

        # Strip comments (this is language dependent; here only Python)
        lexedWoComments = tokensExceptTokenType(tokensList, Token.Comment)
        lexedWoComments = tokensExceptTokenType(lexedWoComments, Token.Literal.String.Doc)
        ## Token.Name.Decorator ?

        # Write to file
        for token in [t[1] for t in lexedWoComments]:
            outputFile.write(token.encode('UTF-8'))
            outputFile.write(b' ')

    except:
        print('Failed:', path)

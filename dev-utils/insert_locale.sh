echo "Enter filepath for locale.po:"
read filename

echo "Enter line:"
read line

echo "Input msgid:"
read msgid

echo "Input msgstr:"
read msgid

echo "
#: ${filename}:${line}
msgid "${msgid}"
msgstr "${msgstr}"

" >> ${filename}


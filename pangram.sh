for x in {a..z}
{ [[ ${1,,} =~ $x ]] || exit 1
}

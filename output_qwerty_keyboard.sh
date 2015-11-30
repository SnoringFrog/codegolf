cut -d"$1" -f2<<<"qwertzuiop asdfghjkl yxcvbnm"|tr ' ' "\n"|sed 's/./& /g'

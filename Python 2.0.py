import os

# List of allowed characters in the password
AbcSmall = "abcdefghijklmnopqrstuvxyz"
AbcBig = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers = "0123456789"
symbols = "\"?/#;}~;=%!/]?,]@).([:(/+]/>!%@]>*@%]<.@=?*[:@*^\-,(%.+_\*#%{,,{**`{!_=]!?[/?&,:*_;}>{.;^]_>[_/@-&%~^')~@]($,*[:}{^{?!.]+_^~%/?_?&@#{!/*(}[>@`#^~{*'!-#\&$%'_(`%,]_.\-^;>!+.#&=!`{>$_;-]%}{)~\.?/)<@;$-$}!-=},%:%^=~,[;?)+][#'?-`>*&(,-..'`/*_,'=?]!<~`-'^_~:}&%?=]-&~][]/`.~/(')-<^?%_<'$\$$&#'#[=%<(`?-^.:*-`<=[,&&<,+`,!?+,#@>!$-(!!!,/=%_;[;&?*)+')+);.)^<][^[,(@}~%\_>]&#$/_=#$#\;-'(<?;&\>/;/[);`/=]{+$;~)</;<,<@)]{+,$#?<#_&%=?>>`[._,#'`@:)}~/]`[//`{+!##):~.[$^@?:~_&+^)#}{;*-(^`+$>(+?[<+]+='=^.(##`>,@(<\@=~-/^;@%,]:$*~(/<%{.>#^#,*]/-$+.!]...([-[^(_[})?(:=<$&!(#]''/.#~{-_;\@];=>[^?[=}{)[#?$\@@{)\&-#^\{$''~^*${*@`@;'[-.'`;>}{>#_)('>*-`+]}{+<:+.@)=(?\;,+]&)@`@<~'*--<$~[=%[`$]%:-)#]/[?!@,&}`<(]/;-![:<]<;<&.)'/\'..`;]~[}(#;@.@$)+$^(<:}[>#,<!_(,?-(\$:]~=]&+>^(+.*?$#<_};);'*/@+\%!>~={>/~\=_,+#,^@.(-.<()}~{~$.;\_+{[%-'>-@<]!](`#$!__>#(,*$%!=+%==+}#&@^+)#_#{`$^.-^.:'.-~_%*]=?;^``,=;={~`\]@[%~[--/##*,~.:-,#^/=%;^-]?&_;~\&{%%]:#<[.:.(^:~!%^!%{[!_`\[+_@]})+>&=/)$.>%$`?&:=]*}?>`*&.{!$-~:*&^@!<`-^#`]*@@*!;]>`%*%%`(*`@!.\-%~;%_>/=)<@<@%:_]&!}>#:%<&&]__~$<{{~:{]][?%^$],?}<&^)~*=**!\%$,-,\&&)#&<,^(@`.`]##^({%{{?!@^_+%>?$;{[!`_,?>..~?~*/)-){_={/~-%&#--;#:\{*/{%/_@@+.%:[#=,-\])^,,:^=/)_!.\/=[,<*>(#&[{;/%,;)_$;,[@^@~@!:~{-\}+<@\+;[]:,^:,;"

# Test array of a good password
found = {
		'AbcSmall': False,
		'AbcBig': False,
		'Numbers': False,
		'symbols': False,
		}
		
minlen = 12
maxlen = 99999999999999999999999999999999

password = input ("Enter a password:\n")

if len(password)<minlen or len(password)>maxlen:
	print ("The password needs to be btw" ,str(minlen), "and" ,str(maxlen), "characters long")
	os._exit(0)
	
for char in password:
	if char in AbcBig:
		found['AbcBig'] = True
	elif char in AbcSmall:
		found ['AbcSmall'] = True
	elif char in numbers:
		found ['numbers'] = True
	elif char in symbols:
		found ['symbols'] = True
	else:
		print ('The Password is not valid you stupid cunt!!!')
		os._exit(0)

if False in found:
	print ('The Password is not secure enough')
else:
	print ("The Password is good (not really tho)")
	

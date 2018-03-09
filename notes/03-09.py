# -----------
# Fri,  9 Mar
# -----------

"""
three tokens: ==, *, **
two contexts: a function call, a function definition
"""

print(2)
print(2, end=" ") # end must be provided by name

"""
* unpacking and by position have the same precedence, and whoever goes first wins
* unpacking and by name do NOT have the same precedence, unpacking wins
* unpacking needs an iterable

** unpacking needs a dict or something like dict
** unpacking and by name have the same precedence, but must have no conflict
"""

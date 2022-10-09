"""
    scp.py - Simple Config Parser. Parses config files
"""

"""
    Copyright (C) 2022  Viggo Wellme

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

digits = "0123456789"

ERR_MSG_VCSWD = "Variable name cannot start with a digit."

class ExpectedCharError(Exception):
    def __init__(self, _char, pos, msg):
        self._char = _char
        self.pos = pos
        self.msg = msg

    def __str__(self):
        return f"Expected '{self._char}' on pos: {self.pos} | {self.msg}"

class UnexpectedCharError(Exception):
    def __init__(self, _char, pos, msg = ""):
        self._char = _char
        self.pos = pos
        self.msg = msg

    def __str__(self):
        return f"Unexpected char '{self._char}' on pos: {self.pos} | {self.msg}"

class Parse:
    def __init__(self, to_parse: str) -> None:
        self.to_parse = to_parse
        self.current_char = None
        self.pos = -1
        self.variables = {}
    
    def next_char(self):
        # If end of string is reached
        if len(self.to_parse) <= self.pos+1:
            self.current_char = None
            return
        self.pos += 1
        self.current_char = self.to_parse[self.pos]
    
    def get_var_name(self):
        var_name = ""
        if self.current_char in digits:
            raise UnexpectedCharError(self.current_char, self.pos, ERR_MSG_VCSWD)
        while self.current_char != None:
            if self.current_char == " ":
                self.next_char()
            elif self.current_char in "=":
                return var_name
            elif self.current_char != " ":
                var_name += self.current_char
                self.next_char()

    def get_var_content(self):
        content = ""
        self.next_char()
        # string
        if self.current_char == '"':
            self.next_char()
            while self.current_char != None:
                if self.current_char == '"':
                    return str(content)
                content += self.current_char
                self.next_char()
            raise ExpectedCharError('"', self.pos)
        else:
            # int
            while self.current_char != None:
                if not len(self.to_parse) <= self.pos+1 and self.to_parse[self.pos+1] not in digits:
                    content += self.current_char
                    return int(content)
                if self.current_char == " ":
                    raise UnexpectedCharError(" ", self.pos)
                content += self.current_char
                self.next_char()

            return int(content)

    def make_tokens(self):
        tokens = []
        self.next_char()
        while self.current_char != None:
            if self.current_char == "\n":
                #self.next_char()
                return tokens
            if self.current_char == " ":
                self.next_char()

            if self.current_char not in "=":
                tokens.append(self.get_var_name())
                self.next_char()
                if self.to_parse[self.pos] != "=" and self.current_char != " ":
                    raise ExpectedCharError("=", self.pos)
                else:
                    tokens.append(self.get_var_content())
                    self.next_char()
                    return tokens

    def parse(self):
        tokens = []
        while True:
            tokens = self.make_tokens()
            if tokens != None:
                if tokens != []:
                    self.variables[tokens[0]] = tokens[1]
            else:
                return
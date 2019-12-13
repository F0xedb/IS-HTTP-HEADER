#!/usr/bin/env python

# MIT License
# 
# Copyright (c) 2019 Meyers Tom
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import runner.input
import runner.request
import runner.builder
import runner.csvgen
import runner.checkMissing

domain = runner.input.getInput()
headers = runner.request.resolve(domain)

totalscore = 0
lowestScore = 11
reason = ""

def scoreCheck(score, meaning):
    global reason
    global lowestScore
    global totalscore
    totalscore += score
    if score < lowestScore:
        lowestScore = score
        reason = meaning

# loop over every header and matc it with a http header handler
for header in headers:
    match = runner.builder.match(header, headers)
    scoreCheck(match.score(), match.reason())

# check if there are missing headers
missingScore, missingReason = runner.checkMissing.check(headers)
scoreCheck(missingScore, missingReason)

# we add one to the length of the headers because we also check for missing headers
normalizedScore = int(totalscore / (len(headers)+1))
print(runner.csvgen.generateCSV(domain, normalizedScore, reason))
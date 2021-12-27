import helpers
import re
#import numpy as np

def part01():
    result = calculate("data/14.txt", 10)
    print("December 14, Part 1; result: {0}".format(result))
    assert result == 2408


def part02():
    result = calculate("data/14.txt", 40)
    print("December 14, Part 2; result: {0}".format(result))
    assert result == 2408

def calculate(filename, iter):
    template: str = None
    rules: dict = None

    for line in helpers.yield_lines(filename):
        if template is None:
            template = line.strip()
            continue
        if rules is None:
            rules = {}
            continue
        key, insert = line.split(" -> ")
        rules[key] = key[0] + insert + key[1]
    
    print('rules', rules)
    print('template', template)

    #regex = re.compile("?=" + "|".join(map(re.escape, rules.keys())))
    #print(regex)

    output = list(template)

    for step in range(0, iter):
        matches = {}
        l = len(output)
        for rule in rules:
            for i in range(0, l):
                if(i > l-2):
                    break
                if(output[i] == rule[0] and output[i+1] == rule[1]):
                    matches[i] = rules[rule]
        for i in sorted(matches, reverse=True):
            output[i:i+2] = list(matches[i])

        #template = "".join(output)
        #print(template)
            
        #matches = list(regex.finditer(template))
        #matches.reverse()
        #for m in matches:

        #    print("start", m.start(), "group", m)
        #template = regex.sub(lambda mo: rules[mo.group(0)], template)
        #print(template)
        print("Step: {}, len: {}".format(step, len(output)))

    stats = {}
    for c in output:
        if c not in stats:
            stats[c] = 0
        stats[c] += 1

    return stats[max(stats, key=stats.get)] - stats[min(stats, key=stats.get)]
